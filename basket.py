import math

import matplotlib.pyplot as plt


displacement = {}
velocity = {}
xcalbs = {}


def path(x, y, v, g, r, q, k, dt, w, m):
    vx = v * math.cos(r)
    vy = v * math.sin(r)
    while y >= 0:
        ax = (-q*math.cos(r)*v**2-math.sin(r)*k*w*v)/m
        ay = -g + (-q*math.sin(r)*v**2+math.cos(r)*k*w*v)/m
        displacement[x] = y
        x += vx * dt
        y += vy * dt
        vx += ax * dt
        vy += ay * dt
        print(ax)
        if (vx != 0):
            r = math.atan(vy / vx)
            v = math.sqrt(vx * vx + vy * vy)
        else:
            v = vy
    global xf
    global vf
    global rf
    global yf
    xf = x
    vf = v
    rf = r

    # caliberation(x,y, dt)
def caliberation(x, y, dt):
    xp = list(displacement.keys())
    x_1 = xp[len(xp) - 2]
    y_1 = displacement.get(x_1)
    kc = (y_1 - y) / (x_1 - x)
    m = y - kc * x
    xcalib = -m / kc
    xcalbs[-1 * math.log(dt)] = xcalib

def konv():
    for i in range(1, 2):
        print(i)
        path(0, 0, 75, -9.82, math.radians(11), 0.0012, 0.011, 1 / (10 ** (i)), 2, 0.045)
m = 0.62
path(0, 140, 0, 9.82, math.radians(75), 0.00016, 0.02, 0.001, 5.5,m)
collisionEnergy = (m * (vf ** 2) /2)*0.5
while collisionEnergy>= 0.6:
    v = math.sqrt(collisionEnergy*2/m)
    path(xf, 0, v, 9.82, -1*rf, 0.009, 0.004, 0.001, 5.5, m)
    collisionEnergy = (m * (vf ** 2) / 2) * 0.92
plt.plot(displacement.keys(), displacement.values())
displacement.clear()
#plt.scatter(xcalbs.keys(), xcalbs.values())



plt.show()
