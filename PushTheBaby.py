import pywhatkit as pwk
 
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import time



cred = credentials.Certificate(r"D:\Download\CLIMBER\climber-e8098-firebase-adminsdk-2fc00-775aa3a16c.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://climber-e8098-default-rtdb.firebaseio.com'
})

data= {
    "Altitude": "5062",
    "Cell": "Kiyovu",
    "District": "Nyarugenge",
    "HearBeat": "73",
    "Latitude": -1.95552,
    "Longitude": 30.06367,
    "Province": "Kigali",
    "Sector": "Nyarugenge",
    "Temperature": "21.25",
    "Time": 1669281548,
    "Village": "Isibo",
    "climebrId": "1"
              }

path=str(int(time.time()))
data= {
    "Altitude": "6062",
    "Cell": "Kiyovu",
    "District": "Nyarugenge",
    "HearBeat": "73",
    "Latitude": -1.95552,
    "Longitude": 30.06367,
    "Province": "Kigali",
    "Sector": "Nyarugenge",
    "Temperature": "25",
    "Time": path,
    "Village": "Isibo",
    "climebrId": "1"
            }

users_ref = db.reference('/Climber/Kigali/Nyarugenge/Nyarugenge/Kiyovu/Isibo/ClimberId_1/{}'.format(path)).set(
    data
)   

print("Data sent")