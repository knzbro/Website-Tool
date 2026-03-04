#!/usr/bin/env python3
# ============================================
# ALL-IN-ONE WEBSITE TOOLKIT v4.0 PRO
# Powered By MDF Legends
# Author: Kashif Bhai
# ============================================

import os
import sys
import json
import time
import requests
import re
import urllib.parse
import shutil
import threading
import random
from bs4 import BeautifulSoup
from datetime import datetime
import subprocess
import signal

# ============================================
# COLOR CODES - PRO EDITION
# ============================================
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
PURPLE = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
BLACK = '\033[90m'
ORANGE = '\033[33m'
PINK = '\033[95m'
BROWN = '\033[33m'
RESET = '\033[0m'
BOLD = '\033[1m'
DIM = '\033[2m'
UNDERLINE = '\033[4m'
BLINK = '\033[5m'
REVERSE = '\033[7m'
HIDDEN = '\033[8m'

# ============================================
# ANIMATION FUNCTIONS - PRO LEVEL
# ============================================

def clear_screen():
    """Screen clear with effect"""
    os.system('clear' if os.name == 'posix' else 'cls')

def type_effect(text, speed=0.03, color=WHITE):
    """Typing animation effect"""
    for char in text:
        print(f"{color}{char}{RESET}", end='', flush=True)
        time.sleep(speed)
    print()

def loading_bar(duration=2, message="Loading"):
    """Loading bar animation"""
    print(f"\n{YELLOW}{message}{RESET}")
    for i in range(21):
        time.sleep(duration/20)
        bar = "█" * i + "░" * (20 - i)
        percentage = i * 5
        print(f"\r{CYAN}[{bar}]{RESET} {WHITE}{percentage}%{RESET}", end='', flush=True)
    print()

def matrix_effect(lines=5):
    """Matrix rain effect"""
    for _ in range(lines):
        line = ''.join(random.choice('01') for _ in range(50))
        print(f"{GREEN}{line}{RESET}")
        time.sleep(0.1)

def spinner_animation(duration=2, message="Processing"):
    """Spinner animation"""
    spin = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        print(f"\r{CYAN}{spin[i % len(spin)]}{RESET} {message}...", end='', flush=True)
        i += 1
        time.sleep(0.1)
    print("\r" + " " * 50, end='\r')

def pulse_effect(text, duration=2):
    """Pulse animation"""
    end_time = time.time() + duration
    while time.time() < end_time:
        for color in [GREEN, YELLOW, RED, BLUE, PURPLE, CYAN]:
            print(f"\r{color}{BOLD}{text}{RESET}", end='', flush=True)
            time.sleep(0.2)
    print()

def star_animation():
    """Star field animation"""
    stars = ['★', '☆', '✧', '✦', '✨']
    for _ in range(10):
        line = ''.join(random.choice(stars) for _ in range(30))
        print(f"{YELLOW}{line}{RESET}")
        time.sleep(0.05)

# ============================================
# INTRO ANIMATION - MDF LEGENDS
# ============================================

def show_pro_intro():
    """PRO Level Intro Animation"""
    clear_screen()
    
    # Matrix effect background
    print(f"{GREEN}")
    matrix_effect(8)
    print(f"{RESET}")
    time.sleep(0.5)
    clear_screen()
    
    # Big MDF Legends Logo
    print(f"{PURPLE}{BOLD}")
    logo = [
        "╔══════════════════════════════════════════════════════════╗",
        "║     ███╗   ███╗██████╗ ███████╗    ██╗     ███████╗     ║",
        "║     ████╗ ████║██╔══██╗██╔════╝    ██║     ██╔════╝     ║",
        "║     ██╔████╔██║██║  ██║█████╗      ██║     █████╗       ║",
        "║     ██║╚██╔╝██║██║  ██║██╔══╝      ██║     ██╔══╝       ║",
        "║     ██║ ╚═╝ ██║██████╔╝██║         ███████╗███████╗     ║",
        "║     ╚═╝     ╚═╝╚═════╝ ╚═╝         ╚══════╝╚══════╝     ║",
        "╚══════════════════════════════════════════════════════════╝"
    ]
    
    for line in logo:
        print(f"{PURPLE}{BOLD}{line:^80}{RESET}")
        time.sleep(0.1)
    
    time.sleep(0.5)
    
    # Flash effect
    for _ in range(3):
        print(f"\r{YELLOW}{BOLD}⚡ MDF LEGENDS ⚡{RESET}", end='', flush=True)
        time.sleep(0.2)
        print(f"\r{PURPLE}{BOLD}⚡ MDF LEGENDS ⚡{RESET}", end='', flush=True)
        time.sleep(0.2)
    print()
    
    time.sleep(0.5)
    clear_screen()
    
    # Author credit with typing effect
    print(f"\n\n{CYAN}{BOLD}{'═' * 60}{RESET}")
    type_effect("                      PRESENTS", 0.05, YELLOW)
    print(f"{CYAN}{BOLD}{'═' * 60}{RESET}")
    
    time.sleep(0.5)
    
    # Tool name animation
    print(f"\n\n")
    pulse_effect("   WEBSITE TOOLKIT PRO", 3)
    
    time.sleep(0.5)
    
    # Author box
    print(f"\n\n{WHITE}{BOLD}╔══════════════════════════════════════════════╗{RESET}")
    time.sleep(0.2)
    print(f"{WHITE}{BOLD}║{RESET}  {GREEN}CREATED BY:{RESET} {YELLOW}{BOLD}KASHIF BHAI{WHITE}{BOLD}                    ║{RESET}")
    time.sleep(0.2)
    print(f"{WHITE}{BOLD}║{RESET}  {GREEN}TEAM:{RESET} {PURPLE}{BOLD}MDF LEGENDS{WHITE}{BOLD}                      ║{RESET}")
    time.sleep(0.2)
    print(f"{WHITE}{BOLD}║{RESET}  {GREEN}VERSION:{RESET} {CYAN}{BOLD}4.0 PRO{WHITE}{BOLD}                        ║{RESET}")
    time.sleep(0.2)
    print(f"{WHITE}{BOLD}║{RESET}  {GREEN}POWERED BY:{RESET} {BLUE}{BOLD}MDF LEGENDS TEAM{WHITE}{BOLD}            ║{RESET}")
    time.sleep(0.2)
    print(f"{WHITE}{BOLD}╚══════════════════════════════════════════════╝{RESET}")
    
    time.sleep(1)
    
    # Loading animation
    print(f"\n")
    loading_bar(3, "Initializing Toolkit")
    
    # Star animation
    print(f"\n")
    star_animation()
    
    # Final tagline
    clear_screen()
    print(f"\n\n{BLUE}{BOLD}")
    print("╔══════════════════════════════════════════════════════════╗")
    print("║     ALL-IN-ONE WEBSITE TOOLKIT PRO v4.0                ║")
    print("║     ⚡ MDF LEGENDS - KASHIF BHAI ⚡                     ║")
    print("╚══════════════════════════════════════════════════════════╝")
    print(f"{RESET}")
    time.sleep(1)

# ============================================
# STORAGE MANAGER - FIXED VERSION
# ============================================
class StorageManager:
    """Storage handle karne ke liye"""
    
    def __init__(self):
        self.storage_paths = []
        self.working_path = None
        self.find_all_storage()
        
    def find_all_storage(self):
        """Saare possible storage locations dhundho"""
        
        # Possible storage locations
        possible_paths = [
            '/sdcard/WebsiteResults',
            '/storage/emulated/0/WebsiteResults',
            '/data/media/0/WebsiteResults',
            './results',
            f"{os.path.expanduser('~')}/storage/shared/WebsiteResults",
            f"{os.path.expanduser('~')}/results",
            '/sdcard/Download/WebsiteResults',
            '/storage/emulated/0/Download/WebsiteResults'
        ]
        
        print(f"\n{BLUE}[*] Checking storage locations...{RESET}")
        
        for path in possible_paths:
            try:
                os.makedirs(path, exist_ok=True)
                test_file = os.path.join(path, 'test.txt')
                with open(test_file, 'w') as f:
                    f.write('test')
                os.remove(test_file)
                
                self.storage_paths.append(path)
                print(f"{GREEN}✅ Writable: {path}{RESET}")
                
                if not self.working_path:
                    self.working_path = path
                    
            except:
                print(f"{RED}❌ Not writable: {path}{RESET}")
        
        if not self.working_path:
            self.working_path = './results'
            os.makedirs(self.working_path, exist_ok=True)
            print(f"{YELLOW}⚠️ Using local: {self.working_path}{RESET}")
    
    def save_file(self, content, filename, filetype='text'):
        """File save karo with multiple options"""
        
        # Pehle working path mein save karo
        main_path = os.path.join(self.working_path, filename)
        
        try:
            with open(main_path, 'w', encoding='utf-8') as f:
                if filetype == 'json':
                    json.dump(content, f, indent=4)
                else:
                    f.write(content)
            print(f"{GREEN}✅ Saved: {main_path}{RESET}")
        except:
            print(f"{RED}❌ Failed to save: {main_path}{RESET}")
            return False
        
        # Copy to other locations
        self.copy_to_all_locations(main_path, filename)
        
        return True
    
    def copy_to_all_locations(self, source_path, filename):
        """File ko saari locations mein copy karo"""
        for path in self.storage_paths:
            if path != self.working_path:
                try:
                    dest = os.path.join(path, filename)
                    shutil.copy2(source_path, dest)
                    print(f"{BLUE}📋 Copied to: {dest}{RESET}")
                except:
                    pass

# ============================================
# WEBSITE TOOLKIT CLASS
# ============================================
class WebsiteToolkit:
    def __init__(self):
        # Show intro
        show_pro_intro()
        
        self.url = ""
        self.base_url = ""
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
        })
        
        # Initialize storage
        with spinner_animation(2, "Setting up storage"):
            self.storage = StorageManager()
        
        self.set_target()
    
    def set_target(self):
        """Target URL set karo"""
        print(f"\n{YELLOW}════════════════════════════════════{RESET}")
        self.url = input(f"{CYAN}Enter Website URL: {RESET}").strip()
        
        if self.url:
            if not self.url.startswith('http'):
                self.url = 'https://' + self.url
            self.base_url = urllib.parse.urlparse(self.url).netloc
            print(f"{GREEN}✅ Target set to: {self.url}{RESET}")
    
    def print_banner(self):
        """Menu banner"""
        clear_screen()
        print(f"{BLUE}{BOLD}")
        print("╔══════════════════════════════════════════════════════════╗")
        print("║     WEBSITE TOOLKIT PRO v4.0                            ║")
        print("║     ⚡ MDF LEGENDS - KASHIF BHAI ⚡                     ║")
        print("╠══════════════════════════════════════════════════════════╣")
        print(f"║  Target: {self.url[:50]:<50} ║")
        print("╚══════════════════════════════════════════════════════════╝")
        print(f"{RESET}")
    
    def print_menu(self):
        """Main menu"""
        print(f"""
{GREEN}[MAIN MENU]{RESET}
═══════════════════════════════════════════════════════════

{YELLOW}[01]{RESET} 🌐 Website Info Extractor
{YELLOW}[02]{RESET} 🔍 API Endpoint Finder
{YELLOW}[03]{RESET} 📄 HTML/CSS/JS Extractor
{YELLOW}[04]{RESET} 🔗 All Links Extractor
{YELLOW}[05]{RESET} 📸 Images Extractor
{YELLOW}[06]{RESET} 📝 Forms Extractor
{YELLOW}[07]{RESET} 🔑 Hidden Elements Finder
{YELLOW}[08]{RESET} 📊 Technology Detector
{YELLOW}[09]{RESET} 🔒 Security Headers Check
{YELLOW}[10]{RESET} 🌍 Subdomain Finder
{YELLOW}[11]{RESET} 📁 Directory Scanner
{YELLOW}[12]{RESET} 💾 Website Downloader
{YELLOW}[13]{RESET} 🔎 Parameter Finder
{YELLOW}[14]{RESET} 📧 Email Extractor
{YELLOW}[15]{RESET} 🔢 Phone Number Extractor
{YELLOW}[16]{RESET} 📍 Social Media Links
{YELLOW}[17]{RESET} ⏱️  Response Time Check
{YELLOW}[18]{RESET} 📦 All-in-One Scan
{YELLOW}[19]{RESET} 📋 Copy Files to All Locations
{YELLOW}[20]{RESET} 🚪 Exit

{CYAN}═══════════════════════════════════════════════════════════{RESET}
        """)
    
    def copy_files_to_all(self):
        """Saari files copy karo"""
        print(f"\n{BLUE}[*] Copying files to all locations...{RESET}")
        
        files = []
        for file in os.listdir(self.storage.working_path):
            if os.path.isfile(os.path.join(self.storage.working_path, file)):
                files.append(file)
        
        if not files:
            print(f"{RED}❌ No files found to copy{RESET}")
            return
        
        print(f"{GREEN}Found {len(files)} files{RESET}")
        
        for file in files:
            source = os.path.join(self.storage.working_path, file)
            self.storage.copy_to_all_locations(source, file)
        
        print(f"{GREEN}✅ Copy complete!{RESET}")
        input(f"\n{YELLOW}Press Enter to continue...{RESET}")
    
    def website_info(self):
        """Website info extractor"""
        self.print_banner()
        print(f"\n{BLUE}[*] Fetching website info...{RESET}")
        
        try:
            with spinner_animation(2, "Fetching data"):
                response = self.session.get(self.url, timeout=10)
                soup = BeautifulSoup(response.text, 'html.parser')
            
            info = {
                'url': self.url,
                'status_code': response.status_code,
                'server': response.headers.get('Server', 'Unknown'),
                'title': soup.title.string if soup.title else 'No Title',
                'encoding': response.encoding,
                'timestamp': datetime.now().isoformat()
            }
            
            filename = f"{self.base_url}_info.json"
            self.storage.save_file(info, filename, 'json')
            
        except Exception as e:
            print(f"{RED}❌ Error: {e}{RESET}")
        
        input(f"\n{YELLOW}Press Enter to continue...{RESET}")
    
    def run(self):
        """Main loop"""
        while True:
            self.print_banner()
            self.print_menu()
            
            choice = input(f"{CYAN}Select option (1-20): {RESET}")
            
            if choice == '1':
                self.website_info()
            elif choice == '2':
                print(f"{YELLOW}Coming soon...{RESET}")
                time.sleep(1)
            elif choice == '19':
                self.copy_files_to_all()
            elif choice == '20':
                self.exit_animation()
                break
            else:
                print(f"{RED}Invalid option!{RESET}")
                time.sleep(1)
    
    def exit_animation(self):
        """Exit with style"""
        clear_screen()
        print(f"\n\n{PURPLE}{BOLD}")
        print("╔════════════════════════════════════╗")
        print("║     THANKS FOR USING MDF TOOLS    ║")
        print("║        ⚡ KASHIF BHAI ⚡          ║")
        print("║        MDF LEGENDS PROUD          ║")
        print("╚════════════════════════════════════╝")
        print(f"{RESET}")
        
        time.sleep(1)
        print(f"\n{GREEN}Exiting...{RESET}")
        time.sleep(1)

# ============================================
# MAIN
# ============================================
def main():
    """Main function"""
    try:
        # Handle Ctrl+C
        def signal_handler(sig, frame):
            print(f"\n\n{YELLOW}Exiting...{RESET}")
            sys.exit(0)
        
        signal.signal(signal.SIGINT, signal_handler)
        
        # Run toolkit
        tool = WebsiteToolkit()
        tool.run()
        
    except Exception as e:
        print(f"{RED}Error: {e}{RESET}")
        sys.exit(1)

if __name__ == "__main__":
    main()