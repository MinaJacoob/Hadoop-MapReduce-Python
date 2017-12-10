import csv
from random import *
import string
import random


def generate_email(size=10, chars=string.ascii_uppercase + string.digits):
    foo = ['@gmail.com', '@hotmail.com', '@fcih.edu.eg', '@yahoo.com']
    part_1 = ''.join(random.choice(chars) for _ in range(size))
    part_2 = random.choice(foo)
    return part_1 + part_2


with open("you_favourite_path/user_info.csv", 'wb')  as csvfile:
    id = 1000
    Languages = ["ENG", "AR", "FR", "SP", "IT"]
    locations = ["Brazil", "Canada", "Denmark", "Egypt", "Finland", "Germany", "Hong-Kong", "India", "Japan", "Kenya"]
    Writer = csv.writer(csvfile)
    for i in range(1, 22):
        Writer.writerow([str(id + i), generate_email(), Languages[randint(0, len(Languages) - 1)],
                         locations[randint(0, len(locations) - 1)]])

with open("you_favourite_path/product_info.csv", 'wb')  as csvfile2:
    transaction_id = 1000
    product_id = 1000
    user_id = 0
    purchase_amount = 0
    product_desc = "description"
    Writer2 = csv.writer(csvfile2)
    for i in range(1, 101):
        Writer2.writerow(
            [str(transaction_id + i), str(randint(1, 5)), str(randint(1001, 1020)), str(randint(1000, 2000)),
             product_desc])
