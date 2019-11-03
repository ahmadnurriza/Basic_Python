# tensor addition
from numpy import array
from numpy import tensordot

A = array([
  [[1,2,3],    [4,5,6],    [7,8,9]],
  [[11,12,13], [14,15,16], [17,18,19]],
  [[21,22,23], [24,25,26], [27,28,29]],
  ])
B = array([
  [[1,2,3],    [4,5,6],    [7,8,9]],
  [[11,12,13], [14,15,16], [17,18,19]],
  [[21,22,23], [24,25,26], [27,28,29]],
  ])

C = A+B     #Addition
D = A-B     #Substraction
E = A*B     #Hadamart Product
F = A/B     #Division

G = array([
    [[1,2,3], [4,5,6], [7,8,9]],
    [[1,2,3], [4,5,6], [7,8,9]],
    [[1,2,3], [4,5,6], [7,8,9]],
    ])

H = tensordot(A, B, Axes=0)
print G