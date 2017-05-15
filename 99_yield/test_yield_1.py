import math

def get_primes(input_list):
    result_list=list()
    for element in input_list:
        if is_prime(element):
            result_list.append(element)
    return result_list

def is_prime(number):
    if number>1:
        if number==2:
            return True
        if number%2==0:
            return False
        for current in range(3,int(math.sqrt(number)+1),2):
            if number%current ==0:
                return False
        return True
    return False

l=[1,2,3,4,5,6,7,8,9]
print(get_primes(l))

def simple_generator_function():
    yield 1
    yield 2
    yield 3

for value in simple_generator_function():
    print(value)

    
