import os
import sqlite3
from sqlite3 import Error

DB_FILE = 'db.sqlite3'


def delete_db(db_file):
    if delete_db and os.path.exists(db_file):
        os.remove(db_file)
        return True
    return False


def create_db_connection(db_file=DB_FILE):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        conn.execute("PRAGMA foreign_keys = 1")
    except Error as e:
        print(e)
    return conn


def execute_db_command(conn, query):
    try:
        c = conn.cursor()
        c.execute(query)
    except Error as e:
        print(e)
        print("-- {0}".format(query))


def create_db_schema():
    authority = """CREATE TABLE IF NOT EXISTS Authority (
                        id INTEGER PRIMARY KEY NOT NULL,
                        title TEXT NOT NULL UNIQUE
                    );"""
    designation = """CREATE TABLE IF NOT EXISTS Designation (
                        id INTEGER PRIMARY KEY NOT NULL,
                        title TEXT NOT NULL UNIQUE
                    );"""
    department = """CREATE TABLE IF NOT EXISTS Department (
                        id INTEGER PRIMARY KEY NOT NULL,
                        title TEXT NOT NULL UNIQUE
                    );"""
    person = """CREATE TABLE IF NOT EXISTS Person (
                        id INTEGER PRIMARY KEY NOT NULL,
                        authority_id INTEGER,
                        designation_id INTEGER,
                        department_id INTEGER,
                        first_name TEXT,
                        last_name TEXT,
                        pay_type TEXT,
                        base_annualized_salary REAL,
                        actual_salary_paid REAL,
                        overtime_paid REAL,
                        performance_bonus REAL,
                        extra_pay REAL,
                        other_compensation REAL,
                        total_compensation REAL,
                        paid_by_another_entity INTEGER,
                        exempt_indicator INTEGER,
                        fiscal_year_end_date DATETIME,
                        
                        FOREIGN KEY (authority_id) REFERENCES authority (id),
                        FOREIGN KEY (designation_id) REFERENCES designation (id),
                        FOREIGN KEY (department_id) REFERENCES department (id)
                    );"""

    create_indexes = """CREATE INDEX IF NOT EXISTS idx_authority ON Authority (title);"""
    create_indexes += """CREATE INDEX IF NOT EXISTS idx_designation ON Designation (title);"""
    create_indexes += """CREATE INDEX IF NOT EXISTS idx_department ON Department (title);"""

    create_indexes += """CREATE INDEX IF NOT EXISTS idx_full_name ON Person (first_name, last_name);"""
    create_indexes += """CREATE INDEX IF NOT EXISTS idx_financials ON Person (base_annualized_salary, 
    actual_salary_paid, overtime_paid, performance_bonus, extra_pay, other_compensation, total_compensation);"""
    create_indexes += """CREATE INDEX IF NOT EXISTS idx_financials2 ON Person (pay_type, paid_by_another_entity, fiscal_year_end_date);"""

    conn = create_db_connection()
    execute_db_command(conn, authority)
    execute_db_command(conn, designation)
    execute_db_command(conn, department)
    execute_db_command(conn, person)

    for index_query in create_indexes.split(";"):
        execute_db_command(conn, '{0};'.format(index_query))

    conn.commit()
    return conn.close()


def fetch_data(conn, query):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    try:
        cur = conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        return rows
    except Error as e:
        print(e)
