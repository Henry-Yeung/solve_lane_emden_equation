import numpy as np
import matplotlib.pyplot as plt

# Run for a loop so that we can plot a graph which contains six polytropic indices from n = 0 to n = 5
for n in range(6) :
    # Set up the initial condition
    theta = 1
    xi = 0.0000001
    delta_xi = 0.001
    initial_gradient = 0 # dtheta/dxi

    # Create and define the lists
    theta1  = [theta]
    xi1 = [xi]
    initial_gradient1 = [initial_gradient]

    # Set up the boundary conditions and use the equations to find the values of theta and xi\
    while  xi < 20 and theta > 0:

        b = - ( 2 / xi ) * initial_gradient - theta ** n    # b is secondary derivative (d2theta/dxi2)
        xi = xi + delta_xi                                  # calculate every value of xi so that we can plot the graph (while xi < 20)
        initial_gradient = initial_gradient + delta_xi * b  # initial_gradient is dtheta/dxi, calculate the value of dtheta/dxi
        theta = theta + delta_xi * initial_gradient         # calculate the set of values of theta\

        # Store the calculated value back into the lists
        theta1.append(theta)
        xi1.append(xi)
        initial_gradient1.append(initial_gradient)

        # Specify the condition when we use the equations below to do calculations and plot graphs\
    if theta < 0 :
        initial_gradient = initial_gradient + delta_xi * b  # restate it and make sure it is saved under a different condition
        xi2 = xi + delta_xi                                 # calculate the value of xi where x > 0 (called as xi2)
        xi3 = xi2 + delta_xi                                # calculate the value of xi where x < 0 (called as xi3)
        theta2 = theta + delta_xi * initial_gradient        # calculate the value of theta where x > 0 (called as theta2)
        theta3 = theta2 + delta_xi * initial_gradient       # calculate the value of theta where x < 0 (called as theta3)


        # Using the interpolation method to estimate the xi value which is called as ξ below
        def interpolation(x):          # define the function
            inter = ((-theta2*(xi3-xi2)) / (theta3-theta2)) + xi2  # put the equation for linear interpolation which was rearranged as xi (where x > 0) as the subject
            return inter          # return the function so that the data will be stored
        xi_r = interpolation(0)   # assign the equation to a name for calculating different values of xi accrodingly to different n

        # print out the xi values, polytropic indices (n), the values of dtheta/dxi (called as initial_gradient) from n=0 to n=4 (under the condition we set at the beginning of this cell)
        initial_gradient = initial_gradient + delta_xi * b
        print('The value of ξ is = {:.3f} when n = {} and the gradient is {}.'.format(xi_r, n, initial_gradient))



    # Plot the graph by using the value we just calculated above
    plt.plot(xi1,theta1, label='n=%s'%n)
    plt.xlabel('xi')
    plt.ylabel('Theta')
    plt.legend()
    plt.ylim(0.3,1.1)
    plt.xlim(0,5)  
plt.show()
