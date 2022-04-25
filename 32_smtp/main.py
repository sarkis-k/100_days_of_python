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



