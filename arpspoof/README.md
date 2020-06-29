# net-tools
ARP spoofing attack allow an attacker the possibility to sniffing the communication between hosts in a network. You can use Wireshark to listen the traffic when you use the script.

## Usage
Python >= 3.4
> Scapy installation (Better in a venv)

`pip install --pre scapy[complete]`

> Example ARP spoofing attack

`./arpspoof.py -t 10.10.10.35 -s 10.10.10.254`
