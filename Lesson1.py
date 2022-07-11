#Date : 14th April 2022

# Assignment of values

a = 100
b = 200

#Equality
print(1 == 1)
print(a == b)

#Data types
#integer:1,2,3,4,5,6


#Type casting
a = 1.2345
type(a)
<class 'float'>
type(int(a))
<class 'int'>

#Data type
#1.list
a = [1, 2, 3, 4]
type(a)
<class 'list'>

#2. Str
a = "This is a str"
type(a)
<class 'str'>

#Dictionary
c = {"male": ["tom", "jerry", "jeff"]}
type (c)
<class 'dict'>
import pprint
d = {"Male": ["Kiran", "Jeff", "Tommy", "clavin", "klein"], "female": ["Mary", "Jane", "Woman", "Ah girl"],
     "Non-binary": ["No name", "bu zhi dao", "Anyhow"]}
d
{'Male': ['Kiran', 'Jeff', 'Tommy', 'clavin', 'klein'], 'female': ['Mary', 'Jane', 'Woman', 'Ah girl'],
 'Non-binary': ['No name', 'bu zhi dao', 'Anyhow']}
pprint.pprint(d)
{'Male': ['Kiran', 'Jeff', 'Tommy', 'clavin', 'klein'],
 'Non-binary': ['No name', 'bu zhi dao', 'Anyhow'],
 'female': ['Mary', 'Jane', 'Woman', 'Ah girl']}

for key, value in d.items():
    print("key is {},value is {}".format(key, value))
key is Male, value is ['Kiran', 'Jeff', 'Tommy', 'clavin', 'klein']
key is female, value is ['Mary', 'Jane', 'Woman', 'Ah girl']
key is Non - binary, value is ['No name', 'bu zhi dao', 'Anyhow']

for key, value in d.items():
    print("key is {}, type of value is {}".format(key, type(value)))

key is Male, type of value is <class 'list'>key is female, type of value is <class 'list'> key is Non - binary, type
of value is <class 'list'>

#Function
def addition(a,b):
    return  a+b
ans = addition(100,2093)
ans
2193

def subtraction(a,b,c):
    return a-b+c
ans = subtraction(100,1000,200)
ans
-700

def multiply(a,b):
    return int(float(a))*int(float(b))

#lesson 2
#else if
def grader(a):
    if a > 100:
        return "Please enter a value less than or equal to 100"
    if a < 0:
        return "Please enter a value more than or equal to 0"
    if a>=75:
        return "A1"
    elif a<75 and a>= 70:
        return "A2"
    elif a<70 and a>=65:
        return "B3"
    elif a<65 and a>=60:
        return "B4"
    elif a<60 and a>=55:
        return "C5"
    elif a<55 and a>=50:
        return "C6"
    else:
        return "FAIL"

    grader(-0.5)
    'Please enter a value more than or equal to 0'
    grader(50)
    'C6'
    grader(25)
    'FAIL'
    grader(75)
    'A1'