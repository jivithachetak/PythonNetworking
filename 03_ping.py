import os
import netifaces


#AF_INET is a dictionary of ip address families. 
#Breaking down the dictionary to derive the desired ip adress family
def default_ip(ip_family):
        gateways = netifaces.gateways()
        defaults =gateways.get("default")
        gateway_info = defaults.get(ip_family)
        if not gateway_info:
            return
        #Breaking down the IPaddress dictionary to obtain key:value pair
        addresses = netifaces.ifaddresses(gateway_info[1]).get(ip_family)
        if addresses:
            return addresses[0]["addr"]

        return default_ip(netifaces.AF_INET) or default_ip(netifaces.AF_INET6) 

def main():
 ip = default_ip(netifaces.AF_INET)
 response = os.system("ping -c 1 " + ip)

#Checking connection by status code {0}
 if response == 0 :
        print(ip , "gateway Ping Successful")
 else:
        print(ip , "gateway Ping Unsuccessful")


 
    
if __name__ == "__main__":
    main()

