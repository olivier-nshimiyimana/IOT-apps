import time
#from datetime import datetime
from csv import writer


import datetime

while (True):
    try :
        # list_data = []
        # this_moment = datetime.today().strftime('%Y-%m-%d %H:%M:%s')
        # list_data = ['price', 'pName', this_moment]

        # with open('csvfile.csv', 'a', newline='') as f_object:

        #     writer_object = writer(f_object)
        #     writer_object.writerrow(list_data)
        #     f_object.close()
        message = "Uploading every 3seconds"

                
        now = datetime.datetime.now()

        #seconds
        time.sleep(3)
        print()
        print(message)
        print("======================================== ")
        print ("Current date and time : ")
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
    except:
        print("Problem with script or manual exit")


