import numpy as np

L = 11
rho_max = 250
nx = 51
dt = .001
dx = L/(nx - 1)


########  part_a  ########
V_max = 80

# Define the function for part a
def fa(t):
	t = t/60  # minutes to hours
	nt = t/dt
	 # initial condition
	x = np.linspace(0, L, nx)
	rho0 = np.ones(nx)*10
	rho0[10:20] = 50

	for n in range(int(nt)):
		rhon = rho0.copy()
		rho0[0] = 10 # Boundary condition
		rho0[1:] = rhon[1:] - V_max*(1 - 
			rhon[1:]/rho_max)*dt/dx*(rhon[1:] - rhon[0:-1])

	return rho0 


# question 1
rho0 = fa(0)
V_min = V_max*(1 - np.max(rho0)/rho_max)
print(V_min/3.6) # convert km/hr to m/s 


# question 2
rho0 = fa(3)
V = V_max*(1 - np.mean(rho0)/rho_max)
print(V/3.6)

# question 3 
rho0 = fa(6)
V_min = V_max*(1 - np.max(rho0)/rho_max)
print(V_min/3.6)


########  part_b  ########
V_max = 136

# Define the function for part b
def fb(t):
	t = t/60  # minutes to hours
	nt = t/dt
	 # initial condition
	x = np.linspace(0, L, nx)
	rho0 = np.ones(nx)*20
	rho0[10:20] = 50

	for n in range(int(nt)):
		rhon = rho0.copy()
		rho0[0] = 20 # Boundary condition
		rho0[1:] = rhon[1:] - V_max*(1 - 
			rhon[1:]/rho_max)*dt/dx*(rhon[1:] - rhon[0:-1])

	return rho0 

# question 4
rho0 = fb(0)
V_min = V_max*(1 - np.max(rho0)/rho_max)
print(V_min/3.6) # convert km/hr to m/s 


# question 5
rho0 = fb(3)
V = V_max*(1 - np.mean(rho0)/rho_max)
print(V/3.6)

# question 6 
rho0 = fb(3)
V_min = V_max*(1 - np.max(rho0)/rho_max)
print(V_min/3.6)
