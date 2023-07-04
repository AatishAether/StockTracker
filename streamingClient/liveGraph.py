import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import sys
from config import mydb

style.use('fast')
ticker = sys.argv[1]

fig = plt.figure()
plt.title(ticker)
plt.grid(False)
plt.xlabel("Time")
plt.ylabel("Price")

ax1 = fig.add_subplot(1,1,1)
def animate(i):
    graph_data = mydb[ticker].find()
    xs = []
    ys = []
    for candle in graph_data:
        try:
            xs.append(candle['datetime'].split(' ')[1])
        except:
            xs.append(candle['datetime'])
        finally:
            ys.append(candle['close'])
    
    ax1.clear()
    ax1.plot(xs,ys)

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()