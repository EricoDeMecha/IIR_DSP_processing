import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pyfirmata

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


# This function is called periodically from FuncAnimation
def animate(i, xs, ys):
    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(ldr.read()*260000) # 130000 lux is the maximum light intensity in a green house.

    # Limit x and y lists to 20 items
    xs = xs[-20:]
    ys = ys[-20:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys, 'b')
    # apply filter
    # 1. Generating sos coefficients
    sos =
    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Digital UV light signal')
    plt.ylabel('Signal Strength (lux)')


# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=500)
plt.show()
