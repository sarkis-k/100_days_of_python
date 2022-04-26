import smtplib
import time
import requests
import datetime as dt


def iss_in_area():
    # return true if iss is in the circle +-5 degree
    if my_lat - 5 <= iss_lat <= my_lat + 5:
        if my_long - 5 <= iss_long <= my_long + 5:
            return True
    return False


def is_night():
    # return true if it's night sky in my place
    if sunset <= time_now.hour <= sunrise:
        return True
    return False


# ISS requests

iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_response.raise_for_status()

iss_long = float(iss_response.json()["iss_position"]["longitude"])
iss_lat = float(iss_response.json()["iss_position"]["latitude"])
iss_pos = (iss_long, iss_lat)

print(iss_pos)

# ISS only visible at night. get the sunset from api and if iss is in your sky notify yourself

my_long = -118.243683
my_lat = 34.052235

parameters = {
    "lat": my_lat,
    "lng": my_long,
    "formatted": 0
}

sun_response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
sun_response.raise_for_status()

data = sun_response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = dt.datetime.now()

while True:
    if is_night():
        if iss_in_area():
            # open smtp and send an email
            # connection = smtplib.SMTP("smtp.gmail.com")
            # connection.starttls()
            # connection.login(email, pass)
            # connection.sendmail(
            #     from_addr=,
            #     to_addrs=,
            #     msg="subject:\n\n"
            #         "msg"
            # )
            print("sent")
    print("not now")
    time.sleep(60)

# Kanye West requests

# from tkinter import *
#
#
# def get_quote():
#     response = requests.get(url="http://api.kanye.rest")
#     response.raise_for_status()
#
#     quote = response.json()["quote"]
#     canvas.itemconfigure(quote_text, text=quote)
#
#
# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)
#
# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="background.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"),
#                                 fill="white")
# canvas.grid(row=0, column=0)
#
# kanye_img = PhotoImage(file="kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
# kanye_button.grid(row=1, column=0)
#
# window.mainloop()
