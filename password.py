import random

lower_case = "qwertyuiopasdfghjklzxcvbnm"
upper_case = "ABCDEFGHIJKLMNTOPURWQZS"
symbols = "{}[]\|/?><+=-)(*&^%$#@!"
numbers = "1234567890"
length = 20

all_elements = lower_case + upper_case + symbols + numbers

password_print = "".join(random.sample(all_elements,length))
print(password_print)