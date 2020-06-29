# net-tools
This script allow an attacker to carry out a Double Tagging Attack on a target vlan. Use Wireshark on the target to verify that you receive a ICMP request from your ip address, if so, your switches have misconfigurations. 

## Usage
Python >= 3.4
> Scapy installation (Better in a venv)

`pip install --pre scapy[complete]`

> Attack example

`sudo python3 dtagging.py -o 1 -i 3 -a 192.168.1.8`
