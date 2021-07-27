import os
#example host name

#Checking internet connection by status code {0}
def main():
 hostname = "www.heise.de" 
 status  = os.system("ping -c 1 " + hostname)

 if status == 0:
  print (hostname, 'is up!')
 else:
  print (hostname, 'is down!')
  