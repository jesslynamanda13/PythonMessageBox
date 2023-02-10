import pywhatkit
# pip install pywhatkit

print("Welcome to Message Box!")
print("Enter the number you'd like to message")
number = input("Enter your number (+62....)")
message = input("Write you message...")
hour,min = input("When will they receive your message?(hour min)").split()

pywhatkit.sendwhatmsg(number, message, int(hour), int(min))
print("Your message has been delivered, thanks for using Message Box!")