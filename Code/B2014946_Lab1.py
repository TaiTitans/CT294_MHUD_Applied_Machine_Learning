a = 5
b = 3
if a > b:
    a=a*2+3
    b=b-6
    c=a/b
    print(c)

#Next

c=a+b+\
    10*a-b/4-\
    5+a*3
print(c)


#Next

a=5
b=3
if a>b:
    print("True")
    print(a)
else:
    print("False")
    print(b)

#Next
a=1
b=10
while a<b:
    a+=1
    print(a)

for i in range (1,10):
    print(a)

#Next
def binhphuong(number):
    return number*number
print(binhphuong(5))

#Next
cats = ['Tom', 'Snappy', 'Kitty', 'Jessie', 'Chester']

print (cats[2]) # in ra phần tử có chỉ số là 2

print (cats[-1]) # in ra phần tử cuối cùng của list

print (cats[1:3]) # in ra các phần tử có chỉ số từ 1 đến 3


#Next

dict1 = {'Name': 'Zyra', 'Age' : 7, 'Class': 'A5'}
print(dict['Name'])
print(dict['Age'])



dict = {'Name': 'Zara', 'Age': 7,'Class':'First'}
dict['Age'] = 8
dict['School'] = "DPS School"
print(dict['Age'])
print(dict['School'])