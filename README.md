# Generate arbitary IP network topologies

Generates arbitary IP network topologies (ASN networks)
which you can optionally carve into different prefixes as an
Internet Routing Registry (IRR) would do.

Inputs:

- Number of networks you want
- (optional) specify exact number of subnets per network

Output:

- A `List` of networks, optionally subnetted as requested.

If exact number of subnets is not chosen, then the default class subnet is used.

# Usage example

> Only a recent python 3 is neded. There are no external dependencies to install. :)

Here we ask for 3 disparate networks, and control the number of subnets
(prefix lengths) carved out of teahc of those networks.

```
python3 -i main.py 
How many disparate networks do you want?3
Do you want to specify the exact number of subnets per network? y/n: y
DEBUG:root:Ask exactly how many subnets wanted per network
How many subnets do you want in network 1?6
How many subnets do you want in network 2?3
How many subnets do you want in network 3?1
DEBUG:root:Generating network 0
DEBUG:root:You have been assigned 112.162.186.208
DEBUG:root:Your ina assigned network address is 112.0.0.0/8
DEBUG:root:The deault number of subnets for 112.0.0.0/8 is 2
DEBUG:root:The default number of subnets for 112.0.0.0/8 is 2, but we want 6
DEBUG:root:Borriwing 3 bits for 6 networks requested
DEBUG:root:The number of borrowed bits for network are: 11
DEBUG:root:Great. We wanted at least 6 and we have 8
DEBUG:root:The max number of hosts per subnet is now: 2097152
DEBUG:root:Generating network 1
DEBUG:root:You have been assigned 188.156.194.98
DEBUG:root:Your ina assigned network address is 188.156.0.0/16
DEBUG:root:The deault number of subnets for 188.156.0.0/16 is 2
DEBUG:root:The default number of subnets for 188.156.0.0/16 is 2, but we want 3
DEBUG:root:Borriwing 2 bits for 3 networks requested
DEBUG:root:The number of borrowed bits for network are: 18
DEBUG:root:Great. We wanted at least 3 and we have 4
DEBUG:root:The max number of hosts per subnet is now: 16384
DEBUG:root:Generating network 2
DEBUG:root:You have been assigned 113.93.88.76
DEBUG:root:Your ina assigned network address is 113.0.0.0/8
DEBUG:root:The deault number of subnets for 113.0.0.0/8 is 2
DEBUG:root:The default number of subnets for 113.0.0.0/8 is 2, but we want 1
DEBUG:root:Borriwing 0 bits for 1 networks requested
DEBUG:root:The number of borrowed bits for network are: 8
DEBUG:root:Great. We wanted at least 1 and we have 1
DEBUG:root:The max number of hosts per subnet is now: 16777216
>>> networks
[{'network': IPv4Address('112.162.186.208'), 'subnets': [IPv4Network('112.0.0.0/11'), IPv4Network('112.32.0.0/11'), IPv4Network('112.64.0.0/11'), IPv4Network('112.96.0.0/11'), IPv4Network('112.128.0.0/11'), IPv4Network('112.160.0.0/11'), IPv4Network('112.192.0.0/11'), IPv4Network('112.224.0.0/11')]}, {'network': IPv4Address('188.156.194.98'), 'subnets': [IPv4Network('188.156.0.0/18'), IPv4Network('188.156.64.0/18'), IPv4Network('188.156.128.0/18'), IPv4Network('188.156.192.0/18')]}, {'network': IPv4Address('113.93.88.76'), 'subnets': [IPv4Network('113.0.0.0/8')]}]
>>> 
```

