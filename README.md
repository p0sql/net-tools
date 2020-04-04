# net-tools
Networks tools to accomplish network discovery and ARP spoofing attack. These tools are useful for people works on Fedora or who use Linux distros does not have packages for netdiscover.

## Usage
Python >= 3.4
> Scapy installation (Better in a venv)

`pip install --pre scapy[complete]`

> Example ARP spoofing attack

`./arpspoof 10.10.10.35 10.10.10.254`

> Example to discovery network

`./pydiscover -r 172.16.0.0/16`
