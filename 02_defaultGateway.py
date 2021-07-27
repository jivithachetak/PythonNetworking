
import netifaces


#Return the default gateway IP for the machine.
def get_machine_default_gateway_ip():
    
    gateways = netifaces.gateways()
    defaults = gateways.get("default")
    
    if not defaults:
        return
    else :
        return defaults.values()

def main():
    print(get_machine_default_gateway_ip() )
    
if __name__ == "__main__":
    main()