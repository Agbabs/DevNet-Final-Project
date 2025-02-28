import ipaddress
    #This module is used for creating, manipulating, and analyzing IP addresses and networks. 
    # It is utilized in the code to handle IPv4 networks and subnetting operations.

import math 
    #This module provides mathematical functions, 
    #and here it is used to calculate the number of bits required to create the requested number of subnets.

import os
    #This module is used for interacting with the operating system, 
    # such as getting the directory of the script to save output files.

import pandas as pd
    #The import for this module is commented out, so it will not be used unless uncommented. If enabled, 
    # it would help convert the results into a DataFrame and save them to a CSV file.

def subnet_calculator(network, num_subnets):
    try:
        network = ipaddress.IPv4Network(network, strict=False)
        new_prefix_len = network.prefixlen + math.ceil(math.log2(num_subnets))
        subnets = list(network.subnets(new_prefix=new_prefix_len))
        if len(subnets) < num_subnets:
            raise ValueError("Not enough subnets available")

        results = []
        for subnet in subnets[:num_subnets]:
            entry = {
                "Subnet Network Address": str(subnet.network_address),
                "Broadcast Address": str(subnet.broadcast_address),
                "Subnet Mask": str(subnet.netmask),
                "Number of Usable Hosts": subnet.num_addresses - 2,
                "First Usable Host": str(subnet.network_address + 1),
                "Last Usable Host": str(subnet.broadcast_address - 1)
            }
            results.append(entry)
        return results
    except ValueError as e:
        return [{"Error": str(e)}]

def main():
    network = input("Enter the network address (e.g., 192.168.40.0/24): ")
    num_subnets = int(input("Enter the number of subnets: "))
    
    results = subnet_calculator(network, num_subnets)
    
    df = pd.DataFrame(results)
    
    scripts_dir = os.path.dirname(os.path.realpath(__file__))
    output_file = os.path.join(scripts_dir, "subnet_calculator_output.csv")
    df.to_csv(output_file, index=False)
    print(f"Results saved to {output_file}")
main()

