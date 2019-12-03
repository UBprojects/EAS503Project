import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import analyze

PLOT_FIGSIZE = (15, 10)
PLOT_ROTATION = 45


def plot_department_pay(limit=10):
    data = analyze.department_pays_most_and_least(limit=limit)
    x_axis, ymax_axis, ymin_axis = list(), list(), list()
    for d in data:
        x_axis.append(d[0])
        ymax_axis.append(d[1])
        ymin_axis.append(d[2])

    fig, ax1 = plt.subplots(figsize=PLOT_FIGSIZE)
    plt.xticks(rotation=PLOT_ROTATION)
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
        x_axis.append(d[0].title())
        ymax_axis.append(d[1])
        ymin_axis.append(d[2])

    n_groups = len(x_axis)
    plt.subplots(figsize=PLOT_FIGSIZE)
    plt.xticks(rotation=PLOT_ROTATION)
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.8

    plt.bar(index, ymax_axis, bar_width,
            alpha=opacity,
            color='g',
            label='Max. Amount ($)')

    plt.bar(index + bar_width, ymin_axis, bar_width,
            alpha=opacity,
            color='b',
            label='Min. Amount ($)')

    plt.xlabel('Designations')
    plt.ylabel('Salary amount')
    plt.title('Designations salary - Most & Least')
    plt.xticks(index + bar_width, x_axis)
    plt.legend()

    plt.tight_layout()
    plt.show()


def plot_authority_pay(limit=10):
    data = analyze.authority_pays_most_and_least(limit=limit)
    x_axis, ymax_axis, ymin_axis = list(), list(), list()
    for d in data:
        x_axis.append(d[0].title())
        ymax_axis.append(d[1])
        ymin_axis.append(d[2])

    n_groups = len(x_axis)
    plt.subplots(figsize=PLOT_FIGSIZE)
    plt.xticks(rotation=PLOT_ROTATION)
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.8

    plt.bar(index, ymax_axis, bar_width,
            alpha=opacity,
            color='g',
            label='Max. Amount ($)')

    plt.bar(index + bar_width, ymin_axis, bar_width,
            alpha=opacity,
            color='b',
            label='Min. Amount ($)')

    plt.xlabel('Authorities')
    plt.ylabel('Salary amount')
    plt.title('Authorities salary - Most & Least')
    plt.xticks(index + bar_width, x_axis)
    plt.legend()

    plt.tight_layout()
    plt.show()


def plot_department_public_private_pay(limit=10):
    data = analyze.department_pays_private_or_public(limit=limit)
    x_axis, ymax_axis, ymin_axis = list(), list(), list()
    for d in data:
        x_axis.append(d[0])
        ymax_axis.append(d[1] if d[1] else 0)
        ymin_axis.append(d[2] if d[2] else 0)

    fig, ax1 = plt.subplots(figsize=PLOT_FIGSIZE)
    plt.xticks(rotation=PLOT_ROTATION)
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
    plt.subplots(figsize=PLOT_FIGSIZE)
    plt.xticks(rotation=PLOT_ROTATION)
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


def plot_authority_avg_salary(limit=10):
    data = analyze.authority_avg_salary(limit=limit)

    x_axis, y_axis = list(), list()
    for d in data:
        x_axis.append(d[0])
        y_axis.append(d[1] if d[1] else 0)

    n_groups = len(x_axis)
    plt.subplots(figsize=PLOT_FIGSIZE)
    plt.xticks(rotation=PLOT_ROTATION)
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.8

    plt.bar(index, y_axis, bar_width,
            alpha=opacity,
            color='r',
            label='Average Salary')

    plt.xlabel('Authorities')
    plt.ylabel('Salary amount')
    plt.title('Average salary for authorities')
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
    plt.subplots(figsize=PLOT_FIGSIZE)
    plt.xticks(rotation=PLOT_ROTATION)
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

    x_axis, y_axis_2016, y_axis_2017, y_axis_2018 = list(), list(), list(), list()
    for d in data:
        x_axis.append(d[0])
        y_axis_2016.append(d[1] if d[1] else 0)
        y_axis_2017.append(d[2] if d[2] else 0)
        y_axis_2018.append(d[3] if d[3] else 0)

    n_groups = len(x_axis)
    plt.subplots(figsize=PLOT_FIGSIZE)
    plt.xticks(rotation=PLOT_ROTATION)
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.8

    plt.bar(index, y_axis_2016, bar_width,
            alpha=opacity,
            color='b',
            label='2016')

    plt.bar(index + bar_width, y_axis_2017, bar_width,
            alpha=opacity,
            color='g',
            label='2017')

    plt.bar(index + (bar_width * 2), y_axis_2018, bar_width,
            alpha=opacity,
            color='r',
            label='2018')

    plt.xlabel('Year')
    plt.ylabel('# of employees')
    plt.title('# of employees in department for past 3 years')
    plt.xticks(index + bar_width, x_axis)
    plt.legend()

    plt.tight_layout()
    plt.show()


def plot_authority_employee_count_over_years(limit=10):
    data = analyze.authority_employee_count_over_years(limit=limit)

    x_axis, y_axis_2016, y_axis_2017, y_axis_2018 = list(), list(), list(), list()
    for d in data:
        x_axis.append(d[0])
        y_axis_2016.append(d[1] if d[1] else 0)
        y_axis_2017.append(d[2] if d[2] else 0)
        y_axis_2018.append(d[3] if d[3] else 0)

    n_groups = len(x_axis)
    plt.subplots(figsize=PLOT_FIGSIZE)
    plt.xticks(rotation=PLOT_ROTATION)
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.8

    plt.bar(index, y_axis_2016, bar_width,
            alpha=opacity,
            color='b',
            label='2016')

    plt.bar(index + bar_width, y_axis_2017, bar_width,
            alpha=opacity,
            color='g',
            label='2017')

    plt.bar(index + (bar_width * 2), y_axis_2018, bar_width,
            alpha=opacity,
            color='r',
            label='2018')

    plt.xlabel('Year')
    plt.ylabel('# of employees')
    plt.title('# of employees in authorities for past 3 years')
    plt.xticks(index + bar_width, x_axis)
    plt.legend()

    plt.tight_layout()
    plt.show()


def plot_department_avg_salary_trend(limit=10):
    data = analyze.department_avg_salary_trend(limit=limit)

    data_dict = {'x': [i for i in range(2011, 2018 + 1)]}
    for d in data:
        data_dict.update({d[0]: [d[i] for i in range(1, len(d))]})

    # Make a data frame
    df = pd.DataFrame(data_dict)

    # Figure size and rotation
    plt.figure(figsize=PLOT_FIGSIZE)
    plt.xticks(rotation=PLOT_ROTATION)

    # style
    plt.style.use('seaborn-darkgrid')

    # create a color palette
    palette = plt.get_cmap('Set1')

    # multiple line plot
    num = 0
    for column in df.drop('x', axis=1):
        num += 1
        plt.plot(df['x'], df[column], marker='', color=palette(num), linewidth=2, alpha=0.9, label=column)

    # Add legend
    plt.legend(loc=2, ncol=2)

    # Add titles
    plt.title("Department average salary over the years", loc='left', fontsize=12, fontweight=0, color='orange')
    plt.xlabel("Year")
    plt.ylabel("Average salary")


def plot_department_employees_pie_chart(limit=10):
    data = analyze.department_num_employees(limit=limit)

    x_axis, y_axis = list(), list()
    for d in data:
        x_axis.append(d[0])
        y_axis.append(d[1] if d[1] else 0)

    # Pie chart
    fig1, ax1 = plt.subplots(figsize=PLOT_FIGSIZE)
    ax1.pie(y_axis, labels=x_axis, autopct='%1.1f%%', shadow=True, startangle=90)

    # Equal aspect ratio ensures that pie is drawn as a circle
    ax1.axis('equal')
    plt.tight_layout()
    plt.show()


def plot_designation_employees_pie_chart(limit=10):
    data = analyze.designation_num_employees(limit=limit)

    x_axis, y_axis = list(), list()
    for d in data:
        x_axis.append(d[0])
        y_axis.append(d[1] if d[1] else 0)

    # Pie chart
    fig1, ax1 = plt.subplots(figsize=PLOT_FIGSIZE)
    ax1.pie(y_axis, labels=x_axis, autopct='%1.1f%%', shadow=True, startangle=90)

    # Equal aspect ratio ensures that pie is drawn as a circle
    ax1.axis('equal')
    plt.tight_layout()
    plt.show()
