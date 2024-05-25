# Domain Enumeration Tool

This Python script is a domain enumeration tool that gathers information about a domain including its IP address, subdomains, and registered owner. Additionally, it runs several other tools to provide a comprehensive enumeration report.

## Features

- Retrieves IP address of the domain.
- Fetches subdomains using crt.sh.
- Retrieves registered owner information using whois.
- Runs additional tools like Naabu, Shuffledns, Puredns, Sudomy, Cero, and Crtndstry for further enumeration.
- Simple and easy-to-use command-line interface.

## Prerequisites

- Python 3 installed on your system.
- Required Python packages (`requests`, `whois`).
- Additional tools like Naabu, Shuffledns, Puredns, Sudomy, Cero, and Crtndstry installed and available in your system's PATH.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/zkeebl3/DomainScrutinizer.git
