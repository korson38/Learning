# task 2.a

def namer(name):
    print("Hello " + name)


names = ["Daniel", "Michal", "Bartek", "Krzysztof", "Julia"]
for x in names:
    namer(x)

# task 2.b


def multiplier(lst: list) -> list:
    new_list = []
    for num in lst:
        new_list.append(num*2)
    return new_list

# task 2.b - list comprehension


def multiply(lst: list) -> list:
    output_list = [x*2 for x in lst]
    return output_list

# task 2.c


def parzyste(liczby):
    num_clean = [x for x in liczby if x % 2 == 0]
    print(num_clean)

# task 2.d


def every_second(nums):
    for ind in range(0, len(nums), 2):
        print(nums(ind))

