''' 
A very simple server 
'''

##################
from getpass import getpass
from art import *
import time
import socket
###################

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

print("\n\n\n")


############## Registration ############
isRegistered = input("Are you registered on our server? (yes/no) : ").lower()

# if isRegistered == 'no':
#   print("[ALERT] : You need to register before logging into our server!".center(100))
#   print("Contact your administrator for more info .".center(100))
#   GotIt = input("Enter 'q' to quit : ")
#   while not GotIt == 'q':
#     print("[ERROR] : Invalid input .")
#     GotIt = input("Enter 'q' to quit : ")
#   exit()

# elif isRegistered == 'yes':
#     print("Taking you to the server ...")
#     time.sleep(2)

# else:
#     print("ERROR: Invalid input.")

while not isRegistered == 'yes' and not isRegistered == 'no':
    print("ERROR: Invalid input.\n")
    isRegistered = input("Are you registered on our server? (yes/no) : ").lower()


if isRegistered == 'no':
  print("\n\n")
  print("[ALERT] : You need to register before logging into our server!".center(100))
  print("Contact your Administrator for more info.".center(100))
  GotIt = input("Enter 'q' to quit : ")
  while not GotIt == 'q':
    print("[ERROR] : Invalid input .")
    GotIt = input("Enter 'q' to quit : ")
  exit()

else:
    print("Taking you to the server ...")
    time.sleep(2)


########################################
print("\n\n")
for i in range(90):
  print("*",end='')

tprint("\nServer  Login")
time.sleep(2)

########## Authentication ##############
User = input("Server Username: ".center(50))
print("\n")
print("[NOTE] : Password isn't visible !".center(68))
print("\n")
Pass = getpass("Server Password: ".center(50))
########################################
usernames = 'abraar','admin'
password = 'admin@786'

while not User == usernames and not Pass == password:
  print("\n\n")
  for i in range(90):
    print("*",end='')
  print("\n\n[ERROR] : Wrong Authentication ! Please try again or quit immediately\n\n".center(50))
  User = input("Server Username: ".center(50))
  print("\n")
  print("[NOTE] : Password isn't visible !".center(60))
  print("\n")
  Pass = getpass("Server Password: ".center(50))

print("\n\n")



############### Main Terminal ############################
for i in range(90):
  print("*",end='')
tprint("\n\nWelcome   Admin !",font="small")
print("Admin accessed : ",User.center(50))
print("Admin hostname : ",hostname.center(50))
print("Admin Ipv4 : ",IPAddr.center(60))
print("Login: ",time.strftime("%B %d, %Y [%H:%M:%S]".center(70)))
print("\n")



print("\n\nProgram done.")


