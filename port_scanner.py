import socket
import sys
import pyfiglet
import geocoder
from datetime import datetime

text1=pyfiglet.figlet_format(text="Port",font='isometric1')
text2=pyfiglet.figlet_format(text="Scanner",font='isometric1')
print(text1)
print(text2)

while True:
    HOST=input(str("\nEnter the URL of the website to scan: "))
    PORT=int(input(("Enter Port Number: ")))
    try:
            start_time = datetime.now()
            target = socket.gethostbyname(HOST)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            conn = s.connect_ex((HOST,PORT))
            if conn ==0:
                print("Port {} is open".format(PORT))
                s.close() 
            else:
                print("Port {} is closed".format(PORT))
                s.close()
                
            g = geocoder.ip(target)
            end_time = datetime.now() 
            time_diff = end_time - start_time 

            print("Scan speed: {} seconds".format(time_diff.total_seconds())) 

            print("\nGeolocation Information:")
            print("Latitude: {}".format(g.lat))
            print("Longitude: {}".format(g.lng))
            print("Country: {}".format(g.country))
            print("City: {}".format(g.city))

    except KeyboardInterrupt:
            print("Quiting")
            sys.exit()

    except socket.error:
            print("Server not responding try again")
            sys.exit() 
    val=input(str("\nWould you like to try again y/n :"))
    if val =='y':
          continue
    elif val =='n':
          break
    else:
          print("please enter a valid option")
          break
    
          