import math

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

def get_primes(number):
    while True:
        if is_prime(number):
            number = yield number
        number+=1
        

def solve_number_10():
    total=2
    for next_prime in get_primes(3):
        if next_prime <20:
            print(next_prime)
            total+=next_prime
        else:
            print(total)
            return

#solve_number_10()
    

def print_successive_primes(iterations,base=10):
    prime_generator=get_primes(base)
    prime_generator.send(None)
    for power in range(iterations):
        print(prime_generator.send(base ** power))

print_successive_primes(10)
        
