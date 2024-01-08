# task 1

def greet(name: string, surname: string) -> string:
    return f"Cześć {name} {surname}!"


# task 2


def multiply(val1: int, val2: int) -> int:
    return val1 * val2


# task 3


def czy_parzysta(val: int) -> bool:
    return val % 2 == 0


if czy_parzysta(2):
    print("parzysta")
else:
    print("Nie parzysta")

# task 4


def checker(val1: int, val2: int, val3: int) -> bool:
    output = val1 + val2 == val3 or val1 + val2 > val3
    return output

# task 5


def szukam(list_val: list, val: int) -> bool:
    return val in list_val

# task 6


def list_adder(list1: list, list2: list) -> list:
    new_list = list1 + list2
    no_duplicates = []
    for elem in new_list:
        if elem not in no_duplicates:
            no_duplicates.append(elem)
    no_duplicates = [x**3 for x in no_duplicates]
    return no_duplicates


