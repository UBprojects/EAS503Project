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
