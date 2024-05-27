#--Email Validation in Python(Using RegEx)
# a-z jensastha987@gmail.com
# 0-9
# . _ one time
# @ one time
# . 2,3 position from last

import re #regEx module
email_condition = r"^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$" # + joins the condition
user_email = input("Enter your Email : ") #g@g.in / .com

if re.search(email_condition, user_email): #Matches email_condition and user_email
    print("Right Email")
else:
    print("Wrong Email")
