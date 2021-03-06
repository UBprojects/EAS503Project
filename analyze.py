from helpers import database as db_helper


def department_pays_most_and_least(limit=10):
    query = """SELECT
                    d.title AS max_department,
                    MAX(base_annualized_salary) AS max_pay,
                    MIN(base_annualized_salary) AS min_pay
                FROM
                    Person p
                    JOIN Department d ON d.id = p.department_id
                WHERE
                    base_annualized_salary >= 1
                GROUP BY
                    d.title
                ORDER BY
                    max_pay DESC
                LIMIT {limit};""".format(limit=limit)

    db_conn = db_helper.create_db_connection()
    data = db_helper.fetch_data(db_conn, query)
    db_conn.close()
    return data


def authority_pays_most_and_least(limit=10):
    query = """SELECT
                    lower(a.title) AS authority,
                    MAX(base_annualized_salary) AS max_pay,
                    MIN(base_annualized_salary) AS min_pay
                FROM
                    Person p
                    JOIN Authority a ON a.id = p.authority_id
                WHERE
                    base_annualized_salary >= 1
                GROUP BY
                    a.id HAVING max_pay!=min_pay
                ORDER BY
                    max_pay DESC
                LIMIT {limit};""".format(limit=limit)

    db_conn = db_helper.create_db_connection()
    data = db_helper.fetch_data(db_conn, query)
    db_conn.close()
    return data


def designation_pays_most_and_least(limit=10):
    query = """SELECT
                    lower(d.title) AS designation,
                    MAX(base_annualized_salary) AS max_pay,
                    MIN(base_annualized_salary) AS min_pay
                FROM
                    Person p
                    JOIN Designation d ON d.id = p.designation_id
                WHERE
                    base_annualized_salary >= 1
                GROUP BY
                    designation HAVING max_pay!=min_pay
                ORDER BY
                    max_pay DESC
                LIMIT {limit};""".format(limit=limit)

    db_conn = db_helper.create_db_connection()
    data = db_helper.fetch_data(db_conn, query)
    db_conn.close()
    return data


def department_pays_private_or_public(limit=10):
    query = """SELECT
                    d.title AS max_department,
                    CASE WHEN paid_by_another_entity=0 THEN COUNT(p.id) END AS private_pay,
                    CASE WHEN paid_by_another_entity=1 THEN COUNT(p.id) END AS public_pay
                FROM
                    Person p
                    JOIN Department d ON d.id = p.department_id
                GROUP BY
                    d.title
                ORDER BY
                    d.title
                LIMIT {limit};""".format(limit=limit)

    db_conn = db_helper.create_db_connection()
    data = db_helper.fetch_data(db_conn, query)
    db_conn.close()
    return data


def department_employees_full_part_time(limit=10):
    query = """SELECT
                    d.title,
                    SUM(case when pay_type='FT' then 1 else 0 END) as full_time,
                    SUM(case when pay_type='PT' then 1 else 0 END) as part_time
                FROM
                    Person p
                    JOIN Department d ON d.id = p.department_id
                GROUP BY
                    d.title
                ORDER BY
                    d.title
                LIMIT {limit};""".format(limit=limit)

    db_conn = db_helper.create_db_connection()
    data = db_helper.fetch_data(db_conn, query)
    db_conn.close()
    return data


def designation_avg_salary(limit=10):
    query = """SELECT
                    d.title, (AVG(base_annualized_salary)) as avg_salary
                FROM
                    Person p
                    JOIN Designation d ON d.id = p.designation_id
                GROUP BY
                    p.designation_id
                ORDER BY
                    avg_salary DESC
                LIMIT {limit};""".format(limit=limit)

    db_conn = db_helper.create_db_connection()
    data = db_helper.fetch_data(db_conn, query)
    db_conn.close()
    return data


def authority_avg_salary(limit=10):
    query = """SELECT
                    a.title, (AVG(base_annualized_salary)) as avg_salary
                FROM
                    Person p
                    JOIN Authority a ON a.id = p.authority_id
                GROUP BY
                    p.authority_id
                ORDER BY
                    avg_salary DESC
                LIMIT {limit};""".format(limit=limit)

    db_conn = db_helper.create_db_connection()
    data = db_helper.fetch_data(db_conn, query)
    db_conn.close()
    return data


def department_avg_salary(limit=10):
    query = """SELECT
                    d.title, (AVG(base_annualized_salary)) as avg_salary
                FROM
                    Person p
                    JOIN Department d ON d.id = p.department_id
                GROUP BY
                    d.title
                ORDER BY
                    d.title
                LIMIT {limit};""".format(limit=limit)

    db_conn = db_helper.create_db_connection()
    data = db_helper.fetch_data(db_conn, query)
    db_conn.close()
    return data


def department_employee_count_over_years(limit=10):
    query = """SELECT
                    d.title, 
                    sum(case when strftime('%Y', fiscal_year_end_date) = '2016' then 1 else 0 end) as year_2016,
                    sum(case when strftime('%Y', fiscal_year_end_date) = '2017' then 1 else 0 end) as year_2017,
                    sum(case when strftime('%Y', fiscal_year_end_date) = '2018' then 1 else 0 end) as year_2018
                FROM
                    Person p
                    JOIN Department d ON d.id = p.department_id
                GROUP BY
                    d.title
                ORDER BY
                    year_2016 DESC, year_2017 DESC, year_2018 DESC
                LIMIT {limit};""".format(limit=limit)

    db_conn = db_helper.create_db_connection()
    data = db_helper.fetch_data(db_conn, query)
    db_conn.close()
    return data


def designation_employee_count_over_years(limit=10):
    query = """SELECT
                    d.title, 
                    sum(case when strftime('%Y', fiscal_year_end_date) = '2016' then 1 else 0 end) as year_2016,
                    sum(case when strftime('%Y', fiscal_year_end_date) = '2017' then 1 else 0 end) as year_2017,
                    sum(case when strftime('%Y', fiscal_year_end_date) = '2018' then 1 else 0 end) as year_2018
                FROM
                    Person p
                    JOIN Designation d ON d.id = p.designation_id
                GROUP BY
                    p.designation_id
                ORDER BY
                    year_2016 DESC, year_2017 DESC, year_2018 DESC
                LIMIT {limit};""".format(limit=limit)

    db_conn = db_helper.create_db_connection()
    data = db_helper.fetch_data(db_conn, query)
    db_conn.close()
    return data


def authority_employee_count_over_years(limit=10):
    query = """SELECT
                    a.title, 
                    sum(case when strftime('%Y', fiscal_year_end_date) = '2016' then 1 else 0 end) as year_2016,
                    sum(case when strftime('%Y', fiscal_year_end_date) = '2017' then 1 else 0 end) as year_2017,
                    sum(case when strftime('%Y', fiscal_year_end_date) = '2018' then 1 else 0 end) as year_2018
                FROM
                    Person p
                    JOIN Authority a ON a.id = p.authority_id
                GROUP BY
                    p.authority_id
                ORDER BY
                    year_2016 DESC, year_2017 DESC, year_2018 DESC
                LIMIT {limit};""".format(limit=limit)

    db_conn = db_helper.create_db_connection()
    data = db_helper.fetch_data(db_conn, query)
    db_conn.close()
    return data


def department_avg_salary_trend(limit=10):
    query = """SELECT
                d.title, 
                AVG(case when strftime('%Y', fiscal_year_end_date) = '2011' then base_annualized_salary else NULL end) as year_2011,
                AVG(case when strftime('%Y', fiscal_year_end_date) = '2012' then base_annualized_salary else NULL end) as year_2012,
                AVG(case when strftime('%Y', fiscal_year_end_date) = '2013' then base_annualized_salary else NULL end) as year_2013,
                AVG(case when strftime('%Y', fiscal_year_end_date) = '2014' then base_annualized_salary else NULL end) as year_2014,
                AVG(case when strftime('%Y', fiscal_year_end_date) = '2015' then base_annualized_salary else NULL end) as year_2015,
                AVG(case when strftime('%Y', fiscal_year_end_date) = '2016' then base_annualized_salary else NULL end) as year_2016,
                AVG(case when strftime('%Y', fiscal_year_end_date) = '2017' then base_annualized_salary else NULL end) as year_2017,
                AVG(case when strftime('%Y', fiscal_year_end_date) = '2018' then base_annualized_salary else NULL end) as year_2018
            FROM
                Person p
                JOIN Department d ON d.id = p.department_id
            GROUP BY
                d.title
            ORDER BY
                d.title
            LIMIT {limit};""".format(limit=limit)

    db_conn = db_helper.create_db_connection()
    data = db_helper.fetch_data(db_conn, query)
    db_conn.close()
    return data


def designation_num_employees(limit=10):
    query = """SELECT
                    d.title, COUNT(p.id) as num_employees
                FROM
                    Person p
                    JOIN Designation d ON d.id = p.designation_id
                GROUP BY
                    d.title
                ORDER BY
                    num_employees DESC
                LIMIT {limit};""".format(limit=limit)

    db_conn = db_helper.create_db_connection()
    data = db_helper.fetch_data(db_conn, query)
    db_conn.close()
    return data


def department_num_employees(limit=10):
    query = """SELECT
                    d.title, COUNT(p.id) as num_employees
                FROM
                    Person p
                    JOIN Department d ON d.id = p.department_id
                GROUP BY
                    d.title
                ORDER BY
                    num_employees DESC
                LIMIT {limit};""".format(limit=limit)

    db_conn = db_helper.create_db_connection()
    data = db_helper.fetch_data(db_conn, query)
    db_conn.close()
    return data


def authority_total_compensation(limit=10, year=2108):
    query = """SELECT
                    a.title,
                    sum(p.total_compensation) AS total_compensation
                FROM
                    Person p
                    JOIN Authority a ON a.id = p.authority_id
                WHERE
                    strftime ('%Y', fiscal_year_end_date) = '{year}'
                GROUP BY
                    a.title
                ORDER BY
                    total_compensation DESC
                LIMIT {limit};""".format(limit=limit, year=year)

    db_conn = db_helper.create_db_connection()
    data = db_helper.fetch_data(db_conn, query)
    db_conn.close()
    return data


def authority_total_employees(limit=10, year=2108, sort_by='ASC'):
    query = """SELECT
                    a.title,
                    COUNT(p.id) AS num_employees
                FROM
                    Person p
                    JOIN Authority a ON a.id = p.authority_id
                WHERE
                    strftime ('%Y', fiscal_year_end_date) = '2018'
                GROUP BY
                    a.title
                ORDER BY
                    num_employees {sort_by}
                LIMIT {limit};""".format(limit=limit, year=year, sort_by=sort_by)

    db_conn = db_helper.create_db_connection()
    data = db_helper.fetch_data(db_conn, query)
    db_conn.close()
    return data


def get_all_data():
    query = """select first_name "First Name", last_name "Last Name", fiscal_year_end_date "Fiscal Year End Date", base_annualized_salary "Base Annualized Salary",
                a.title "Authority Name", ds.title "Title", dp.title "Group"
                from Person p
                join Authority a on a.id = p.authority_id
                join Designation ds on ds.id = p.designation_id
                join Department dp on dp.id = p.department_id;"""

    db_conn = db_helper.create_db_connection()
    data = db_helper.fetch_data(db_conn, query)
    db_conn.close()
    return data
