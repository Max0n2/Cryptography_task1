import random as rdm

def mod(nun1: int, nun2: int):
    return nun1%nun2

def eulerian(n: int):
    result = n
    num1 = 2
    while num1**2 < n:
        while n % num1 == 0:
            n /= num1
            result -= result / num1
        num1 += 1
    if n > 1:
        result -= result / n
    return int(result)

def generaited_prime_list(start: int, stop: int):
    prime_list=[]
    for num1 in range(start, stop):
        for num2 in range(2,num1):
            if num1%num2==0:
                break
        else:
            prime_list.append(num1)
    return prime_list

a = int(input("Введіть а: "))
b = int(input("Введіть b: "))
m = int(input("Введіть m: "))

assig2 = mod(a, m)
assig3 = mod(a**b, m)
assig4 = mod(b*a**(eulerian(m)-1), m)
assig5 = rdm.choice(generaited_prime_list(a, b))

print(f'Завдання 2: {a} mod {m} = {assig2}')
print(f'Завдання 3: {a}^{b} mod {m} = {assig3}')
print(f'Завдання 4: {b}*{a}^(({m})-1) mod {m} = {assig4}')
print(f'Завдання 5: Згенерований простий список з {a} до {b} = {assig5}')
