import json
from datetime import datetime

import requests

from helpers import database as db_helper

API_ENDPOINT = 'https://data.ny.gov/resource/unag-2p27.json'


def get_data_from_api(endpoint, limit=1000):
    endpoint += '?$limit={0}&$offset={0}'.format(limit)
    resp = requests.get(endpoint)
    json_data = json.loads(resp.text)
    return json_data


def get_foreign_id(db_conn, table_name, title):
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
    first_name, last_name = data['first_name'], data['last_name']

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
                                                                                     paid_by_another_entity=data[
                                                                                         'paid_by_another_entity'],
                                                                                     total_compensation=data[
                                                                                         'total_compensation'],
                                                                                     other_compensation=data[
                                                                                         'other_compensation'],
                                                                                     extra_pay=data['extra_pay'],
                                                                                     performance_bonus=data[
                                                                                         'performance_bonus'],
                                                                                     overtime_paid=data[
                                                                                         'overtime_paid'],
                                                                                     actual_salary_paid=data[
                                                                                         'actual_salary_paid'],
                                                                                     base_annualized_salary=data[
                                                                                         'base_annualized_salary'],
                                                                                     exempt_indicator=data[
                                                                                         'exempt_indicator'],
                                                                                     pay_type=data['pay_type'],
                                                                                     fiscal_year_end_date=fiscal_year_end_date)
        db_helper.execute_db_command(db_conn, insert_query)
        db_conn.commit()


def populate_data(endpoint=API_ENDPOINT, limit=1000, offset=1000, db_conn=None):
    if not db_conn:
        db_conn = db_helper.create_db_connection()

    print('Fetching data from #{0} until #{1}.'.format(limit, limit + offset))
    json_data = get_data_from_api(endpoint=endpoint, limit=limit)
    if json_data:
        for d in json_data:
            authority_id = get_foreign_id(db_conn, 'Authority', d['authority_name'])
            designation_id = get_foreign_id(db_conn, 'Designation', d['title'])
            department_id = get_foreign_id(db_conn, 'Department', d['group'])

            insert_person_record(db_conn, d, authority_id, department_id, designation_id)

        populate_data(endpoint=endpoint, limit=limit + offset, db_conn=db_conn)

    print('Data parsing complete!')
    db_conn.close()


def populate_incremental_data():
    query = """SELECT COUNT(id) FROM Person;"""
    db_conn = db_helper.create_db_connection()
    data = db_helper.fetch_data(db_conn, query)
    if data:
        limit = data[0][0]
        populate_data(endpoint=API_ENDPOINT, limit=limit, db_conn=db_conn)
