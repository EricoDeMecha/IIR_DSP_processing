import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pyfirmata
from IIRFilter import IIRFilter

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []
board = pyfirmata.ArduinoMega('/dev/ttyACM0')

print("Communication Success")

it = pyfirmata.util.Iterator(board)
it.start()

ldr = board.analog[0]
ldr.enable_reporting()
# Filter init
# Generating sos coefficients
'''
order: 2
cuttoff: [45,55]
filter type: 'bandstop'
design: cheby1
rp:0.01
rs: 1
fs: 200
'''
sos = [2, [45, 55], 'bandstop', 'cheby1', 0.01, 1, 200]

# 2. setup filters
IIRFilter(sos)  # filters are setup with coefficients


# This function is called periodically from FuncAnimation
def animate(i, xs, ys):
    # get the output of the sensor
    ldr_val = ldr.read()
    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(ldr_val * 260000)  # 130000 lux is the maximum light intensity in a green house.

    # Limit x and y lists to 20 items
    xs = xs[-20:]
    ys = ys[-20:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys, 'b')
    # apply filter
    # filter_ys = IIRFilter.filter(ldr_val)
    # ax.plot(xs, ys, 'r')  # plot the result
    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Digital UV light signal')
    plt.ylabel('Signal Strength (lux)')


# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=500)
plt.show()
