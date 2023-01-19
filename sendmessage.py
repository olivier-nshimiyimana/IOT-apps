import pywhatkit as pwk
import smtplib
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import time
from datetime import datetime

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('aristodush@gmail.com', 'bopfevckdyophgqf')

class Notify:
    def __init__(self,**climber):
        
        self.climberId=climber["id"]
        self.alt=climber["alt"]
        self.heart=climber["heart"]
        self.temperature=climber["temperature"]
        self.lat=climber["lat"]
        self.time=climber["time"]
        self.long=climber["long"]
    # using Exception Handling to avoid unexpected errors
    def sendWhatsapp(self,code):
        try:
            text="Climber id: *{}*\n Altitude: *{}*\n Time: *{}*\n HeartBeat: *{}BPM*\n Temperature: *{}Deg* \nSupport Code: *{}*\nLocation: https://www.google.com/maps/?q={},{}".format(self.climberId,self.alt,self.time,self.heart,self.temperature,code,self.lat,self.long)
            subject = "Climber feed back Support Code:  {}".format(code)
            message = 'Subject: {}\n\n{}'.format(subject, text)
            server.sendmail('aristodush@gmail.com', 'aristodush@gmail.com', message)
            print("Email sent")
            # # sending message in Whatsapp in India so using Indian dial code (+91)
            # pwk.sendwhatmsg_instantly("+250786344674", text)
            

        except: 
            print("Error in sending the message")

cred = credentials.Certificate(r"D:\Download\CLIMBER\climber-e8098-firebase-adminsdk-2fc00-775aa3a16c.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://climber-e8098-default-rtdb.firebaseio.com'
})

changeTemp=db.reference("/Climber/Kigali/Nyarugenge/Nyarugenge/Kiyovu/Isibo").get()
time.sleep(1)


while True:
    # try:
        # Get the data from your firebase path
        change=db.reference("/Climber/Kigali/Nyarugenge/Nyarugenge/Kiyovu/Isibo").get()

       
       
 
        if len(changeTemp.get("ClimberId_1")) == len(change.get("ClimberId_1")):
            print("tic")
            continue
            
        # if something changed in the hashes
        else:
            # # notify
            # print("something changed i am sending a notification right now")
            changeTemp=change
     
            # waw This code is crazy
            data={
                "id":1,
                "heart":"45",
                "temperature":"28",
                "time":"20/20/2020",
                "lat":"-1.958026289547252",
                "long":"30.064340967771606",
             
            }
            # very cool stuff
            lastInstance=list(changeTemp.get("ClimberId_1"))[-1]
            instance=changeTemp.get("ClimberId_1").get(lastInstance)

            data["heart"]=instance.get("HearBeat")
            
            data["alt"]=instance.get("Altitude")
            data["time"]=str(datetime.fromtimestamp(int(instance.get("Time"))))
        
            data["temperature"]=instance.get("Temperature")
            alert=Notify(**data)
            if float(instance.get("Temperature")) <=24 or int(instance.get("HearBeat")) <50  or int(instance.get("HearBeat")) >=120  or int(instance.get("Altitude")) >=5070 or  float(instance.get("Temperature"))>=29:
                if  float(instance.get("Temperature")) >=35  or int(instance.get("HearBeat")) <=29  or int(instance.get("HearBeat")) >100  or int(instance.get("Altitude")) >=5050 or  float(instance.get("Temperature")) <15:
                    alert.sendWhatsapp("Red")
                else:
                    alert.sendWhatsapp("Blue")

            time.sleep(10)
            print("checking...")
            time.sleep(1)
            continue
 
    # To handle exceptions
    # except Exception as e:
    #     print("error")
