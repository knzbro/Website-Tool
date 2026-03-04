#!/usr/bin/env python3
# ============================================
# ALL-IN-ONE WEBSITE TOOLKIT v4.1 PRO
# FIXED - No More NoneType Errors
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
# COLOR CODES
# ============================================
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
PURPLE = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m'
BOLD = '\033[1m'

# ============================================
# ERROR HANDLING DECORATOR
# ============================================
def handle_errors(func):
    """Sab errors handle karne ke liye decorator"""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except AttributeError as e:
            print(f"{RED}❌ Attribute Error: {e}{RESET}")
            print(f"{YELLOW}⚠️ Value None hai, check karo{RESET}")
            return None
        except TypeError as e:
            print(f"{RED}❌ Type Error: {e}{RESET}")
            return None
        except Exception as e:
            print(f"{RED}❌ Error: {e}{RESET}")
            return None
    return wrapper

# ============================================
# SAFE GET FUNCTION
# ============================================
def safe_get(obj, attr, default=None):
    """Safe attribute access - NoneType error nahi aayega"""
    try:
        if obj is None:
            return default
        value = getattr(obj, attr, default)
        if value is None:
            return default
        return value
    except:
        return default

def safe_call(func, *args, default=None, **kwargs):
    """Safe function call"""
    try:
        result = func(*args, **kwargs)
        if result is None:
            return default
        return result
    except:
        return default

# ============================================
# INTRO ANIMATION
# ============================================
def show_intro():
    """Safe intro animation"""
    try:
        os.system('clear')
        print(f"{PURPLE}{BOLD}")
        print("╔══════════════════════════════════════════════╗")
        print("║     WEBSITE TOOLKIT PRO v4.1                ║")
        print("║     ⚡ MDF LEGENDS - KASHIF BHAI ⚡         ║")
        print("╚══════════════════════════════════════════════╝")
        print(f"{RESET}")
        time.sleep(1)
    except:
        pass

# ============================================
# STORAGE MANAGER - FIXED
# ============================================
class StorageManager:
    """Storage handle karne ke liye - No NoneType Errors"""
    
    def __init__(self):
        self.storage_paths = []
        self.working_path = None
        self.find_all_storage()
        
    def find_all_storage(self):
        """Saari locations check karo"""
        possible_paths = [
            '/sdcard/WebsiteResults',
            '/storage/emulated/0/WebsiteResults',
            './results',
            os.path.expanduser('~/results'),
            '/sdcard/Download/WebsiteResults'
        ]
        
        print(f"\n{BLUE}[*] Checking storage...{RESET}")
        
        for path in possible_paths:
            try:
                if path is None:
                    continue
                os.makedirs(path, exist_ok=True)
                test_file = os.path.join(path, 'test.txt')
                with open(test_file, 'w') as f:
                    f.write('test')
                os.remove(test_file)
                
                self.storage_paths.append(path)
                print(f"{GREEN}✅ {path}{RESET}")
                
                if self.working_path is None:
                    self.working_path = path
                    
            except Exception as e:
                print(f"{RED}❌ {path}{RESET}")
        
        if self.working_path is None:
            self.working_path = './results'
            os.makedirs(self.working_path, exist_ok=True)
            print(f"{YELLOW}⚠️ Using: {self.working_path}{RESET}")
    
    @handle_errors
    def save_file(self, content, filename, filetype='text'):
        """File save karo - No NoneType Errors"""
        
        if content is None:
            print(f"{RED}❌ Content is None, cannot save{RESET}")
            return False
        
        if filename is None:
            filename = 'unknown.txt'
        
        main_path = os.path.join(self.working_path, filename)
        
        try:
            with open(main_path, 'w', encoding='utf-8') as f:
                if filetype == 'json':
                    if content is not None:
                        json.dump(content, f, indent=4)
                    else:
                        f.write("{}")
                else:
                    if content is not None:
                        f.write(str(content))
                    else:
                        f.write("")
            print(f"{GREEN}✅ Saved: {main_path}{RESET}")
            return True
        except Exception as e:
            print(f"{RED}❌ Save failed: {e}{RESET}")
            return False

# ============================================
# WEBSITE TOOLKIT CLASS - FIXED
# ============================================
class WebsiteToolkit:
    def __init__(self):
        show_intro()
        self.url = ""
        self.base_url = ""
        self.session = None
        self.storage = None
        self.init_session()
        self.init_storage()
        self.set_target()
    
    @handle_errors
    def init_session(self):
        """Session initialize karo"""
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        })
        self.session.timeout = 10
    
    @handle_errors
    def init_storage(self):
        """Storage initialize karo"""
        self.storage = StorageManager()
    
    @handle_errors
    def set_target(self):
        """Target URL set karo"""
        try:
            url = input(f"{CYAN}Enter Website URL: {RESET}").strip()
            if url:
                if not url.startswith(('http://', 'https://')):
                    url = 'https://' + url
                self.url = url
                parsed = urllib.parse.urlparse(url)
                self.base_url = safe_get(parsed, 'netloc', 'unknown.com')
                print(f"{GREEN}✅ Target: {self.url}{RESET}")
            else:
                print(f"{YELLOW}⚠️ URL not set{RESET}")
        except Exception as e:
            print(f"{RED}❌ Error: {e}{RESET}")
    
    @handle_errors
    def safe_request(self, url=None):
        """Safe request function"""
        if url is None:
            url = self.url
        
        if not url:
            print(f"{RED}❌ No URL provided{RESET}")
            return None
        
        try:
            response = self.session.get(url, timeout=10)
            return response
        except requests.exceptions.Timeout:
            print(f"{RED}❌ Timeout error{RESET}")
            return None
        except requests.exceptions.ConnectionError:
            print(f"{RED}❌ Connection error{RESET}")
            return None
        except Exception as e:
            print(f"{RED}❌ Request error: {e}{RESET}")
            return None
    
    @handle_errors
    def get_soup(self, html=None):
        """Safe soup function"""
        if html is None:
            response = self.safe_request()
            if response is None:
                return None
            html = safe_get(response, 'text', '')
        
        if html:
            return BeautifulSoup(html, 'html.parser')
        return None
    
    # ============================================
    # FEATURE 1: WEBSITE INFO - FIXED
    # ============================================
    @handle_errors
    def website_info(self):
        """Website info extractor - No NoneType Errors"""
        self.clear_screen()
        print(f"\n{BLUE}[*] Fetching website info...{RESET}")
        
        response = self.safe_request()
        if response is None:
            print(f"{RED}❌ Could not fetch website{RESET}")
            input(f"\n{YELLOW}Press Enter...{RESET}")
            return
        
        # Safe HTML parsing
        soup = None
        try:
            soup = BeautifulSoup(response.text, 'html.parser')
        except:
            pass
        
        # Safe title extraction
        title = "No Title"
        if soup is not None:
            title_tag = soup.find('title')
            if title_tag is not None:
                title = title_tag.string
                if title is None:
                    title = "No Title"
        
        # Safe headers extraction
        server = "Unknown"
        try:
            headers = safe_get(response, 'headers', {})
            if headers:
                server = headers.get('Server', 'Unknown')
                if server is None:
                    server = 'Unknown'
        except:
            pass
        
        info = {
            'url': self.url if self.url else 'Not set',
            'status_code': safe_get(response, 'status_code', 0),
            'server': server,
            'title': title,
            'encoding': safe_get(response, 'encoding', 'Unknown'),
            'timestamp': datetime.now().isoformat()
        }
        
        print(f"\n{GREEN}✅ Website Information:{RESET}")
        print(f"{CYAN}════════════════════════════════════{RESET}")
        for key, value in info.items():
            print(f"{YELLOW}{key.replace('_', ' ').title()}:{RESET} {value}")
        
        # Save file
        if self.base_url:
            filename = f"{self.base_url}_info.json"
            self.storage.save_file(info, filename, 'json')
        else:
            filename = f"unknown_info.json"
            self.storage.save_file(info, filename, 'json')
        
        input(f"\n{YELLOW}Press Enter to continue...{RESET}")
    
    # ============================================
    # FEATURE 2: API FINDER - FIXED
    # ============================================
    @handle_errors
    def find_apis(self):
        """API endpoints find karo"""
        self.clear_screen()
        print(f"\n{BLUE}[*] Searching for API endpoints...{RESET}")
        
        response = self.safe_request()
        if response is None:
            print(f"{RED}❌ Could not fetch website{RESET}")
            input(f"\n{YELLOW}Press Enter...{RESET}")
            return
        
        soup = self.get_soup(response.text)
        if soup is None:
            print(f"{RED}❌ Could not parse HTML{RESET}")
            input(f"\n{YELLOW}Press Enter...{RESET}")
            return
        
        apis = set()
        
        # Find in script tags
        scripts = soup.find_all('script') if soup else []
        for script in scripts:
            script_text = safe_get(script, 'string', '')
            if script_text:
                matches = re.findall(r'["\'](/api/.*?)["\']', str(script_text))
                for match in matches:
                    if match:
                        full_url = urllib.parse.urljoin(self.url, match)
                        apis.add(full_url)
        
        print(f"\n{GREEN}✅ Found {len(apis)} potential APIs:{RESET}")
        for i, api in enumerate(list(apis)[:10], 1):
            print(f"{YELLOW}{i}.{RESET} {api}")
        
        # Save file
        filename = f"{self.base_url}_apis.txt"
        content = "\n".join(list(apis))
        self.storage.save_file(content, filename)
        
        input(f"\n{YELLOW}Press Enter to continue...{RESET}")
    
    # ============================================
    # FEATURE 3: EMAIL EXTRACTOR - FIXED
    # ============================================
    @handle_errors
    def extract_emails(self):
        """Emails extract karo"""
        self.clear_screen()
        print(f"\n{BLUE}[*] Extracting emails...{RESET}")
        
        response = self.safe_request()
        if response is None:
            print(f"{RED}❌ Could not fetch website{RESET}")
            input(f"\n{YELLOW}Press Enter...{RESET}")
            return
        
        # Email pattern
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        text = safe_get(response, 'text', '')
        
        emails = set()
        if text:
            matches = re.findall(email_pattern, text)
            for match in matches:
                if match:
                    emails.add(match)
        
        print(f"\n{GREEN}✅ Found {len(emails)} emails:{RESET}")
        for i, email in enumerate(list(emails)[:10], 1):
            print(f"{YELLOW}{i}.{RESET} {email}")
        
        # Save file
        filename = f"{self.base_url}_emails.txt"
        content = "\n".join(list(emails))
        self.storage.save_file(content, filename)
        
        input(f"\n{YELLOW}Press Enter to continue...{RESET}")
    
    # ============================================
    # FEATURE 4: COPY FILES - FIXED
    # ============================================
    @handle_errors
    def copy_files(self):
        """Files copy karo saari locations mein"""
        self.clear_screen()
        print(f"\n{BLUE}[*] Copying files to all locations...{RESET}")
        
        if self.storage is None or self.storage.working_path is None:
            print(f"{RED}❌ Storage not initialized{RESET}")
            input(f"\n{YELLOW}Press Enter...{RESET}")
            return
        
        try:
            files = []
            if os.path.exists(self.storage.working_path):
                files = os.listdir(self.storage.working_path)
            
            if not files:
                print(f"{YELLOW}⚠️ No files found to copy{RESET}")
                input(f"\n{YELLOW}Press Enter...{RESET}")
                return
            
            print(f"{GREEN}Found {len(files)} files{RESET}")
            
            for file in files:
                source = os.path.join(self.storage.working_path, file)
                if os.path.isfile(source):
                    for dest_path in self.storage.storage_paths:
                        if dest_path != self.storage.working_path:
                            try:
                                dest = os.path.join(dest_path, file)
                                shutil.copy2(source, dest)
                                print(f"{BLUE}📋 Copied to: {dest}{RESET}")
                            except:
                                pass
            
            print(f"{GREEN}✅ Copy complete!{RESET}")
            
        except Exception as e:
            print(f"{RED}❌ Copy error: {e}{RESET}")
        
        input(f"\n{YELLOW}Press Enter to continue...{RESET}")
    
    # ============================================
    # UTILITY FUNCTIONS
    # ============================================
    def clear_screen(self):
        """Screen clear karo"""
        try:
            os.system('clear' if os.name == 'posix' else 'cls')
            self.print_banner()
        except:
            pass
    
    def print_banner(self):
        """Banner print karo"""
        print(f"{PURPLE}{BOLD}")
        print("╔══════════════════════════════════════════════╗")
        print("║     WEBSITE TOOLKIT PRO v4.1                ║")
        print("║     ⚡ MDF LEGENDS - KASHIF BHAI ⚡         ║")
        print("╚══════════════════════════════════════════════╝")
        print(f"{RESET}")
    
    def print_menu(self):
        """Menu print karo"""
        print(f"""
{GREEN}[MAIN MENU]{RESET}
═══════════════════════════════════════════════

{YELLOW}[1]{RESET} 🌐 Website Info Extractor
{YELLOW}[2]{RESET} 🔍 API Endpoint Finder
{YELLOW}[3]{RESET} 📧 Email Extractor
{YELLOW}[4]{RESET} 📋 Copy Files to All Locations
{YELLOW}[5]{RESET} 🚪 Exit

{CYAN}═══════════════════════════════════════════════{RESET}
        """)
    
    # ============================================
    # MAIN LOOP
    # ============================================
    def run(self):
        """Main loop"""
        while True:
            self.clear_screen()
            self.print_menu()
            
            try:
                choice = input(f"{CYAN}Select option (1-5): {RESET}").strip()
                
                if choice == '1':
                    self.website_info()
                elif choice == '2':
                    self.find_apis()
                elif choice == '3':
                    self.extract_emails()
                elif choice == '4':
                    self.copy_files()
                elif choice == '5':
                    print(f"\n{GREEN}Thanks for using MDF Tools!{RESET}")
                    print(f"{PURPLE}⚡ Kashif Bhai - MDF Legends ⚡{RESET}")
                    break
                else:
                    print(f"{RED}Invalid option!{RESET}")
                    time.sleep(1)
                    
            except KeyboardInterrupt:
                print(f"\n\n{YELLOW}Exiting...{RESET}")
                break
            except Exception as e:
                print(f"{RED}Error: {e}{RESET}")
                time.sleep(1)

# ============================================
# MAIN
# ============================================
def main():
    """Main function"""
    try:
        tool = WebsiteToolkit()
        tool.run()
    except Exception as e:
        print(f"{RED}Fatal Error: {e}{RESET}")
        sys.exit(1)

if __name__ == "__main__":
    main()