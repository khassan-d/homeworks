import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    if min < 1 or max > 1000 or not 1 <= quantity <= max - min + 1:
        return []

    numbers = [number for number in range(min, max + 1)]
    return sorted(random.sample(numbers, quantity))

test = get_numbers_ticket(1, 2, 1)
print(test)