# import smtplib
# import datetime as dt
# import random
#
# my_email = "...@gmail.com"
# password = "12345"
# #
# # with smtplib.SMTP("smtp.gmail.com") as connection:
# #     connection.starttls()
# #     connection.login(user=my_email, password=password)
# #     connection.sendmail(from_addr=my_email, to_addrs="to@mail.ru", msg="Subject:hello\n\n"
# #                                                                      "this is the message")
# now = dt.datetime.now()
# if now.weekday() == 1:
#     with open("quotes.txt", "r") as quotes_file:
#         data = quotes_file.readlines()
#         random_quote = random.choice(data)
#
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=password)
#         connection.sendmail(
#             from_addr=my_email,
#             to_addrs="to@mail.ru",
#             msg=f"Subject:Motivation\n\n"
#                 f"{random_quote}")
#
#
#

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas as pd
import datetime as dt
import random
import smtplib
import os

now = dt.datetime.now()
month_day = (1,1)

data = pd.read_csv("birthdays.csv")
bday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
final_letter=""
if month_day in bday_dict:
    print("ta dam")
    bday_person = bday_dict[month_day]
    rand_letter_name = random.choice(os.listdir("/home/sk/Project/Udemy_2/everything/32_smtp/letter_templates"))
    with open(f"letter_templates/{rand_letter_name}", "r") as letter_to_send:
        for x in letter_to_send.readlines():
            final_letter += x

final_letter = final_letter.replace("[NAME]", bday_person["name"])
final_letter = final_letter.replace("Angela", "Sarkis")


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="to@mail.ru",
        msg=f"Subject:Happy BDay!\n\n"
            f"{final_letter}")