import optparse
import scapy.all as scapy

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--ip", dest="ip", help="IP address to enter")
    parser.add_option("-r", "--range", dest="range", help="Subnet to enter")
    (options, arguments) = parser.parse_args()
    if options.ip:
        return options.ip
    if options.range:
        return options.range
    if not options.ip and not options.range:
        parser.error("[-] Specify an ip address or a CIDR mask")

def scan(ip):
    arp_req = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_packet = broadcast/arp_req
    answered = scapy.srp(arp_packet, timeout=1, verbose=False)[0]

    print("IP\t\t\tMAC Address\n---------------------------------------------")
    for i in answered:
        print("{}\t\t{}".format(i[1].psrc, i[1].hwsrc))

options = get_arguments()
scan(options)