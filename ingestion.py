import json
from datetime import datetime

import requests

from helpers import database as db_helper

API_ENDPOINT = 'https://data.ny.gov/resource/unag-2p27.json'


def get_data_from_api(endpoint, limit=1000, offset=1000):
    endpoint += '?$limit={0}&$offset={1}'.format(limit, offset)
    resp = requests.get(endpoint)
    json_data = json.loads(resp.text)
    return json_data


def get_foreign_id(db_conn, table_name, title):
    if not title:
        return None

    query = """SELECT id FROM {1} WHERE title = "{0}";""".format(title, table_name)
    data = db_helper.fetch_data(db_conn, query)
    if data:
        return data[0][0]
    else:
        insert_query = """INSERT INTO {1} (title) VALUES ("{0}");""".format(title, table_name)
        db_helper.execute_db_command(db_conn, insert_query)
        db_conn.commit()
        return get_foreign_id(db_conn, table_name, title)


def insert_person_record(db_conn, data, authority_id, department_id, designation_id):
    first_name = data['first_name'] if 'first_name' in data else None
    last_name = data['last_name'] if 'last_name' in data else None

    if not (first_name and last_name and authority_id and department_id and designation_id):
        return None

    query = """SELECT id FROM Person 
                WHERE first_name="{first_name}" AND last_name="{last_name}" 
                AND authority_id="{authority_id}" AND department_id="{department_id}" 
                AND designation_id="{designation_id}";""".format(first_name=first_name, last_name=last_name,
                                                                 authority_id=authority_id, department_id=department_id,
                                                                 designation_id=designation_id)
    person_data = db_helper.fetch_data(db_conn, query)
    if not person_data:
        fiscal_year_end_date = None
        if data['fiscal_year_end_date']:
            fiscal_year_end_date = datetime.strptime(data['fiscal_year_end_date'], '%Y-%m-%dT%H:%M:%S.%f')
            fiscal_year_end_date = fiscal_year_end_date.strftime('%Y-%m-%d %H:%M:%S')

        total_compensation = data['total_compensation'] if 'total_compensation' in data else None
        other_compensation = data['other_compensation'] if 'other_compensation' in data else None
        extra_pay = data['extra_pay'] if 'extra_pay' in data else None
        performance_bonus = data['performance_bonus'] if 'performance_bonus' in data else None
        overtime_paid = data['overtime_paid'] if 'overtime_paid' in data else None
        actual_salary_paid = data['actual_salary_paid'] if 'actual_salary_paid' in data else None
        base_annualized_salary = data['base_annualized_salary'] if 'base_annualized_salary' in data else None
        pay_type = data['pay_type'] if 'pay_type' in data else None
        paid_by_another_entity = data['paid_by_another_entity'] if 'paid_by_another_entity' in data else None
        if paid_by_another_entity == "Y":
            paid_by_another_entity = 1
        else:
            paid_by_another_entity = 0
        exempt_indicator = data['exempt_indicator'] if 'exempt_indicator' in data else None
        if exempt_indicator == "Y":
            exempt_indicator = 1
        else:
            exempt_indicator = 0

        insert_query = """INSERT INTO Person (first_name, last_name, authority_id, department_id, designation_id,
            paid_by_another_entity, total_compensation, other_compensation, extra_pay, performance_bonus, overtime_paid,
            actual_salary_paid, base_annualized_salary, exempt_indicator, pay_type, fiscal_year_end_date) 
            VALUES ("{first_name}", "{last_name}", {authority_id}, {department_id}, {designation_id},
            "{paid_by_another_entity}", "{total_compensation}", "{other_compensation}", "{extra_pay}",
            "{performance_bonus}", "{overtime_paid}", "{actual_salary_paid}", "{base_annualized_salary}", 
            "{exempt_indicator}", "{pay_type}", "{fiscal_year_end_date}");""".format(first_name=first_name,
                                                                                     last_name=last_name,
                                                                                     authority_id=authority_id,
                                                                                     department_id=department_id,
                                                                                     designation_id=designation_id,
                                                                                     paid_by_another_entity=paid_by_another_entity,
                                                                                     total_compensation=total_compensation,
                                                                                     other_compensation=other_compensation,
                                                                                     extra_pay=extra_pay,
                                                                                     performance_bonus=performance_bonus,
                                                                                     overtime_paid=overtime_paid,
                                                                                     actual_salary_paid=actual_salary_paid,
                                                                                     base_annualized_salary=base_annualized_salary,
                                                                                     exempt_indicator=exempt_indicator,
                                                                                     pay_type=pay_type,
                                                                                     fiscal_year_end_date=fiscal_year_end_date)
        db_helper.execute_db_command(db_conn, insert_query)


def populate_data(db_conn, endpoint=API_ENDPOINT, limit=1000, offset=1000):
    print('Fetching data from #{0} until #{1}.'.format(limit, limit + offset))
    json_data = get_data_from_api(endpoint=endpoint, limit=limit, offset=offset)
    if json_data:
        for d in json_data:
            authority_id = get_foreign_id(db_conn, 'Authority', d['authority_name']) if 'authority_name' in d else None
            designation_id = get_foreign_id(db_conn, 'Designation', d['title']) if 'title' in d else None
            department_id = get_foreign_id(db_conn, 'Department', d['group']) if 'group' in d else None

            insert_person_record(db_conn, d, authority_id, department_id, designation_id)
        db_conn.commit()
        populate_data(db_conn=db_conn, endpoint=endpoint, limit=limit + offset, offset=offset)
    print('Data parsing complete!')


def populate_incremental_data():
    query = """SELECT COUNT(id) FROM Person;"""
    db_conn = db_helper.create_db_connection()
    data = db_helper.fetch_data(db_conn, query)
    if data:
        limit = data[0][0]
        if not limit:
            limit = 1
        populate_data(endpoint=API_ENDPOINT, limit=limit, db_conn=db_conn)
    db_conn.close()
