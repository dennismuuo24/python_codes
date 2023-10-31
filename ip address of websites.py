import socket

def get_public_ip_addresses(domain):
    # Get address information for the domain
    addr_info = socket.getaddrinfo(domain, None)

    # Extract public IP addresses from address information
    public_ips = set()
    for addr in addr_info:
        ip = addr[4][0]
        if not ip.startswith("127.") and not ip.startswith("::1"):
            public_ips.add(ip)

    return public_ips

domain = "hello.com"  # Replace with the domain you want to retrieve IP addresses for
public_ips = get_public_ip_addresses(domain)

print(f"Public IP addresses for {domain}:")
for ip in public_ips:
    print(ip)