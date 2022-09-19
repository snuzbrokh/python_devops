from random import choices


def fruit():
    fruits = ["apple", "banana", "kiwi"]

    return choices(fruits)[0]


def meal(beverage):
    my_fruit = fruit()
    if my_fruit == "kiwi":
        complete_meal = f"Your meal is a {my_fruit} and {beverage}"
        return complete_meal
    return f"Have some steak and {beverage}"
