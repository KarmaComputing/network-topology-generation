from ipaddress import IPv4Address
import random

classA_start_address = int(IPv4Address("0.0.0.0"))
classA_end_address = int(IPv4Address("127.255.255.255"))
classArange = range(classA_start_address, classA_end_address)

classB_start_address = int(IPv4Address("128.0.0.0"))
classB_end_address = int(IPv4Address("191.255.255.255"))
classB_range = range(classB_start_address, classB_end_address)

classC_start_address = int(IPv4Address("192.0.0.0"))
classC_end_address = int(IPv4Address("223.255.255.255"))
classC_range = range(classC_start_address, classC_end_address)


def get_default_classful_netmask(network_address):
    network_address = int(network_address)
    if network_address in classArange:
        return "/8"
    elif network_address in classB_range:
        return "/16"
    elif network_address in classC_range:
        return "/24"
    raise Exception(f"Could not determin default netmask for {network_address}")


def get_ip_class(network_address):
    network_address = int(network_address)
    if network_address in classArange:
        return "A"
    elif network_address in classB_range:
        return "B"
    elif network_address in classC_range:
        return "C"


def get_random_public_ip():
    """Generate random public IP address within
    classful A, B, C ranges"""

    random_range = random_of_ranges([classArange, classB_range, classC_range])
    random_num_within_rage = random.choice(random_range)
    random_public_ip = IPv4Address(random_num_within_rage)
    return random_public_ip


def random_of_ranges(*ranges):
    """https://stackoverflow.com/a/45415604"""
    all_ranges = sum(ranges, [])
    return random.choice(all_ranges)
