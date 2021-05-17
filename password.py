import random

length = int(input("length of your password => "))

lower_case = "qwertyuiopasdfghjklzxcvbnm"
upper_case = "ABCDEFGHIJKLMNTOPURWQZS"
symbols = "{}[]\|/?><+=-)(*&^%$#@!"
numbers = "1234567890"

all_elements = lower_case + upper_case + symbols + numbers

password_print = " ".join(random.sample(all_elements,length))
password_print_two = "".join(random.sample(all_elements,length))
print(password_print)
print(password_print_two)