from datetime import date


x = 1         # assign variable x the value 1
y = True
z = 'hello' 
print(type(x)) # outputs: <class 'bool'>       # assign variable z the value of y

print(x, y, z)

name = input('Enter your name:')
name = input()
print('Hello...............',name)

# calculator basics
first_number = int(input('Type the first number: '));
second_number = int(input('Type the second number: '));
print("The sum is: ", first_number + second_number)


print(date.today())

# unit convertor
parsecs = 11;
lightyears = parsecs * 3.26;
print(str(parsecs) + ' parsecs is '+ str(lightyears) + ' light-years')