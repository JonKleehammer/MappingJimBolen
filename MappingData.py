from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plot
import numpy as np

# setting up the figure
figure = plot.figure()
ax = figure.add_subplot(111, projection='3d')


# map_data called from the test_simulator when the data is finished
def map_data(data):

    # raw data is the data input
    raw_data_size = len(data)
    # processed data is going to include scores and frequency
    processed_data = dict()

    # actually processing the data
    for i in range(0, raw_data_size):
        key = data[i]
        if key in processed_data:
            processed_data[key] += 1
        else:
            processed_data[key] = 1

    x_data = []
    y_data = []
    z_data = []

    processed_data_size = len(processed_data)

    for key in processed_data:
        x_data.append(key[0])
        y_data.append(key[1])
        z_data.append(processed_data[key])

    xpos = x_data

    ypos = y_data

    zpos = np.zeros(processed_data_size)

    dx = np.ones(processed_data_size)
    dy = np.ones(processed_data_size) * 2.5
    dz = z_data

    ax.set_xlabel('Guesses')
    ax.set_ylabel('Scores')
    ax.set_zlabel('Frequency')

    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='#00ceaa')
    plot.show()

    print 'done'