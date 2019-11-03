x = [1, 2, 3, 4, 5, 6]
print(len(x))

a = x[:3]           #print less than 3
print (a)

a = x[3:]           #print more than 3
print (a)

a = x[-2:]          #print the last two
print (a)

x.extend([7,8])     #extend value of x
print (x)

x.append(20)        #add a value in the last
print (x)

y = [10, 11, 12]    #membuat koordinat x,y
listOfLists = [x, y]
print listOfLists

print y[0]          #array ke .....

z = [1, 5, 3, 2, 4] #sort number
z.sort()
print (z)
z.sort(reverse = True)
print(z)