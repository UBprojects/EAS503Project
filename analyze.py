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


def designation_pays_most_and_least(limit=10):
    query = """SELECT
                    d.title AS max_designation,
                    MAX(base_annualized_salary) AS max_pay,
                    MIN(base_annualized_salary) AS min_pay
                FROM
                    Person p
                    JOIN Designation d ON d.id = p.designation_id
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
                    JOIN Designation d ON d.id = p.department_id
                GROUP BY
                    d.title
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
                    avg_salary DESC
                LIMIT {limit};""".format(limit=limit)

    db_conn = db_helper.create_db_connection()
    data = db_helper.fetch_data(db_conn, query)
    db_conn.close()
    return data


def department_employee_count_over_years(limit=10):
    query = """SELECT
                    d.title, 
                    sum(case when strftime('%Y', fiscal_year_end_date) = '2017' then 1 else 0 end) as year_2017,
                    sum(case when strftime('%Y', fiscal_year_end_date) = '2018' then 1 else 0 end) as year_2018
                FROM
                    Person p
                    JOIN Department d ON d.id = p.department_id
                GROUP BY
                    d.title
                ORDER BY
                    year_2017 DESC, year_2018 DESC
                LIMIT {limit};""".format(limit=limit)

    db_conn = db_helper.create_db_connection()
    data = db_helper.fetch_data(db_conn, query)
    db_conn.close()
    return data
