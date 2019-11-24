import matplotlib.pyplot as plt

import analyze


def plot_department(limit=10):
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


def plot_designation(limit=10):
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
