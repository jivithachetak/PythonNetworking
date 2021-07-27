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
    print(default_ip(netifaces.AF_INET) )
    
if __name__ == "__main__":
    main()