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
        x += vx * dt
        y += vy * dt
        displacement[x] = y
        vx += ax * dt
        vy += ay * dt
        r = math.atan(vy / vx)
        v = math.sqrt(vx * vx + vy * vy)
    global xf
    global vf
    global rf
    global yf
    xf = x
    vf = v
    rf = r
    caliberation(x,y, dt)
def caliberation(x, y, dt):
    xp = list(displacement.keys())
    x_1 = xp[len(xp) - 2]
    y_1 = displacement.get(x_1)
    kc = (y_1 - y) / (x_1 - x)
    m = y - kc * x
    xcalib = -m / kc
    xcalbs[-1 * math.log(dt)] = xcalib
def konv():
    for i in range(1, 7):
        print(i)
        path(0, 0, 75, 9.82, math.radians(11), 0.0012, 0.011, 1 / (10 ** (i)), 1, 0.045)
    plt.scatter(xcalbs.keys(), xcalbs.values())
def collision(energy, m, k):
    path(0, 0, 80, 9.82, math.radians(13), 0.0011, k, 0.001, 1,m)
    collisionEnergy = (m * (vf ** 2) /2)*0.9
    while collisionEnergy>= energy:
        v = math.sqrt(collisionEnergy*2/m)
        path(xf, 0, v, 9.82, -1*rf, 0.0011, k, 0.001, 1, m)
        collisionEnergy = (m * (vf ** 2)/ 2)*0.25
    plt.plot(displacement.keys(), displacement.values())
    displacement.clear()

#plt.scatter(xcalbs.keys(), xcalbs.values())
konv()
plt.gca().set_aspect('equal', adjustable='box')

plt.show()
