# Write a program that will iteratively predict and correct
# based on the distance and speed measurements and
# given initial state and acceleration in 4D

import numpy as np
from numpy.linalg import inv

# Mean and standard deviation of initial state in x-direction
x_mu = 4000      # distance
xv_mu = 280      # speed
x_sig = 10.0     # uncetainty in distance
xv_sig = 10.0    # uncertainty in speed

# Mean and standard deviation of initial state in y-direction
y_mu = 3000      # distance
yv_mu = 180      # speed
y_sig = 10.0     # uncetainty in distance
yv_sig = 10.0    # uncertainty in speed

# measurements and uncertainties in measuring in x-direction
x_obses = np.array([4260, 4550, 4860, 5110])  # distances
xv_obses = np.array([282, 285, 286, 290])     # speeds

# measurements and uncertainties in measuring in y-direction
y_obses = np.array([3181, 3366, 3552, 3742])  # distances
yv_obses = np.array([184, 186, 190, 194])     # speeds

obs_x_sig = 25  # uncetainty in distance measuring in x-direction
obs_xv_sig = 6  # uncertainty in speed measuring in x-direction
obs_y_sig = 25  # uncetainty in distance measuring in y-direction
obs_yv_sig = 6  # uncertainty in speed measuring in y-direction

dt = 1.0        # time interval to update
acx = 2.0       # Acceleration in x-direction
acy = 3.0       # Acceleration in y-direction

p_x_sig = 20.0  # uncetainty in prediting distance in x-direction
p_xv_sig = 5    # uncertainty in predicting speed in x-direction
p_y_sig = 20.0  # uncetainty in prediting distance in y-direction
p_yv_sig = 5    # uncertainty in predicting speed in y-direction


# Do not delete this comment!
# Do not add or change any code above

# Enter your code below to provide
# (1) initial state: X and covariance matrix: COV 
X = np.array([[x_mu], [y_mu], [xv_mu], [yv_mu]])
COV = np.diag([x_sig**2, y_sig**2, xv_sig**2, yv_sig**2])

# (2) Matrixes: A, B, C, u_t
A = np.array([[1, 0, dt, 0], [0, 1, 0, dt], [0, 0, 1, 0], [0, 0, 0, 1]])
B = np.array([[0.5*dt**2, 0], [0, 0.5*dt**2], [dt, 0], [0, dt]])
C = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
u_t = np.array([[acx], [acy]])

# (3) Covariance matrix in predicting: R_t
R_t = np.diag([p_x_sig**2, p_y_sig**2, p_xv_sig**2, p_yv_sig**2])

# (4) Covariance matrix in measuring: Q_t
Q_t = np.diag([obs_x_sig**2, obs_y_sig**2, obs_xv_sig**2, obs_yv_sig**2])


# Do not add or change any code below
def predict4D(X, COV):
    X_bar = A.dot(X) + B.dot(u_t)
    COV_bar = A.dot(COV).dot(A.T) + R_t
    return X_bar, COV_bar

def correct4D(X_bar, COV_bar, z_t):
    S = C.dot(COV_bar).dot(C.T)+Q_t
    K_t = COV_bar.dot(C.T).dot(inv(S))
    X = X_bar + K_t.dot((z_t - C.dot(X_bar)))
    COV = (np.identity(4) - K_t.dot(C)).dot(COV_bar)
    return X, COV

for i in range(len(x_obses)):
    X_bar, COV_bar = predict4D(X, COV)
    z_t = np.array([[x_obses[i]], [y_obses[i]], [xv_obses[i]], [yv_obses[i]]])
    X, COV = correct4D(X_bar, COV_bar, z_t)

print (X)
print (COV)


