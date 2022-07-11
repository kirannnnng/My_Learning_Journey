# write a if else loop to determine the following condition
"""
1) >75 marks give A1
2) >= 70 <75 give A2
3) >,65 <70 give B3
.....
c6
Last F
"""
def grader(a):
    a=int(a)
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


def grader_2(a):
    a=int(a)
    if a > 100:
        return "Please enter a value less than or equal to 100"
    if a < 0:
        return "Please enter a value more than or equal to 0"
    if a>=75:
        return "A1"
    elif  a>= 70:
        return "A2"
    elif  a>=65:
        return "B3"
    elif  a>=60:
        return "B4"
    elif  a>=55:
        return "C5"
    elif a>=50:
        return "C6"
    else:
        return "FAIL"