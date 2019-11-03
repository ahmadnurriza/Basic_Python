#this is used for the real data so we can not modified the data (can't add or remove the data)

x = (1, 2, 3)
a = len (x)
print x
print a

y = (4, 5, 6)
print y[1]

listofTuples = [x, y]
print listofTuples

age,income = '20,30000'.split(',')
print age
print income