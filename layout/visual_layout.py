import numpy as np
import pygame
import matplotlib.pyplot as plt
from math import pi

board = np.zeros((3, 3))

pygame.init()
pygame.display.init()


pygame.init()
pygame.display.init()

pygame.display.set_caption('flick flack flow')
window_surface = pygame.display.set_mode((370, 370))

background = pygame.Surface((370, 370))
background.fill(pygame.Color('#D39385'))

myfont = pygame.font.SysFont('Courier New', 30)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()
    window_surface.blit(background, (0, 0))
    pygame.display.update()


get_ipython().run_line_magic('matplotlib', 'inline')
plt.style.use('seaborn-whitegrid')

fig, ax = plt.subplots(2, 2)

plt.plot(x, np.sin(x), color='#D39385', linestyle='dashed')
plt.plot(x, np.cos(x), ':c')

ax = plt.axes()
ax.plot(x, np.sin(x))
ax.plot(x, np.cos(x))

ax.set(xlim=(0, 3*pi), ylim=(-2, 2),
       xlabel='x', ylabel='sin(x)',
       title='trig stuff')


"""ax.set( xlim=(0, 4* pi), ylim=(-1, 1),
       xlabel='x in radians', ylabel='sin(x), cos(x)',
       title = 'sin(x) & cos(x)')"""

plt.xticks(np.arange(0, 4 * pi, pi/2))
plt.yticks(np.arange(-1.5, 2.0, 0.5))


# Plot bifurcation of time-iterated dynamics for logistic function with y=x
def plot_bifur(r, x0, n, ax=None):
    t = np.linspace(0, 1)
    ax.plot(t, logistic(r, t), 'k', lw=2)
    ax.plot([0, 1], [0, 1], 'k', lw=2)

    # Iterate the function:
    # Recursively apply y=f(x) and plot two lines,
    # (x, x) -> (x, y)
    # (x, y) -> (y, y)
    x = x0
    for i in range(n):
        y = logistic(r, x)
        ax.plot([x, x], [x, y], 'k', lw=1)
        ax.plot([x, y], [y, y], 'k', lw=1)
        # Each iteration increases opacity
        ax.plot([x], [y], 'ok', ms=10,
                alpha=(i + 1) / n)
        x = y

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title(f"$r={r:.1f}, \, x_0={x0:.1f}$")


fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, figsize=(5, 10), sharex=True, sharey=True)
plot_bifur(2.5, .1, 10, ax=ax1)
plot_bifur(2.9, .1, 10, ax=ax2)
plot_bifur(3.5, .1, 10, ax=ax3)
plot_bifur(3.9, .1, 10, ax=ax4)


get_ipython().run_line_magic('matplotlib', 'inline')


# Plot logistic function f(x)
def logistic(r, x):
    return (r * x * (1-x))


x = np.linspace(0, 1)
fig, ax = plt.subplots(1, 1)
ax.plot(x, logistic(2, x), 'k')
