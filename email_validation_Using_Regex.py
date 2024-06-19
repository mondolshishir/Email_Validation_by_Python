# a-z, 0-9, . _(one time),@(one time), .(will be using 2,3 steps before mail closing)

import re

email_condition = r"^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email = input("Enter your Email : ")

if re.search(email_condition, user_email):
    print("Your Enter Email is correct !!!!!")
else:
    print("You Enter a wrong email. Please follow # a-z, 0-9, . _(one time),@(one time), .(will be using 2,"
          "3 steps before mail closing)")
