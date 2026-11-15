#constanta
MY_LAT=33.1928
MY_LNG=73.1410
MY_EMAIL="harisafsar2007@gmail.com"
MY_PASSWORD="qlnq ipyw lctr zant"
#LIBRARIES
import time
import requests
import datetime
import smtplib



#CURRENT TIME MODULE
now=datetime.datetime.now()
my_time=now.hour

#SUNRISE SUNSET API MODULE
location ={
    "lat":MY_LAT,
    "lng":MY_LNG,

}
request=requests.get("https://api.sunrise-sunset.org/v2",params=location)
request.raise_for_status()
data=request.json()
sunrise=int(data["sunrise"].split("T")[1].split(":")[0])
sunset=int(data["sunset"].split("T")[1].split(":")[0])


#CONDITIONS CHECKS

def location_check(MY_LAT,MY_LNG):
    # ISIS LOCATION MODULE
    # using requests to get response from api endpoint
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    data = response.json()
    # creating tuple from json
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])
    position = (longitude, latitude)
    if MY_LAT-5<=latitude<=MY_LAT+5 and MY_LNG-5<=longitude<=MY_LNG+5:
        return 1
    else:
        return 0


def time_check(my_time):
    # SUNRISE SUNSET API MODULE
    location = {
        "lat": MY_LAT,
        "lng": MY_LNG,

    }
    request = requests.get("https://api.sunrise-sunset.org/v2", params=location)
    request.raise_for_status()
    data = request.json()
    sunrise = int(data["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["sunset"].split("T")[1].split(":")[0])

    if my_time<=sunrise or my_time>=sunset:
        return 1
    else:
        
     return 0



#sending emails
condition_1=location_check(MY_LAT,MY_LNG)
print(condition_1)
condition_2=time_check(my_time)
print(condition_2)
while True:
    time.sleep(60)
    if condition_1==1 and condition_2==1:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL,password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,to_addrs="cryptoman157@gmail.com",msg="Subject:LOOK UP!!\n\nwhoa!! whoa!! Look up bro !! ISIS ! Haris Afsar")
            print("Its above ")
    else:
        print("all good but its not above")



