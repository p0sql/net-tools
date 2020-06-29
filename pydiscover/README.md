# net-tools
This script allow an attacker or networks administrator scan the network to find available hosts in a network through ARP protocol.

## Usage
Python >= 3.4
> Scapy installation (Better in a venv)

`pip install --pre scapy[complete]`

> Example to discovery network

`./pydiscover.py -r 172.16.0.0/16`
