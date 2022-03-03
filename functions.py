# functions in python

# data_type function_name(if_arguments){}

# def fun_name:

def add(a,b):
    return a+b

def fact(x):
    if x<0:
        return None
    elif x==0 or x==1:
        return 1
    else:
        return x*fact(x-1)

sum = add(3,4)

fact = fact(0)

print(fact)
