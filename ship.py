import pygame as pg

#simulator of vertical ship motion: function file
disp = 20714.  #displaced water volume (assumed from literature)
A = 3200.       #water-line are (assumed from literature)
rho = 1025.  #density of sea water
g = 9.80665  #gravity
dt = 0.002      #time-step (chosen such that the numerical solution of the differential equation remains stable)

def rk4(position,speed):  #function to compute the solution of an ordinary differential equation using Runge-Kutta 4 Method
    #the inputs to the function (position and speed) are the states of the system
    ODE_update = lambda position,speed:[speed,-(g*A/disp)*position-g]  #intermediate update formula based on dynamics of system

    k1 = ODE_update(position,speed)      #constants needed by the method
    k2 = ODE_update(position + dt*k1[0]/2.,speed +dt*k1[1]/2.)  #constants needed by the method
    k3 = ODE_update(position+dt*k2[0]/2,speed+dt*k2[1]/2)   #constants needed by the method
    k4 = ODE_update(position+dt*k3[0],speed+dt*k3[1])   #constants needed by the method
    #NOTE: all k's are lists: this is because the ODE_update lambda function returns a list of two elements
    sum_of_ks_for_position = dt*k1[0]+2*dt*k2[0]+2*dt*k3[0]+dt*k4[0]    #constants needed by the method
    sum_of_ks_for_speed = dt*k1[1]+2*dt*k2[1]+2*dt*k3[1]+dt*k4[1]   #constants needed by the method

    return [position + sum_of_ks_for_position/6, speed + sum_of_ks_for_speed/6]     #the function returns the state at the next instant


state_list = [[-2.,0.]]  #list of lists: every sublist contains the states at a different instant, the numbers in the list represent the initial state

for step in range(10000):   #calculating states for 10000 times
    updated_state = rk4(state_list[-1][0],state_list[-1][1])
    state_list.append(updated_state)

position = [sub_list[0] for sub_list in state_list]         #getting just the first element in each list: position

pg.init()   #pygame function: initiation
colour = (50, 200, 255)     #color in RGB numbers made in a tuple
reso = 800, 500             #resolution of screen: made in a tuple
window = pg.display.set_mode(reso)          #creating the window

ship = pg.image.load('ship.png.png')        #loading the image of the ship

running = True

#animation loop
while running:
    
    for state in range(len(state_list)):                            #going through all computed states
        window.fill(colour)                                         #filling window with background color
        pg.draw.line(window, (10,20,25), (0, 300), (800, 300))      #drawing a line (supposed to be the waterline)
        window.blit(ship,(350,200+4*position[state]))               #sending the picture of the ship to the screen

        pg.display.flip()                                           #sending everything to the screen

pg.quit()                                                           #exiting animation