import socket
import requests
import whois
import subprocess
import json

def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return None

def get_subdomains(domain):
    subdomains = []
    url = f"https://crt.sh/?q=%.{domain}&output=json"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for entry in data:
                name_value = entry['name_value']
                subdomain_list = name_value.split('\n')
                subdomains.extend(subdomain_list)
            subdomains = list(set(subdomains))  # Remove duplicates
    except requests.RequestException as e:
        print(f"Error fetching subdomains: {e}")
    return subdomains

def get_registered_owner(domain):
    try:
        whois_info = whois.whois(domain)
        return whois_info
    except Exception as e:
        print(f"Error fetching whois information: {e}")
        return None

def run_command(command):
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        return result.stdout
    except Exception as e:
        return str(e)

def run_naabu(domain):
    return run_command(f"naabu -host {domain}")

def run_shuffledns(domain):
    return run_command(f"shuffledns -d {domain}")

def run_puredns(domain):
    return run_command(f"puredns resolve {domain}")

def run_sudomy(domain):
    return run_command(f"sudomy -d {domain}")

def run_cero(domain):
    return run_command(f"cero -d {domain}")

def run_crtndstry(domain):
    return run_command(f"crtndstry {domain}")

def domain_enumeration(domain):
    print(f"Domain: {domain}")

    ip_address = get_ip_address(domain)
    print(f"IP Address: {ip_address}")

    subdomains = get_subdomains(domain)
    print("Subdomains from crt.sh:")
    for subdomain in subdomains:
        print(f" - {subdomain}")

    owner_info = get_registered_owner(domain)
    if owner_info:
        print(f"\nRegistered Owner Information:")
        print(f" - Name: {owner_info.name}")
        print(f" - Registrar: {owner_info.registrar}")
        print(f" - Creation Date: {owner_info.creation_date}")
        print(f" - Expiration Date: {owner_info.expiration_date}")
        print(f" - Emails: {owner_info.emails}")
    else:
        print("\nRegistered Owner: Not found")

    print("\nRunning additional tools:")
    print("\nNaabu:")
    print(run_naabu(domain))
    
    print("\nShuffledns:")
    print(run_shuffledns(domain))
    
    print("\nPuredns:")
    print(run_puredns(domain))
    
    print("\nSudomy:")
    print(run_sudomy(domain))
    
    print("\nCero:")
    print(run_cero(domain))
    
    print("\nCrtndstry:")
    print(run_crtndstry(domain))

if __name__ == "__main__":
    domain = input("Enter the domain: ")
    domain_enumeration(domain)
