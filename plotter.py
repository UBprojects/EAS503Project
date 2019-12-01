import matplotlib.pyplot as plt
import numpy as np

import analyze


def plot_department_pay(limit=10):
    data = analyze.department_pays_most_and_least(limit=limit)
    x_axis, ymax_axis, ymin_axis = list(), list(), list()
    for d in data:
        x_axis.append(d[0])
        ymax_axis.append(d[1])
        ymin_axis.append(d[2])

    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    # plotting the points
    ax1.plot(x_axis, ymax_axis, 'g-')
    ax2.plot(x_axis, ymin_axis, 'b-')

    # naming the x axis
    ax1.set_xlabel('Departments')
    ax1.set_ylabel('Max. Amount ($)', color='g')
    ax2.set_ylabel('Min. Amount ($)', color='b')

    # giving a title to my graph
    plt.title('Department Pay - Most & Least')

    # function to show the plot
    plt.show()


def plot_designation_pay(limit=10):
    data = analyze.designation_pays_most_and_least(limit=limit)
    x_axis, ymax_axis, ymin_axis = list(), list(), list()
    for d in data:
        x_axis.append(d[0])
        ymax_axis.append(d[1])
        ymin_axis.append(d[2])

    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    # plotting the points
    ax1.plot(x_axis, ymax_axis, 'g-')
    ax2.plot(x_axis, ymin_axis, 'b-')

    # naming the x axis
    ax1.set_xlabel('Designations')
    ax1.set_ylabel('Max. Amount ($)', color='g')
    ax2.set_ylabel('Min. Amount ($)', color='b')

    # giving a title to my graph
    plt.title('Designation Pay - Most & Least')

    # function to show the plot
    plt.show()


def plot_department_public_private_pay(limit=10):
    data = analyze.department_pays_private_or_public(limit=limit)
    x_axis, ymax_axis, ymin_axis = list(), list(), list()
    for d in data:
        x_axis.append(d[0])
        ymax_axis.append(d[1] if d[1] else 0)
        ymin_axis.append(d[2] if d[2] else 0)

    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    # plotting the points
    ax1.plot(x_axis, ymax_axis, 'g-')
    ax2.plot(x_axis, ymin_axis, 'b-')

    # naming the x axis
    ax1.set_xlabel('Department salary - Private or Public')
    ax1.set_ylabel('Private salary', color='g')
    ax2.set_ylabel('Public salary', color='b')

    # giving a title to my graph
    plt.title('Department salary - Private or Public')

    # function to show the plot
    plt.show()


def plot_department_part_full_time(limit=10):
    data = analyze.department_employees_full_part_time(limit=limit)

    x_axis, ymax_axis, ymin_axis = list(), list(), list()
    for d in data:
        x_axis.append(d[0])
        ymax_axis.append(d[1] if d[1] else 0)
        ymin_axis.append(d[2] if d[2] else 0)

    n_groups = len(x_axis)
    plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.8

    plt.bar(index, ymax_axis, bar_width,
            alpha=opacity,
            color='b',
            label='Full-time')

    plt.bar(index + bar_width, ymin_axis, bar_width,
            alpha=opacity,
            color='g',
            label='Part-time')

    plt.xlabel('Departments')
    plt.ylabel('# of employees')
    plt.title('FT or PT employees in each department')
    plt.xticks(index + bar_width, x_axis)
    plt.legend()

    plt.tight_layout()
    plt.show()


def plot_designation_avg_salary(limit=10):
    data = analyze.designation_avg_salary(limit=limit)

    x_axis, y_axis = list(), list()
    for d in data:
        x_axis.append(d[0])
        y_axis.append(d[1] if d[1] else 0)

    n_groups = len(x_axis)
    plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.8

    plt.bar(index, y_axis, bar_width,
            alpha=opacity,
            color='r',
            label='Average Salary')

    plt.xlabel('Designations')
    plt.ylabel('Salary amount')
    plt.title('Average salary for designations')
    plt.xticks(index + bar_width, x_axis)
    plt.legend()

    plt.tight_layout()
    plt.show()


def plot_department_avg_salary(limit=10):
    data = analyze.department_avg_salary(limit=limit)

    x_axis, y_axis = list(), list()
    for d in data:
        x_axis.append(d[0])
        y_axis.append(d[1] if d[1] else 0)

    n_groups = len(x_axis)
    plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.8

    plt.bar(index, y_axis, bar_width,
            alpha=opacity,
            color='r',
            label='Average Salary')

    plt.xlabel('Departments')
    plt.ylabel('Salary amount')
    plt.title('Average salary for departments')
    plt.xticks(index + bar_width, x_axis)
    plt.legend()

    plt.tight_layout()
    plt.show()


def plot_department_employee_count_over_years(limit=10):
    data = analyze.department_employee_count_over_years(limit=limit)

    x_axis, ymax_axis, ymin_axis = list(), list(), list()
    for d in data:
        x_axis.append(d[0])
        ymax_axis.append(d[1] if d[1] else 0)
        ymin_axis.append(d[2] if d[2] else 0)

    n_groups = len(x_axis)
    plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.8

    plt.bar(index, ymax_axis, bar_width,
            alpha=opacity,
            color='b',
            label='2017')

    plt.bar(index + bar_width, ymin_axis, bar_width,
            alpha=opacity,
            color='g',
            label='2018')

    plt.xlabel('Year')
    plt.ylabel('# of employees')
    plt.title('# of employees in department over the years')
    plt.xticks(index + bar_width, x_axis)
    plt.legend()

    plt.tight_layout()
    plt.show()
