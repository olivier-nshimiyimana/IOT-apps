import pywhatkit
import datetime
import time

phone_no = "+250783305114"
message = "Sup mn <br>  Am trying out this thing of pywhatkit"
now = datetime.datetime.now()
time_hour = int(now.strftime("%H"))
time_min = int(now.strftime("%M")) 
time_second  = int(now.strftime("%S"))

# print("Random message to see if it works")
# print(time_hour)
# print(time_min)
# print(time_second)

# pywhatkit.sendwhatmsg(phone_no, message, 21, 5)
while(True):
    try: 
        print()
        pywhatkit.sendwhatmsg_instantly(phone_no, message,3, True,2)
        print("Message sent " + now.strftime("%H:%M:%S"))
        print()  


        time.sleep(60)

    except:
        print("Something went wrong")

