import matplotlib.pyplot as plt
from datetime import datetime


import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


# Set time period
start = datetime(2022, 11, 1)
end = datetime(2022, 11, 11)


# Fetch the service account key JSON file contents
cred = credentials.Certificate(r"D:\Download\CLIMBER\climber-e8098-firebase-adminsdk-2fc00-775aa3a16c.json")

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://climber-e8098-default-rtdb.firebaseio.com'
})


class Climber:
    timeStamps=[]
    timeDate=[]

    def __init__(self,climber):
        self.climber=climber

        self.__getTimestamp()
        # self.__getDate()
 

    def __getTimestamp(self):
        keys=[]
        # Get ALl the data keys
        for data in self.climber.get("Climber").get("Kigali").get("Nyarugenge").get("Nyarugenge").get("Kiyovu").get("Isibo").get("ClimberId_1").keys():
            keys.append(data)
        self.timeStamps=keys
        
    # onOff = onStatus
    # FAILURE: STATUS

    # 
    # def __getDate(self):
    #     for tmstmp in self.timeStamps:
    #         self.timeDate.append(datetime.fromtimestamp(tmstmp))
    # @property
    # def onStatusTimegetDate(self):
    #     onStatus = []
    #     totalOnTime=[]
    #     totalOffTime=[]
    #     for i,time in enumerate(self.timeStamps):
    #         # Stop Theloop if at the end
    #         if i==len(self.timeStamps)-1:
    #             break
    #         if  self.climber.get("Failure").get("Kigali").get("Nyarugenge").get("Nyarugenge").get("Sensor_1").get(str(time)):
    #             if(self.climber.get("Failure").get("Kigali").get("Nyarugenge").get("Nyarugenge").get("Sensor_1").get(str(time)).get("Climber")):
    #                 totalOnTime.append(self.timeStamps[i+1]-time)
    #             else:
    #                 totalOffTime.append(self.timeStamps[i+1]-time)
    #         onStatus.append(self.timeStamps[i+1]-time)
    #     return [onStatus,totalOffTime,totalOnTime]

    # Get the daily On and off Time From the current Day, 
    # This data represent the first Pie chart
    def getDailyOnStatusTime(self):
        onStatus = []
        for i,time in enumerate(self.timeStamps):
            if i==len(self.timeStamps)-1:
                break
            onStatus.append(self.timeStamps[i+1]-time)
        return onStatus


    # function to format timestap to appropriate format 
    def formatedDateTime(self,data=timeDate):
        values= []
        for i in data:
            values.append(i.strftime("%a, %H:%M"))
        return values
    # Function to get the current and Voltage data from 
    def temperature(self):
        temperature=[]
        altitude=[]
        heartBeat=[]
        time=[]
        for i in self.climber.get("Climber").get("Kigali").get("Nyarugenge").get("Nyarugenge").get("Kiyovu").get("Isibo").get("ClimberId_1"):
            alt=self.climber.get("Climber").get("Kigali").get("Nyarugenge").get("Nyarugenge").get("Kiyovu").get("Isibo").get("ClimberId_1").get(i).get("Altitude")
            temp=self.climber.get("Climber").get("Kigali").get("Nyarugenge").get("Nyarugenge").get("Kiyovu").get("Isibo").get("ClimberId_1").get(i).get("Temperature")
            tempb=self.climber.get("Climber").get("Kigali").get("Nyarugenge").get("Nyarugenge").get("Kiyovu").get("Isibo").get("ClimberId_1").get(i).get("HearBeat")
            if float(temp)>=0:
                temperature.append(float(temp))
                altitude.append(int(alt))
                
            if float(tempb)>=35:
                heartBeat.append(float(tempb))
                altitude.append(int(alt))
            
        
            time.append(datetime.fromtimestamp(int(self.climber.get("Climber").get("Kigali").get("Nyarugenge").get("Nyarugenge").get("Kiyovu").get("Isibo").get("ClimberId_1").get(i).get("Time"))))
        return [temperature,heartBeat,altitude,self.formatedDateTime(time)]
        





climber=db.reference("/").get()




mydata=Climber(climber)
print("TEMPERATURE DATA TO BE USED FOR DECISION TAKING")
print("======================================================")
print(mydata.temperature()[0])

print("HEART BPM DATA TO BE USED FOR DECISION TAKING")
print("======================================================")
print(mydata.temperature()[1])

print("ALTITUDE DATA TO BE USED FOR DECISION TAKING")
print("======================================================")
print(mydata.temperature()[2])
# labels =["Thu 06:30","Thu 09:30", "Thu 11:30", "Thu 11:54", "Thu 12:30"]
# sizes = [83149,4306, 2000, 2189, 43149]

# currentData=mydata.currentData()

# injury=mydata.injuryData()


# colors=['#DAFFA6','#ffa600']
# explode = (0.1,0, 0.1,0, 0.1)




fig, axs = plt.subplot_mosaic([['upper left', 'lower left','middle left']],
                              figsize=(5.5, 3.5), layout="constrained")

# # Figure one 
# axs['upper left'].pie(sizes, labels=labels, explode=explode,autopct='%1.1f%%',shadow=True, startangle=45,textprops={'size': 'x-small'},colors=colors)
# axs['upper left'].set_title('Daily Climber Status')

# # Figure one
axs['upper left'].plot(mydata.temperature()[0])
# axs['lower left'].plot(mydata.temperature()[1])

axs['upper left'].legend(["temperature"])
axs['upper left'].set_title("temperature")
axs['upper left'].grid(True,color="#ff0131")


# # Figure Two
axs['lower left'].plot(mydata.temperature()[1])

axs['lower left'].legend(["Heart"])
axs['lower left'].set_title("Heart Beat Variation")
axs['lower left'].set_ylim(1,100)
axs['lower left'].set_yticks(range(30,120,10))
axs['lower left'].grid(True,color="#89cff0")




# # Figure Three
axs['middle left'].plot(mydata.temperature()[2])

axs['middle left'].legend(["Altitude"])
axs['middle left'].set_title("Altitude variation")
axs['middle left'].grid(True,color="#ff0343")

axs['lower left'].set_ylim(1,100)
axs['lower left'].set_yticks(range(30,120,10))

# # # Figure one
# axs['upper left'].plot(mydata.temperature()[0])
# # axs['lower left'].plot(mydata.temperature()[1])

# axs['upper left'].legend(["temperature"])
# axs['upper left'].set_title("temperature")
# axs['upper left'].grid(True,color="#ff0131")



# Bicolors=['#ffa600','#42b883']
# # Figure Three 
# axs["upper right"].pie(injury.get("Kigali"), labels=["Injury Area","Non Injury Area"],autopct='%1.1f%%',shadow=True, startangle=45,textprops={'size': 'x-small'},colors=Bicolors)
# axs["upper right"].set_title('Kigali/Nyarugenge Injury')




# # Figure Four 
# axs["middle top right"].pie(Injury.get("Nyarugenge").get("Nyarugenge"), labels=["Injury Area","Non Injury Area"],autopct='%1.1f%%',shadow=True, startangle=45,textprops={'size': 'x-small'},colors=Bicolors)
# axs["middle top right"].set_title('Nyarugenge Injury')




# import pandas as pd 

# from datetime import datetime
# import matplotlib.pyplot as plt
# from meteostat import Point, Daily

# # Create Point for Vancouver, BC
# city = Point(-1.966829,30.063457)

# # Get daily data for 2018
# apiData = Daily(city, start, end)
# apiData = apiData.fetch()

# # Create a new instance of daframe 
# df = {
#   "injuryStatus": mydata.getDailyOnStatusTime(),
#   "wind": apiData.wspd,
#   "Temperature": apiData.tmin,
# }

# data = pd.DataFrame(df)

# # Analyse correlation between different datas
# print(data.corr())

plt.show()



