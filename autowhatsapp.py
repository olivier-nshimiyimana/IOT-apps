import pywhatkit

phone_no = "+250783305114"
message = "Hy"


# pywhatkit.sendwhatmsg_instantly(phone_no, message)

# Same as above but Closes the Tab in 2 Seconds after Sending the Message

# pywhatkit.sendwhatmsg_instantly(phone_no, message)

pywhatkit.sendwhatmsg(phone_no, message, 22, 17, 10, True, 4)

print("message sent")
