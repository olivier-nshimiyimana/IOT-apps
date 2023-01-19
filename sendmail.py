# import smtplib
# import time

# i=0;
# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.starttls()


# server.login('aristodush@gmail.com', 'bopfevckdyophgqf')
# while(True):
#     try: 

#         subject = "This is message sent using python  #" + str(i)
#         text = "Mail sent from python"
#         message = 'Subject: {}\n\n{}'.format(subject, text)
#         server.sendmail('aristodush@gmail.com', 'aristodush@gmail.com', message)
#         print("Message sent : " + str(i+1))
#         i = i+1
#         time.sleep(10)
#     except:
#         print("Something went wrong")


ar = ['le', 'he']

print(len(ar))

