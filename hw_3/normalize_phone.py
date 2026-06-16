import re

def normalize_phone(phone_number: str) -> str:
    pattern = r'[\D]'
    replacement = ""
    only_number_string = re.sub(pattern,replacement,phone_number)
    pure_num_pattern = r'[0]\d+'
    pure_num = re.search(pure_num_pattern, only_number_string)

    return f'+38{pure_num.group()}'

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print(sanitized_numbers)

