from math import pi
import numpy
from matplotlib import pyplot
from matplotlib import rcParams
rcParams['font.family'] = 'serif'
rcParams['font.size'] = 16

# rocket parameters
m_s = 50.0
g = 9.81
p = 1.091
r = 0.5
A = pi*r**2
v_e = 325
C_D = 0.15
m_p0 = 100

# initial conditions
h0 = 0
v0 = 0


def f(u):

    h = u[0]
    m_p = u[1]
    v = u[2]

    return numpy.array([v,
                        -m_p_dot,
                        -g + m_p_dot*v_e/(m_s + m_p) - p*v*abs(v)*A*C_D/(2*(m_s + m_p))])


def euler_step(u, f, dt):
    return u + dt*f(u)

T = 60
dt = 0.1
N = int(T/dt) + 1
t = numpy.linspace(0.0, T, N)

u = numpy.empty((N,3))
u[0] = numpy.array([h0, m_p0, v0])

for n in range(N-1):

    if n < 50:
        m_p_dot = 20
    else:
        m_p_dot = 0
        m_p = 0
        u[n,1] = 0

    while u[n,0] < 0:
        u[n,0] = 0
        u[n,2] = 0
        m_p_dot = 0

    # print(n, m_p_dot, u[n,0], u[n,1],u[n,2])
    u[n+1] = euler_step(u[n], f, dt)


h = u[:,0] # the altitude
v = u[:,2] # the velocity


# plot the altitude w.r.t time
pyplot.figure(figsize = (8,6))
pyplot.xlabel('t',fontsize=14)
pyplot.ylabel('h',fontsize=14)
pyplot.title('Rocket altitude, flight time = %.2f' % T, fontsize = 18)
pyplot.plot(t,h, 'k-')
pyplot.show()



# plot the velocity w.r.t time
pyplot.figure(figsize = (8,6))
pyplot.xlabel('t',fontsize=14)
pyplot.ylabel('v',fontsize=14)
pyplot.title('Rocket velocity, flight time = %.2f' % T, fontsize = 18)
pyplot.plot(t,v, 'k-')
pyplot.show()
