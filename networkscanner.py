#!/usr/bin/python3

import scapy.all as scapy
import argparse
from colorama import Fore


def get_arguments():
    parse = argparse.ArgumentParser()
    parse.add_argument("-t", "--target", dest="target", help="specify the target network or IP range")
    args = parse.parse_args()
    if not args.target:
        parse.error("[-] Please specify the target IP range using the -t or --target option.")
    return args


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    mac_request = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    broadcast_request = mac_request/arp_request
    answered_list = scapy.srp(broadcast_request, timeout=1, verbose=False)[0]

    create_list = []
    for element in answered_list:
        create_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        create_list.append(create_dict)

    return create_list

print("-----------------------------------------")
def result_scan(result_list):
    print(" IP\t\t\tMAC ADDRESS\n-----------------------------------------")
    for client in result_list:
        print(client["ip"] + "\t\t" + client["mac"])


def main():
    args = get_arguments()
    target = args.target
    scan_result = scan(target)
    result_scan(scan_result)


if __name__ == "__main__":
    main()
