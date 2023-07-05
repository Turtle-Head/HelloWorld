"""
Author: James Fehr Date: 07-04-2023
This script will print out the IP address of a domain name.
Can be used as a module or as a script.
Takes multiple domain names as arguments.
example:
python3 hello_d.py <domain name> [<domain name> ...]
python3 hello_d.py www.google.com www.apple.com
"""

import sys # import the sys module
import socket # import the socket module

def get_ip_address(domain): # define a function called get_ip_address
    try:
        ip_address = socket.gethostbyname(domain) # get the IP address of the domain
        return ip_address # return the IP address
    except socket.gaierror: # if the domain name is invalid
        return None # return None

if __name__ == "__main__": # if this script is run from the command line
    domain_names = sys.argv[1:] if len(sys.argv) > 1 else [] # get the domain names from the command line

    if domain_names: # if there are domain names
        for domain_name in domain_names: # loop through the domain names
            ip_address = get_ip_address(domain_name) # get the IP address of the domain name
            if ip_address: # if the IP address is valid
                print("Hello,", domain_name, "(", ip_address, ")") # print the domain name and IP address
            else:
                print("Unable to resolve IP address for", domain_name) # print an error message
    else:
        print("Please provide domain names as arguments.") # print an error message
