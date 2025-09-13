import requests
import datetime
import smtplib

my_lat=26.218287
my_lng=78.182831
my_email="aryantest1221@gmail.com"
my_pass="Test@1234"
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    print(data)
    latitude=data["iss_position"]["latitude"]
    longitude=data["iss_position"]["longitude"]
    if my_lat-5<= latitude<=my_lat+5 and my_lng-5<=longitude<=my_lng+5:
        return True


def is_night():
    parameters= {
        "lat":my_lat,
        "lng":my_lng,
        "formatted":0,
    }
    response_s= requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
    response_s.raise_for_status()
    data_s=response_s.json()
    sunrise=int(data_s["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset=int(data_s["results"]["sunset"].split("T")[1].split(":")[0])

    time_now= datetime.datetime.now().hour
    if time_now>=sunset or time_now<=sunrise:
        return True
#while True:  #can use if we want the program to run continuously
if is_iss_overhead() and is_night():
    connection=smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(my_email,my_pass)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=my_email,
        msg="Look up "
    )





