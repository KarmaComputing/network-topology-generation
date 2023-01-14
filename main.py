from ipaddress import IPv4Network
from math import log, ceil
from ip_classes import get_default_classful_netmask, get_random_public_ip
import logging
from json import JSONEncoder

"""Generate arbitary IP network topologies"""

logging.basicConfig(level="DEBUG")


class NetworksEncoder(JSONEncoder):
    """Serialize networks object"""

    def default(self, o):
        return str(o)


def main():
    DESIRED_NUM_NETWORKS = int(input("How many disparate networks do you want?"))
    CHOOSE_NUMBER_OF_SUBNETS = input(
        "Do you want to specify the exact number of subnets per network? y/n: "
    )
    if CHOOSE_NUMBER_OF_SUBNETS != "y":
        DESIRED_NUMBER_OF_SUBNETS = int(
            input("How many subnets per each network do you want? ")
        )
    else:
        logging.debug("Ask exactly how many subnets wanted per network")
        map_desired_subnets_per_network = {}
        # Key is subnet number, value is the DESIRED_NUMBER_OF_SUBNETS
        for i in range(0, DESIRED_NUM_NETWORKS):
            msg = f"How many subnets do you want in network {i + 1}?"
            map_desired_subnets_per_network[i] = int(input(msg))

    networks = []

    for i in range(0, DESIRED_NUM_NETWORKS):
        logging.debug(f"Generating network {i}")
        if CHOOSE_NUMBER_OF_SUBNETS == "y":
            asn = generate_asn_network(
                number_of_subnets=map_desired_subnets_per_network[i]
            )
        else:
            asn = generate_asn_network(number_of_subnets=DESIRED_NUMBER_OF_SUBNETS)
        networks.append(asn)

    dump_networks(asn)
    return networks


def generate_asn_network(number_of_subnets=None):
    """Generate a public network with n subnets
    - Generate a random public ip address within class A,
      B, or C range.
    - Performs netmask calculation to borrow host bits to
        divide network into number_of_subnets

    :returns: Dict ASN {"network": <ip-address>, "subnets", []}
    """
    asn = {}
    assigned_network = get_random_public_ip()
    asn["network"] = assigned_network

    logging.debug(f"You have been assigned {assigned_network}")

    # Determine default network class for public network
    default_subnetmask = get_default_classful_netmask(assigned_network)

    # See https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network
    default_network = IPv4Network(f"{assigned_network}{default_subnetmask}", False)

    logging.debug(f"Your ina assigned network address is {default_network}")
    default_num_subnets = len(list(default_network.subnets()))
    logging.debug(
        f"The deault number of subnets for {default_network} is {default_num_subnets}"
    )

    logging.debug(
        f"The default number of subnets for {default_network} is {default_num_subnets}, but we want {number_of_subnets}"
    )

    NUM_BORROWD_BITS_NEEDED = ceil(log(number_of_subnets, 2))

    # Unpartitioned default TEST-NET-1
    # See https://www.iana.org/assignments/iana-ipv4-special-registry/iana-ipv4-special-registry.xhtml

    # Borrow n bits for y networks requested
    logging.debug(
        f"Borriwing {NUM_BORROWD_BITS_NEEDED} buts for {number_of_subnets} networks requested"
    )

    num_borrowed_bits = default_network.prefixlen + NUM_BORROWD_BITS_NEEDED
    logging.debug(f"The number of borrowed bits for network are: {num_borrowed_bits}")

    subnets = list(default_network.subnets(new_prefix=num_borrowed_bits))

    total_num_subnets = len(subnets)

    logging.debug(
        f"Great. We wanted at least {number_of_subnets} and we have {total_num_subnets}"
    )
    NUM_HOST_BITS = 32 - num_borrowed_bits
    MAX_NUM_HOSTS_PER_SUBNET = 2**NUM_HOST_BITS
    logging.debug(
        f"The max number of hosts per subnet is now: {MAX_NUM_HOSTS_PER_SUBNET}"
    )
    asn["subnets"] = subnets
    return asn


def dump_networks(networks):
    """dump networks object to json out"""
    pass


if __name__ == "__main__":
    networks = main()


def again():
    main()
