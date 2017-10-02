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


def f(u, t):

    h = u[0]
    v = u[1]

    return numpy.array([v,
                        -g + m_p_dot(t)*v_e/(m_s + m_p(t)) - p*v*abs(v)*A*C_D/(2*(m_s + m_p(t)))])


def euler_step(u, f, t, dt):
    return u + dt*f(u, t)


def m_p(t):
    """ return the remaining weight of propellant at time t """
    return max(m_p0 - 20*t, 0)

def m_p_dot(t):
    """ return the burning rate at time t """
    return 20 if (t < 5) else 0


T = 60
dt = 0.1
N = int(T/dt) + 1
t = numpy.linspace(0.0, T, N)

u = numpy.empty((N,2))
u[0] = numpy.array([h0, v0])

for n in range(N-1):

    while u[n,0] < 0:
        u[n,0] = 0
        u[n,1] = 0

    # print(n, m_p(n/10), m_p_dot(n/10), u[n,0], u[n,1])
    u[n+1] = euler_step(u[n], f, t[n], dt)


h = u[:,0] # the altitude
v = u[:,1] # the velocity


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
