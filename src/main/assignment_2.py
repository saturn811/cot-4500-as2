import numpy as np
from scipy.linalg import solve
np.set_printoptions(precision=7, suppress=True, linewidth=100)


#QUESTION 1

def neville_method(x_points, y_points, x):
    x_points = [3.6, 3.8, 3.9]
    y_points = [1.675, 1.436, 1.318]

    matrix = np.zeros((3,3))

    for counter, row in enumerate(matrix):
        row[0] = y_points[counter]

    value = x
    num_of_points = len(x_points)
    for i in range(1,num_of_points):
            for j in range(1, i + 1):
                first_multiplication = (value - x_points[i-j]) * matrix[i][j-1]
                second_multiplication = (value - x_points[i]) * matrix[i-1][j-1]

                denominator = x_points[i] - x_points[i-j]

                coefficient = (first_multiplication - second_multiplication)/denominator

                matrix[i][j] = coefficient


        



    print(matrix[num_of_points - 1][num_of_points - 1])



if __name__ == "__main__": 
    x_points = []
    y_points = []
    approximating_value = 3.7

    neville_method(x_points, y_points, approximating_value)


#QUESTION 2

p1 = (25.3913-23.5492) / (7.4-7.2)
q1 = (26.8224-25.3913) / (7.5-7.4)
k1 = (27.4589-26.8224) / (7.6-7.5)

p2 = (q1-p1) / (7.5-7.2)
q2 = (k1-q1) / (7.6-7.4)

p3 = (q2-p2) / (7.6-7.2)
print([p1, p2, p3])


#QUESTION 3

p1x = 23.5492 + p1*(7.3-7.2)
p2x = p1x + p2*(7.3-7.4)*(7.3-7.2)
p3x = p2x + p3*(7.3-7.5)*(7.3-7.4)*(7.3-7.2)
print(p3x)


#QUSETION 4

a1 = 3.6
a2 = 3.6
a3 = 3.8
a4 = 3.8
a5 = 3.9
a6 = 3.9

b1 = 1.675
b2 = 1.675
b3 = 1.436
b4 = 1.436
b5 = 1.318
b6 = 1.318

c1 = 0 
c2 = -1.195
c3 = round((b3 - b2) / (a3 - a2), 7)
c4 = -1.188
c5 = round((b5-b4) / (a5-a4), 7)
c6 = -1.182

d1 = 0
d2 = 0
d3 = round((c3-c2) / (a3-a2), 7)
d4 = round((c4-c3) / (a4-a2), 7)
d5 = round((c5-c4) / (a5-a3), 7)
d6 = round((c6-c5) / (a6-a4), 7)

e1 = 0
e2 = 0
e3 = 0
e4 = round((d4-d3) / (a4-a1), 7)
e5 = round((d5-d4) / (a5-a2), 7)
e6 = round((d6-d5) / (a6-a3), 7)

f1 = 0 
f2 = 0
f3 = 0
f4 = 0
f5 = round((e5-e4) / (a5-a1), 7)
f6 = round((e6-e5) / (a6-a2), 7)

a = np.matrix([[a1,b1,c1,d1,e1,f1],[a2,b2,c2,d2,e2,f2],[a3,b3,c3,d3,e3,f3], [a4,b4,c4,d4,e4,f4], [a5,b5,c5,d5,e5,f5], [a6,b6,c6,d6,e6,f6]]) 
print(a)

#QUESTION 5
#Part A

x0 = 2
x1 = 5
x2 = 8
x3 = 10
y0 = 3
y1 = 5
y2 = 7
y3 = 9

h0 = x1-x0
h1=x2-x1
h2=x3-x2

t1=1
t2=0
t3=0
t4=0
t5=h0
t6=2*(h0+h1)
t7=h1
t8=0
t9=0
t10=h1
t11=2*(h1+h2)
t12=h2
t13=0
t14=0
t15=0
t16=1

z = np.matrix([[t1,t2,t3,t4],[t5,t6,t7,t8],[t9,t10,t11,t12], [t13,t14,t15,t16]])
print(z)

#Part B
r1=0
r2=((3/h1)*(y2-y1)) - ((3/h0)*(y1-y0))
r3=((3/h2)*(y3-y2)) - ((3/h1)*(y2-y1))
r4=0

r = np.array([r1,r2,r3,r4])

print(r)

#Part C
A = np.array([[t1,t2,t3,t4],[t5,t6,t7,t8],[t9,t10,t11,t12], [t13,t14,t15,t16]])
b = np.array([r1, r2, r3, r4])

x = solve(A,b)
print(x)

