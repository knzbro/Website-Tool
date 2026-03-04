#!/usr/bin/env python3
# ============================================
# ALL-IN-ONE WEBSITE TOOLKIT v2.0
# Terminal Based - Educational Purpose
# Features: Info Extractor, Scraper, API Finder
# ============================================

import os
import sys
import json
import time
import requests
import re
import urllib.parse
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import threading
from concurrent.futures import ThreadPoolExecutor
import socket
import ssl
from datetime import datetime
import hashlib

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
# MAIN CLASS
# ============================================
class WebsiteToolkit:
    def __init__(self):
        self.url = ""
        self.base_url = ""
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
        })
        self.results_dir = "results"
        self.create_results_dir()
        
    def create_results_dir(self):
        """Results folder banao"""
        if not os.path.exists(self.results_dir):
            os.makedirs(self.results_dir)
            
    def clear_screen(self):
        """Screen clear karo"""
        os.system('clear' if os.name == 'posix' else 'cls')
        
    def print_banner(self):
        """Banner dikhao"""
        self.clear_screen()
        print(f"""{CYAN}{BOLD}
╔══════════════════════════════════════════════════════════╗
║     ALL-IN-ONE WEBSITE TOOLKIT v2.0                     ║
║     Terminal Based - Educational Purpose                 ║
║     [ Info Extractor | Scraper | API Finder | More ]    ║
╚══════════════════════════════════════════════════════════╝{RESET}
        """)
        
    def print_menu(self):
        """Menu dikhao"""
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
{YELLOW}[19]{RESET} 📋 Save All Results
{YELLOW}[20]{RESET} 🚪 Exit

{RED}[*]{RESET} Current Target: {self.url if self.url else 'Not Set'}
═══════════════════════════════════════════════════════════
        """)
        
    def set_target(self):
        """Target URL set karo"""
        if not self.url:
            url = input(f"\n{YELLOW}Enter Website URL: {RESET}")
            if url:
                if not url.startswith('http'):
                    url = 'https://' + url
                self.url = url
                self.base_url = urlparse(url).netloc
                print(f"{GREEN}✅ Target set to: {self.url}{RESET}")
                time.sleep(1)
                
    # ============================================
    # FEATURE 1: WEBSITE INFO EXTRACTOR
    # ============================================
    def website_info(self):
        """Website ki basic info"""
        self.set_target()
        print(f"\n{BLUE}[*] Fetching website info...{RESET}")
        
        try:
            start = time.time()
            response = self.session.get(self.url, timeout=10)
            end = time.time()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            info = {
                'url': self.url,
                'status_code': response.status_code,
                'response_time': f"{(end-start)*1000:.2f}ms",
                'page_size': f"{len(response.content)/1024:.2f}KB",
                'server': response.headers.get('Server', 'Unknown'),
                'content_type': response.headers.get('Content-Type', 'Unknown'),
                'title': soup.title.string if soup.title else 'No Title',
                'encoding': response.encoding,
                'cookies': len(response.cookies),
                'headers': dict(response.headers)
            }
            
            print(f"\n{GREEN}✅ Website Information:{RESET}")
            print(f"{CYAN}════════════════════════════════════{RESET}")
            for key, value in info.items():
                if key != 'headers':
                    print(f"{YELLOW}{key.replace('_', ' ').title()}:{RESET} {value}")
            
            # Save to file
            filename = f"{self.results_dir}/{self.base_url}_info.json"
            with open(filename, 'w') as f:
                json.dump(info, f, indent=4)
            print(f"\n{GREEN}✅ Info saved to: {filename}{RESET}")
            
        except Exception as e:
            print(f"{RED}❌ Error: {e}{RESET}")
            
        input(f"\n{YELLOW}Press Enter to continue...{RESET}")
        
    # ============================================
    # FEATURE 2: API ENDPOINT FINDER
    # ============================================
    def find_apis(self):
        """API endpoints find karo"""
        self.set_target()
        print(f"\n{BLUE}[*] Searching for API endpoints...{RESET}")
        
        try:
            response = self.session.get(self.url)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Common API patterns
            api_patterns = [
                r'https?://[^"\']*?api[^"\']*',
                r'https?://[^"\']*?/v\d+/[^"\']*',
                r'https?://[^"\']*?/graphql[^"\']*',
                r'https?://[^"\']*?/rest[^"\']*',
                r'https?://[^"\']*?/service[^"\']*',
                r'["\'](/api/.*?)["\']',
                r'["\'](/v\d/.*?)["\']',
                r'["\'](/graphql.*?)["\']',
                r'["\'](/rest.*?)["\']',
            ]
            
            apis = set()
            
            # Find in script tags
            for script in soup.find_all('script'):
                if script.string:
                    for pattern in api_patterns:
                        matches = re.findall(pattern, str(script.string))
                        for match in matches:
                            if match.startswith('/'):
                                match = urljoin(self.url, match)
                            apis.add(match)
            
            # Find in all attributes
            for tag in soup.find_all():
                for attr in ['src', 'href', 'data-api', 'action']:
                    value = tag.get(attr)
                    if value and ('api' in value.lower() or 'v1' in value or 'v2' in value):
                        if value.startswith('/'):
                            value = urljoin(self.url, value)
                        apis.add(value)
            
            print(f"\n{GREEN}✅ Found {len(apis)} potential API endpoints:{RESET}")
            print(f"{CYAN}════════════════════════════════════{RESET}")
            
            for i, api in enumerate(sorted(apis), 1):
                print(f"{YELLOW}{i}.{RESET} {api}")
                
                # Test if endpoint is working
                try:
                    test = self.session.get(api, timeout=3)
                    status = f"{GREEN}[{test.status_code}]{RESET}"
                except:
                    status = f"{RED}[Timeout]{RESET}"
                print(f"   Status: {status}")
            
            # Save to file
            filename = f"{self.results_dir}/{self.base_url}_apis.txt"
            with open(filename, 'w') as f:
                for api in sorted(apis):
                    f.write(f"{api}\n")
            print(f"\n{GREEN}✅ APIs saved to: {filename}{RESET}")
            
        except Exception as e:
            print(f"{RED}❌ Error: {e}{RESET}")
            
        input(f"\n{YELLOW}Press Enter to continue...{RESET}")
        
    # ============================================
    # FEATURE 3: HTML/CSS/JS EXTRACTOR
    # ============================================
    def extract_code(self):
        """HTML, CSS, JS extract karo"""
        self.set_target()
        print(f"\n{BLUE}[*] Extracting HTML, CSS, JS...{RESET}")
        
        try:
            response = self.session.get(self.url)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Save HTML
            html_file = f"{self.results_dir}/{self.base_url}_page.html"
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(soup.prettify())
            print(f"{GREEN}✅ HTML saved: {html_file}{RESET}")
            
            # Extract CSS
            css_files = []
            css_content = []
            
            # External CSS
            for link in soup.find_all('link', rel='stylesheet'):
                href = link.get('href')
                if href:
                    if href.startswith('/'):
                        href = urljoin(self.url, href)
                    css_files.append(href)
                    
            # Inline CSS
            for style in soup.find_all('style'):
                if style.string:
                    css_content.append(style.string)
            
            # Download external CSS
            if css_files:
                css_dir = f"{self.results_dir}/{self.base_url}_css"
                os.makedirs(css_dir, exist_ok=True)
                
                for i, css_url in enumerate(css_files[:10]):  # Limit to 10 files
                    try:
                        css_resp = self.session.get(css_url, timeout=5)
                        filename = f"{css_dir}/style_{i+1}.css"
                        with open(filename, 'w', encoding='utf-8') as f:
                            f.write(css_resp.text)
                        print(f"{GREEN}  ✓ CSS downloaded: {filename}{RESET}")
                    except:
                        print(f"{RED}  ✗ Failed: {css_url}{RESET}")
            
            # Save inline CSS
            if css_content:
                css_file = f"{self.results_dir}/{self.base_url}_inline.css"
                with open(css_file, 'w', encoding='utf-8') as f:
                    f.write('\n\n'.join(css_content))
                print(f"{GREEN}✅ Inline CSS saved: {css_file}{RESET}")
            
            # Extract JS
            js_files = []
            js_content = []
            
            for script in soup.find_all('script'):
                src = script.get('src')
                if src:
                    if src.startswith('/'):
                        src = urljoin(self.url, src)
                    js_files.append(src)
                elif script.string:
                    js_content.append(script.string)
            
            # Download external JS
            if js_files:
                js_dir = f"{self.results_dir}/{self.base_url}_js"
                os.makedirs(js_dir, exist_ok=True)
                
                for i, js_url in enumerate(js_files[:10]):  # Limit to 10 files
                    try:
                        js_resp = self.session.get(js_url, timeout=5)
                        filename = f"{js_dir}/script_{i+1}.js"
                        with open(filename, 'w', encoding='utf-8') as f:
                            f.write(js_resp.text)
                        print(f"{GREEN}  ✓ JS downloaded: {filename}{RESET}")
                    except:
                        print(f"{RED}  ✗ Failed: {js_url}{RESET}")
            
            # Save inline JS
            if js_content:
                js_file = f"{self.results_dir}/{self.base_url}_inline.js"
                with open(js_file, 'w', encoding='utf-8') as f:
                    f.write('\n\n'.join(js_content))
                print(f"{GREEN}✅ Inline JS saved: {js_file}{RESET}")
            
            print(f"\n{GREEN}✅ Extraction complete! Files saved in 'results' folder{RESET}")
            
        except Exception as e:
            print(f"{RED}❌ Error: {e}{RESET}")
            
        input(f"\n{YELLOW}Press Enter to continue...{RESET}")
        
    # ============================================
    # FEATURE 4: ALL LINKS EXTRACTOR
    # ============================================
    def extract_links(self):
        """Saare links extract karo"""
        self.set_target()
        print(f"\n{BLUE}[*] Extracting all links...{RESET}")
        
        try:
            response = self.session.get(self.url)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            links = {
                'internal': set(),
                'external': set(),
                'images': set(),
                'css': set(),
                'js': set(),
                'media': set()
            }
            
            for tag in soup.find_all(['a', 'link', 'script', 'img', 'video', 'audio']):
                attrs = {
                    'a': 'href',
                    'link': 'href',
                    'script': 'src',
                    'img': 'src',
                    'video': 'src',
                    'audio': 'src'
                }
                
                if tag.name in attrs:
                    attr = attrs[tag.name]
                    link = tag.get(attr)
                    
                    if link and not link.startswith('#') and not link.startswith('mailto:'):
                        if link.startswith('/'):
                            full_url = urljoin(self.url, link)
                        elif link.startswith('http'):
                            full_url = link
                        else:
                            full_url = urljoin(self.url, link)
                        
                        if self.base_url in full_url:
                            if tag.name == 'img':
                                links['images'].add(full_url)
                            elif tag.name == 'link' and 'stylesheet' in tag.get('rel', []):
                                links['css'].add(full_url)
                            elif tag.name == 'script':
                                links['js'].add(full_url)
                            elif tag.name in ['video', 'audio']:
                                links['media'].add(full_url)
                            else:
                                links['internal'].add(full_url)
                        else:
                            if tag.name == 'a':
                                links['external'].add(full_url)
            
            print(f"\n{GREEN}✅ Links found:{RESET}")
            print(f"{CYAN}════════════════════════════════════{RESET}")
            print(f"{YELLOW}Internal Links:{RESET} {len(links['internal'])}")
            print(f"{YELLOW}External Links:{RESET} {len(links['external'])}")
            print(f"{YELLOW}Images:{RESET} {len(links['images'])}")
            print(f"{YELLOW}CSS Files:{RESET} {len(links['css'])}")
            print(f"{YELLOW}JS Files:{RESET} {len(links['js'])}")
            print(f"{YELLOW}Media Files:{RESET} {len(links['media'])}")
            
            # Save to files
            for key, urls in links.items():
                if urls:
                    filename = f"{self.results_dir}/{self.base_url}_{key}.txt"
                    with open(filename, 'w') as f:
                        for url in sorted(urls):
                            f.write(f"{url}\n")
                    print(f"{GREEN}✅ {key} links saved to: {filename}{RESET}")
            
        except Exception as e:
            print(f"{RED}❌ Error: {e}{RESET}")
            
        input(f"\n{YELLOW}Press Enter to continue...{RESET}")
        
    # ============================================
    # FEATURE 5: IMAGES EXTRACTOR
    # ============================================
    def extract_images(self):
        """Saari images extract karo"""
        self.set_target()
        print(f"\n{BLUE}[*] Extracting images...{RESET}")
        
        try:
            response = self.session.get(self.url)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            images = []
            for img in soup.find_all('img'):
                src = img.get('src')
                if src:
                    if src.startswith('/'):
                        src = urljoin(self.url, src)
                    elif not src.startswith('http'):
                        src = urljoin(self.url, src)
                    
                    alt = img.get('alt', 'No alt text')
                    title = img.get('title', 'No title')
                    
                    images.append({
                        'url': src,
                        'alt': alt,
                        'title': title,
                        'width': img.get('width', 'auto'),
                        'height': img.get('height', 'auto')
                    })
            
            print(f"\n{GREEN}✅ Found {len(images)} images:{RESET}")
            print(f"{CYAN}════════════════════════════════════{RESET}")
            
            for i, img in enumerate(images[:20], 1):  # Show first 20
                print(f"{YELLOW}{i}.{RESET} {img['url'][:80]}...")
                print(f"   Alt: {img['alt'][:50]}")
                print()
            
            # Save to file
            filename = f"{self.results_dir}/{self.base_url}_images.json"
            with open(filename, 'w') as f:
                json.dump(images, f, indent=4)
            print(f"{GREEN}✅ Images info saved to: {filename}{RESET}")
            
        except Exception as e:
            print(f"{RED}❌ Error: {e}{RESET}")
            
        input(f"\n{YELLOW}Press Enter to continue...{RESET}")
        
    # ============================================
    # FEATURE 6: FORMS EXTRACTOR
    # ============================================
    def extract_forms(self):
        """Saare forms extract karo"""
        self.set_target()
        print(f"\n{BLUE}[*] Extracting forms...{RESET}")
        
        try:
            response = self.session.get(self.url)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            forms = []
            for form in soup.find_all('form'):
                form_data = {
                    'action': form.get('action', ''),
                    'method': form.get('method', 'get').upper(),
                    'id': form.get('id', ''),
                    'name': form.get('name', ''),
                    'inputs': [],
                    'textarea': [],
                    'selects': []
                }
                
                # Make full URL for action
                if form_data['action'] and form_data['action'].startswith('/'):
                    form_data['action'] = urljoin(self.url, form_data['action'])
                
                # Get all inputs
                for input_tag in form.find_all('input'):
                    input_data = {
                        'type': input_tag.get('type', 'text'),
                        'name': input_tag.get('name', ''),
                        'id': input_tag.get('id', ''),
                        'value': input_tag.get('value', ''),
                        'placeholder': input_tag.get('placeholder', ''),
                        'required': 'required' in input_tag.attrs
                    }
                    form_data['inputs'].append(input_data)
                
                # Get all textareas
                for textarea in form.find_all('textarea'):
                    textarea_data = {
                        'name': textarea.get('name', ''),
                        'id': textarea.get('id', ''),
                        'placeholder': textarea.get('placeholder', ''),
                        'rows': textarea.get('rows', ''),
                        'cols': textarea.get('cols', '')
                    }
                    form_data['textarea'].append(textarea_data)
                
                # Get all selects
                for select in form.find_all('select'):
                    select_data = {
                        'name': select.get('name', ''),
                        'id': select.get('id', ''),
                        'options': []
                    }
                    
                    for option in select.find_all('option'):
                        select_data['options'].append({
                            'value': option.get('value', ''),
                            'text': option.text.strip()
                        })
                    
                    form_data['selects'].append(select_data)
                
                forms.append(form_data)
            
            print(f"\n{GREEN}✅ Found {len(forms)} forms:{RESET}")
            print(f"{CYAN}════════════════════════════════════{RESET}")
            
            for i, form in enumerate(forms, 1):
                print(f"{YELLOW}Form {i}:{RESET}")
                print(f"  Action: {form['action']}")
                print(f"  Method: {form['method']}")
                print(f"  Inputs: {len(form['inputs'])}")
                print()
            
            # Save to file
            filename = f"{self.results_dir}/{self.base_url}_forms.json"
            with open(filename, 'w') as f:
                json.dump(forms, f, indent=4)
            print(f"{GREEN}✅ Forms saved to: {filename}{RESET}")
            
        except Exception as e:
            print(f"{RED}❌ Error: {e}{RESET}")
            
        input(f"\n{YELLOW}Press Enter to continue...{RESET}")
        
    # ============================================
    # FEATURE 7: HIDDEN ELEMENTS FINDER
    # ============================================
    def find_hidden(self):
        """Hidden elements dhundho"""
        self.set_target()
        print(f"\n{BLUE}[*] Searching for hidden elements...{RESET}")
        
        try:
            response = self.session.get(self.url)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            hidden = {
                'hidden_inputs': [],
                'comments': [],
                'meta_tags': [],
                'data_attributes': [],
                'display_none': []
            }
            
            # Hidden inputs
            for input_tag in soup.find_all('input', type='hidden'):
                hidden['hidden_inputs'].append({
                    'name': input_tag.get('name', ''),
                    'value': input_tag.get('value', '')
                })
            
            # HTML comments
            comments = re.findall(r'<!--(.*?)-->', response.text, re.DOTALL)
            hidden['comments'] = [c.strip() for c in comments if c.strip()]
            
            # Meta tags
            for meta in soup.find_all('meta'):
                hidden['meta_tags'].append({
                    'name': meta.get('name', meta.get('property', '')),
                    'content': meta.get('content', '')
                })
            
            # Data attributes
            for tag in soup.find_all(attrs={"data-*": True}):
                for attr in tag.attrs:
                    if attr.startswith('data-'):
                        hidden['data_attributes'].append({
                            'tag': tag.name,
                            'attribute': attr,
                            'value': tag[attr]
                        })
            
            # Display none elements
            for tag in soup.find_all(style=re.compile(r'display:\s*none')):
                hidden['display_none'].append({
                    'tag': tag.name,
                    'id': tag.get('id', ''),
                    'class': tag.get('class', ''),
                    'text': tag.text[:100] + '...' if tag.text else ''
                })
            
            print(f"\n{GREEN}✅ Hidden elements found:{RESET}")
            print(f"{CYAN}════════════════════════════════════{RESET}")
            print(f"{YELLOW}Hidden Inputs:{RESET} {len(hidden['hidden_inputs'])}")
            print(f"{YELLOW}HTML Comments:{RESET} {len(hidden['comments'])}")
            print(f"{YELLOW}Meta Tags:{RESET} {len(hidden['meta_tags'])}")
            print(f"{YELLOW}Data Attributes:{RESET} {len(hidden['data_attributes'])}")
            print(f"{YELLOW}Display None:{RESET} {len(hidden['display_none'])}")
            
            # Show some examples
            if hidden['hidden_inputs']:
                print(f"\n{GREEN}Hidden Input Examples:{RESET}")
                for inp in hidden['hidden_inputs'][:5]:
                    print(f"  • {inp['name']} = {inp['value']}")
            
            if hidden['comments']:
                print(f"\n{GREEN}Comment Examples:{RESET}")
                for comment in hidden['comments'][:3]:
                    print(f"  • {comment[:100]}...")
            
            # Save to file
            filename = f"{self.results_dir}/{self.base_url}_hidden.json"
            with open(filename, 'w') as f:
                json.dump(hidden, f, indent=4)
            print(f"{GREEN}✅ Hidden elements saved to: {filename}{RESET}")
            
        except Exception as e:
            print(f"{RED}❌ Error: {e}{RESET}")
            
        input(f"\n{YELLOW}Press Enter to continue...{RESET}")
        
    # ============================================
    # FEATURE 8: TECHNOLOGY DETECTOR
    # ============================================
    def detect_tech(self):
        """Website technology detect karo"""
        self.set_target()
        print(f"\n{BLUE}[*] Detecting technologies...{RESET}")
        
        try:
            response = self.session.get(self.url)
            headers = response.headers
            html = response.text.lower()
            
            tech = {
                'server': headers.get('Server', 'Unknown'),
                'programming': [],
                'frameworks': [],
                'cms': [],
                'analytics': [],
                'cdn': [],
                'javascript': [],
                'css_frameworks': []
            }
            
            # Server detection
            server = headers.get('Server', '').lower()
            if 'apache' in server:
                tech['server'] = 'Apache'
            elif 'nginx' in server:
                tech['server'] = 'Nginx'
            elif 'iis' in server:
                tech['server'] = 'IIS'
            elif 'cloudflare' in server:
                tech['server'] = 'Cloudflare'
            
            # Programming language
            if 'php' in html or '.php' in html:
                tech['programming'].append('PHP')
            if 'asp.net' in html or '__viewstate' in html:
                tech['programming'].append('ASP.NET')
            if 'django' in html or 'csrfmiddlewaretoken' in html:
                tech['programming'].append('Django (Python)')
            if 'rails' in html or 'csrf-token' in html:
                tech['programming'].append('Ruby on Rails')
            if 'laravel' in html:
                tech['programming'].append('Laravel (PHP)')
            
            # CMS detection
            cms_patterns = {
                'WordPress': ['wp-content', 'wp-includes', 'wordpress'],
                'Joomla': ['joomla', 'com_content', 'com_modules'],
                'Drupal': ['drupal', 'sites/all', 'core/themes'],
                'Magento': ['magento', 'skin/frontend', 'mage/cookies'],
                'Shopify': ['shopify', 'myshopify', 'cdn.shopify'],
                'Wix': ['wix', 'wix.com', 'static.wixstatic']
            }
            
            for cms, patterns in cms_patterns.items():
                if any(p in html for p in patterns):
                    tech['cms'].append(cms)
            
            # Analytics
            analytics_patterns = {
                'Google Analytics': ['google-analytics', 'ga.js', 'analytics.js'],
                'Facebook Pixel': ['facebook.com/tr', 'fbq('],
                'Hotjar': ['hotjar', 'hj('],
                'Mixpanel': ['mixpanel'],
                'Heap': ['heap']
            }
            
            for analytic, patterns in analytics_patterns.items():
                if any(p in html for p in patterns):
                    tech['analytics'].append(analytic)
            
            # CDN
            if 'cloudflare' in html or 'cf-ray' in headers:
                tech['cdn'].append('Cloudflare')
            if 'akamai' in html:
                tech['cdn'].append('Akamai')
            if 'fastly' in html:
                tech['cdn'].append('Fastly')
            if 'cdn' in html:
                tech['cdn'].append('Generic CDN')
            
            # JavaScript libraries
            js_libs = {
                'jQuery': ['jquery', 'jQuery'],
                'React': ['react', 'reactjs'],
                'Vue': ['vue', 'vuejs'],
                'Angular': ['angular', 'ng-'],
                'Bootstrap': ['bootstrap', 'bootstrap.min'],
                'Tailwind': ['tailwind'],
                'Font Awesome': ['font-awesome', 'fontawesome']
            }
            
            for lib, patterns in js_libs.items():
                if any(p in html for p in patterns):
                    tech['javascript'].append(lib)
            
            print(f"\n{GREEN}✅ Technologies detected:{RESET}")
            print(f"{CYAN}════════════════════════════════════{RESET}")
            
            for category, items in tech.items():
                if items:
                    if isinstance(items, list):
                        if items:
                            print(f"{YELLOW}{category.replace('_', ' ').title()}:{RESET}")
                            for item in items:
                                print(f"  • {item}")
                    else:
                        print(f"{YELLOW}{category.replace('_', ' ').title()}:{RESET} {items}")
            
            # Save to file
            filename = f"{self.results_dir}/{self.base_url}_tech.json"
            with open(filename, 'w') as f:
                json.dump(tech, f, indent=4)
            print(f"{GREEN}✅ Tech info saved to: {filename}{RESET}")
            
        except Exception as e:
            print(f"{RED}❌ Error: {e}{RESET}")
            
        input(f"\n{YELLOW}Press Enter to continue...{RESET}")
        
    # ============================================
    # FEATURE 9: SECURITY HEADERS CHECK
    # ============================================
    def security_headers(self):
        """Security headers check karo"""
        self.set_target()
        print(f"\n{BLUE}[*] Checking security headers...{RESET}")
        
        try:
            response = self.session.get(self.url)
            headers = response.headers
            
            security_headers = {
                'Strict-Transport-Security': {'status': False, 'value': '', 'desc': 'Forces HTTPS connection'},
                'Content-Security-Policy': {'status': False, 'value': '', 'desc': 'Prevents XSS attacks'},
                'X-Frame-Options': {'status': False, 'value': '', 'desc': 'Prevents clickjacking'},
                'X-Content-Type-Options': {'status': False, 'value': '', 'desc': 'Prevents MIME sniffing'},
                'X-XSS-Protection': {'status': False, 'value': '', 'desc': 'Enables XSS filter'},
                'Referrer-Policy': {'status': False, 'value': '', 'desc': 'Controls referrer info'},
                'Permissions-Policy': {'status': False, 'value': '', 'desc': 'Controls browser features'},
                'Cache-Control': {'status': False, 'value': '', 'desc': 'Caching policy'},
                'X-Powered-By': {'status': False, 'value': '', 'desc': 'Shows technology (should be hidden)'}
            }
            
            for header in security_headers:
                if header in headers:
                    security_headers[header]['status'] = True
                    security_headers[header]['value'] = headers[header]
            
            print(f"\n{GREEN}✅ Security Headers Analysis:{RESET}")
            print(f"{CYAN}════════════════════════════════════{RESET}")
            
            score = 0
            total = len(security_headers)
            
            for header, info in security_headers.items():
                if info['status']:
                    score += 1
                    print(f"{GREEN}✓{RESET} {header}: {info['value'][:50]}")
                else:
                    print(f"{RED}✗{RESET} {header} - {info['desc']}")
            
            security_score = (score / total) * 100
            print(f"\n{YELLOW}Security Score:{RESET} {security_score:.1f}%")
            
            if security_score < 50:
                print(f"{RED}⚠️ Poor security - needs improvement{RESET}")
            elif security_score < 70:
                print(f"{YELLOW}⚠️ Average security{RESET}")
            else:
                print(f"{GREEN}✅ Good security{RESET}")
            
            # Save to file
            filename = f"{self.results_dir}/{self.base_url}_security.json"
            with open(filename, 'w') as f:
                json.dump(security_headers, f, indent=4)
            print(f"{GREEN}✅ Security headers saved to: {filename}{RESET}")
            
        except Exception as e:
            print(f"{RED}❌ Error: {e}{RESET}")
            
        input(f"\n{YELLOW}Press Enter to continue...{RESET}")
        
    # ============================================
    # FEATURE 10: SUBDOMAIN FINDER
    # ============================================
    def find_subdomains(self):
        """Subdomains dhundho"""
        self.set_target()
        print(f"\n{BLUE}[*] Searching for subdomains...{RESET}")
        
        try:
            domain = self.base_url
            if domain.startswith('www.'):
                domain = domain[4:]
            
            # Common subdomains list
            subdomains = [
                'www', 'mail', 'ftp', 'localhost', 'webmail', 'smtp',
                'pop', 'ns1', 'webdisk', 'ns2', 'cpanel', 'whm',
                'autodiscover', 'autoconfig', 'm', 'imap', 'test',
                'ns', 'blog', 'pop3', 'dev', 'www2', 'admin',
                'forum', 'news', 'vpn', 'ns3', 'mail2', 'new',
                'mysql', 'old', 'lists', 'support', 'mobile',
                'mx', 'static', 'docs', 'beta', 'shop', 'sql',
                'secure', 'demo', 'testing', 'stage', 'staging',
                'api', 'api2', 'api3', 'graphql', 'graph',
                'app', 'app2', 'dashboard', 'portal', 'account',
                'accounts', 'login', 'signup', 'auth', 'sso',
                'cdn', 'static', 'media', 'assets', 'images',
                'download', 'uploads', 'files', 'data', 'backup'
            ]
            
            found = []
            
            print(f"\n{BLUE}[*] Scanning {len(subdomains)} subdomains...{RESET}")
            
            def check_sub(sub):
                url = f"http://{sub}.{domain}"
                try:
                    r = requests.get(url, timeout=2)
                    if r.status_code < 400:
                        found.append(f"{sub}.{domain}")
                        print(f"{GREEN}✅ Found: {sub}.{domain}{RESET}")
                except:
                    pass
            
            # Check with threads
            with ThreadPoolExecutor(max_workers=20) as executor:
                executor.map(check_sub, subdomains)
            
            print(f"\n{GREEN}✅ Found {len(found)} subdomains:{RESET}")
            print(f"{CYAN}════════════════════════════════════{RESET}")
            
            for i, sub in enumerate(sorted(found), 1):
                print(f"{YELLOW}{i}.{RESET} {sub}")
            
            # Save to file
            filename = f"{self.results_dir}/{domain}_subdomains.txt"
            with open(filename, 'w') as f:
                for sub in sorted(found):
                    f.write(f"{sub}\n")
            print(f"{GREEN}✅ Subdomains saved to: {filename}{RESET}")
            
        except Exception as e:
            print(f"{RED}❌ Error: {e}{RESET}")
            
        input(f"\n{YELLOW}Press Enter to continue...{RESET}")
        
    # ============================================
    # FEATURE 11: DIRECTORY SCANNER
    # ============================================
    def scan_directories(self):
        """Common directories scan karo"""
        self.set_target()
        print(f"\n{BLUE}[*] Scanning common directories...{RESET}")
        
        try:
            directories = [
                'admin', 'administrator', 'wp-admin', 'dashboard',
                'login', 'signin', 'register', 'signup',
                'backup', 'backups', 'old', 'temp', 'tmp',
                'uploads', 'upload', 'download', 'downloads',
                'files', 'media', 'images', 'img', 'css', 'js',
                'api', 'v1', 'v2', 'v3', 'rest', 'graphql',
                'test', 'tests', 'testing', 'dev', 'development',
                'stage', 'staging', 'beta', 'alpha',
                'config', 'configuration', 'settings',
                'database', 'db', 'mysql', 'phpmyadmin',
                'logs', 'log', 'error_log', 'debug',
                'private', 'secret', 'hidden', 'internal',
                'user', 'users', 'profile', 'profiles',
                'search', 'results', 'category', 'categories',
                'product', 'products', 'shop', 'store',
                'blog', 'news', 'article', 'articles',
                'page', 'pages', 'content', 'contents',
                'includes', 'inc', 'lib', 'libs', 'library',
                'vendor', 'vendors', 'assets', 'resources',
                'static', 'public', 'pub', 'html', 'htm',
                'php', 'asp', 'aspx', 'jsp', 'cgi-bin'
            ]
            
            found = []
            
            print(f"\n{BLUE}[*] Scanning {len(directories)} directories...{RESET}")
            
            for directory in directories:
                url = f"{self.url.rstrip('/')}/{directory}/"
                try:
                    r = self.session.get(url, timeout=2)
                    if r.status_code == 200:
                        found.append(directory)
                        print(f"{GREEN}✅ Found: {url}{RESET}")
                    elif r.status_code == 403:
                        found.append(f"{directory} (403)")
                        print(f"{YELLOW}🔒 Found (403): {url}{RESET}")
                except:
                    pass
            
            print(f"\n{GREEN}✅ Found {len(found)} directories:{RESET}")
            print(f"{CYAN}════════════════════════════════════{RESET}")
            
            for i, dir_name in enumerate(sorted(found), 1):
                print(f"{YELLOW}{i}.{RESET} {dir_name}")
            
            # Save to file
            filename = f"{self.results_dir}/{self.base_url}_directories.txt"
            with open(filename, 'w') as f:
                for dir_name in sorted(found):
                    f.write(f"{dir_name}\n")
            print(f"{GREEN}✅ Directories saved to: {filename}{RESET}")
            
        except Exception as e:
            print(f"{RED}❌ Error: {e}{RESET}")
            
        input(f"\n{YELLOW}Press Enter to continue...{RESET}")
        
    # ============================================
    # FEATURE 12: WEBSITE DOWNLOADER
    # ============================================
    def download_website(self):
        """Website download karo (HTML only)"""
        self.set_target()
        print(f"\n{BLUE}[*] Downloading website...{RESET}")
        
        try:
            response = self.session.get(self.url)
            
            # Create website folder
            website_dir = f"{self.results_dir}/{self.base_url}_website"
            os.makedirs(website_dir, exist_ok=True)
            
            # Save HTML
            html_file = f"{website_dir}/index.html"
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(response.text)
            print(f"{GREEN}✅ HTML saved: {html_file}{RESET}")
            
            # Parse HTML to find resources
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Download CSS
            css_dir = f"{website_dir}/css"
            os.makedirs(css_dir, exist_ok=True)
            
            for i, link in enumerate(soup.find_all('link', rel='stylesheet')):
                href = link.get('href')
                if href:
                    if href.startswith('/'):
                        css_url = urljoin(self.url, href)
                    else:
                        css_url = href
                    
                    try:
                        css_resp = self.session.get(css_url)
                        css_file = f"{css_dir}/style_{i+1}.css"
                        with open(css_file, 'w', encoding='utf-8') as f:
                            f.write(css_resp.text)
                        print(f"{GREEN}  ✓ CSS downloaded: {css_file}{RESET}")
                    except:
                        print(f"{RED}  ✗ Failed: {css_url}{RESET}")
            
            # Download JS
            js_dir = f"{website_dir}/js"
            os.makedirs(js_dir, exist_ok=True)
            
            for i, script in enumerate(soup.find_all('script', src=True)):
                src = script.get('src')
                if src:
                    if src.startswith('/'):
                        js_url = urljoin(self.url, src)
                    else:
                        js_url = src
                    
                    try:
                        js_resp = self.session.get(js_url)
                        js_file = f"{js_dir}/script_{i+1}.js"
                        with open(js_file, 'w', encoding='utf-8') as f:
                            f.write(js_resp.text)
                        print(f"{GREEN}  ✓ JS downloaded: {js_file}{RESET}")
                    except:
                        print(f"{RED}  ✗ Failed: {js_url}{RESET}")
            
            # Download images
            img_dir = f"{website_dir}/images"
            os.makedirs(img_dir, exist_ok=True)
            
            for i, img in enumerate(soup.find_all('img', src=True)):
                src = img.get('src')
                if src:
                    if src.startswith('/'):
                        img_url = urljoin(self.url, src)
                    else:
                        img_url = src
                    
                    try:
                        img_resp = self.session.get(img_url)
                        ext = os.path.splitext(src)[1] or '.jpg'
                        img_file = f"{img_dir}/image_{i+1}{ext}"
                        with open(img_file, 'wb') as f:
                            f.write(img_resp.content)
                        print(f"{GREEN}  ✓ Image downloaded: {img_file}{RESET}")
                    except:
                        print(f"{RED}  ✗ Failed: {img_url}{RESET}")
            
            print(f"\n{GREEN}✅ Website downloaded to: {website_dir}{RESET}")
            
        except Exception as e:
            print(f"{RED}❌ Error: {e}{RESET}")
            
        input(f"\n{YELLOW}Press Enter to continue...{RESET}")
        
    # ============================================
    # FEATURE 13: PARAMETER FINDER
    # ============================================
    def find_parameters(self):
        """URL parameters dhundho"""
        self.set_target()
        print(f"\n{BLUE}[*] Finding URL parameters...{RESET}")
        
        try:
            response = self.session.get(self.url)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            parameters = {
                'url_params': [],
                'form_params': [],
                'js_params': [],
                'hidden_params': []
            }
            
            # URL parameters
            parsed = urlparse(self.url)
            if parsed.query:
                params = urllib.parse.parse_qs(parsed.query)
                parameters['url_params'] = list(params.keys())
            
            # Form parameters
            for form in soup.find_all('form'):
                method = form.get('method', 'get').lower()
                action = form.get('action', '')
                
                for input_tag in form.find_all(['input', 'textarea', 'select']):
                    name = input_tag.get('name')
                    if name:
                        param_info = {
                            'name': name,
                            'type': input_tag.name,
                            'method': method,
                            'action': action
                        }
                        
                        if input_tag.get('type') == 'hidden':
                            parameters['hidden_params'].append(param_info)
                        else:
                            parameters['form_params'].append(param_info)
            
            # JavaScript parameters
            js_patterns = [
                r'["\']([a-zA-Z0-9_]+)["\']\s*:\s*["\']',
                r'var\s+([a-zA-Z0-9_]+)\s*=',
                r'let\s+([a-zA-Z0-9_]+)\s*=',
                r'const\s+([a-zA-Z0-9_]+)\s*=',
                r'parameters?\s*=\s*{([^}]*)}',
                r'params?\s*=\s*{([^}]*)}'
            ]
            
            for script in soup.find_all('script'):
                if script.string:
                    for pattern in js_patterns:
                        matches = re.findall(pattern, script.string)
                        for match in matches:
                            if len(match) > 2 and match not in parameters['js_params']:
                                parameters['js_params'].append(match)
            
            print(f"\n{GREEN}✅ Parameters found:{RESET}")
            print(f"{CYAN}════════════════════════════════════{RESET}")
            
            for category, params in parameters.items():
                if params:
                    print(f"{YELLOW}{category.replace('_', ' ').title()}:{RESET} {len(params)}")
                    if len(params) > 0:
                        for param in params[:10]:  # Show first 10
                            if isinstance(param, dict):
                                print(f"  • {param['name']} ({param['type']})")
                            else:
                                print(f"  • {param}")
            
            # Save to file
            filename = f"{self.results_dir}/{self.base_url}_parameters.json"
            with open(filename, 'w') as f:
                json.dump(parameters, f, indent=4)
            print(f"{GREEN}✅ Parameters saved to: {filename}{RESET}")
            
        except Exception as e:
            print(f"{RED}❌ Error: {e}{RESET}")
            
        input(f"\n{YELLOW}Press Enter to continue...{RESET}")
        
    # ============================================
    # FEATURE 14: EMAIL EXTRACTOR
    # ============================================
    def extract_emails(self):
        """Emails extract karo"""
        self.set_target()
        print(f"\n{BLUE}[*] Extracting email addresses...{RESET}")
        
        try:
            response = self.session.get(self.url)
            
            # Email pattern
            email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
            emails = re.findall(email_pattern, response.text)
            
            # Remove duplicates and sort
            emails = sorted(set(emails))
            
            print(f"\n{GREEN}✅ Found {len(emails)} emails:{RESET}")
            print(f"{CYAN}════════════════════════════════════{RESET}")
            
            for i, email in enumerate(emails, 1):
                print(f"{YELLOW}{i}.{RESET} {email}")
            
            # Save to file
            filename = f"{self.results_dir}/{self.base_url}_emails.txt"
            with open(filename, 'w') as f:
                for email in emails:
                    f.write(f"{email}\n")
            print(f"{GREEN}✅ Emails saved to: {filename}{RESET}")
            
        except Exception as e:
            print(f"{RED}❌ Error: {e}{RESET}")
            
        input(f"\n{YELLOW}Press Enter to continue...{RESET}")
        
    # ============================================
    # FEATURE 15: PHONE NUMBER EXTRACTOR
    # ============================================
    def extract_phones(self):
        """Phone numbers extract karo"""
        self.set_target()
        print(f"\n{BLUE}[*] Extracting phone numbers...{RESET}")
        
        try:
            response = self.session.get(self.url)
            
            # Phone number patterns
            patterns = [
                r'\+\d{1,3}[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}',
                r'0\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,7}',
                r'\d{3}[-.\s]?\d{3}[-.\s]?\d{4}',
                r'\(\d{3}\)\s*\d{3}[-.\s]?\d{4}'
            ]
            
            phones = []
            for pattern in patterns:
                matches = re.findall(pattern, response.text)
                phones.extend(matches)
            
            # Clean and deduplicate
            phones = sorted(set(phones))
            
            print(f"\n{GREEN}✅ Found {len(phones)} phone numbers:{RESET}")
            print(f"{CYAN}════════════════════════════════════{RESET}")
            
            for i, phone in enumerate(phones, 1):
                print(f"{YELLOW}{i}.{RESET} {phone}")
            
            # Save to file
            filename = f"{self.results_dir}/{self.base_url}_phones.txt"
            with open(filename, 'w') as f:
                for phone in phones:
                    f.write(f"{phone}\n")
            print(f"{GREEN}✅ Phone numbers saved to: {filename}{RESET}")
            
        except Exception as e:
            print(f"{RED}❌ Error: {e}{RESET}")
            
        input(f"\n{YELLOW}Press Enter to continue...{RESET}")
        
    # ============================================
    # FEATURE 16: SOCIAL MEDIA LINKS
    # ============================================
    def find_social(self):
        """Social media links dhundho"""
        self.set_target()
        print(f"\n{BLUE}[*] Finding social media links...{RESET}")
        
        try:
            response = self.session.get(self.url)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            social_patterns = {
                'Facebook': ['facebook.com', 'fb.com', 'fb.me'],
                'Twitter': ['twitter.com', 'x.com', 't.co'],
                'Instagram': ['instagram.com', 'instagr.am'],
                'LinkedIn': ['linkedin.com', 'lnkd.in'],
                'YouTube': ['youtube.com', 'youtu.be'],
                'WhatsApp': ['wa.me', 'whatsapp.com'],
                'Telegram': ['t.me', 'telegram.org'],
                'TikTok': ['tiktok.com'],
                'Snapchat': ['snapchat.com'],
                'Pinterest': ['pinterest.com'],
                'Reddit': ['reddit.com'],
                'GitHub': ['github.com'],
                'Medium': ['medium.com'],
                'Discord': ['discord.gg', 'discord.com']
            }
            
            social_links = {platform: [] for platform in social_patterns}
            
            for tag in soup.find_all(['a', 'link']):
                href = tag.get('href')
                if href:
                    for platform, patterns in social_patterns.items():
                        if any(p in href for p in patterns):
                            social_links[platform].append(href)
            
            print(f"\n{GREEN}✅ Social media links found:{RESET}")
            print(f"{CYAN}════════════════════════════════════{RESET}")
            
            for platform, links in social_links.items():
                if links:
                    print(f"{YELLOW}{platform}:{RESET}")
                    for link in links[:3]:  # Show max 3 per platform
                        print(f"  • {link}")
            
            # Save to file
            filename = f"{self.results_dir}/{self.base_url}_social.json"
            with open(filename, 'w') as f:
                json.dump(social_links, f, indent=4)
            print(f"{GREEN}✅ Social links saved to: {filename}{RESET}")
            
        except Exception as e:
            print(f"{RED}❌ Error: {e}{RESET}")
            
        input(f"\n{YELLOW}Press Enter to continue...{RESET}")
        
    # ============================================
    # FEATURE 17: RESPONSE TIME CHECK
    # ============================================
    def response_time(self):
        """Response time check karo"""
        self.set_target()
        print(f"\n{BLUE}[*] Checking response time...{RESET}")
        
        try:
            times = []
            for i in range(5):  # 5 requests
                start = time.time()
                response = self.session.get(self.url)
                end = time.time()
                
                response_time = (end - start) * 1000
                times.append(response_time)
                
                status = f"{GREEN}✓{RESET}" if response.status_code == 200 else f"{RED}✗{RESET}"
                print(f"{status} Request {i+1}: {response_time:.2f}ms (Status: {response.status_code})")
                
                time.sleep(1)
            
            avg_time = sum(times) / len(times)
            min_time = min(times)
            max_time = max(times)
            
            print(f"\n{GREEN}✅ Response Time Analysis:{RESET}")
            print(f"{CYAN}════════════════════════════════════{RESET}")
            print(f"{YELLOW}Average:{RESET} {avg_time:.2f}ms")
            print(f"{YELLOW}Minimum:{RESET} {min_time:.2f}ms")
            print(f"{YELLOW}Maximum:{RESET} {max_time:.2f}ms")
            
            if avg_time < 500:
                print(f"{GREEN}✅ Very Fast Response{RESET}")
            elif avg_time < 1000:
                print(f"{YELLOW}⚠️ Good Response{RESET}")
            elif avg_time < 2000:
                print(f"{RED}⚠️ Slow Response{RESET}")
            else:
                print(f"{RED}❌ Very Slow Response{RESET}")
            
            # Save to file
            filename = f"{self.results_dir}/{self.base_url}_responsetime.txt"
            with open(filename, 'w') as f:
                f.write(f"Average: {avg_time:.2f}ms\n")
                f.write(f"Minimum: {min_time:.2f}ms\n")
                f.write(f"Maximum: {max_time:.2f}ms\n")
            print(f"{GREEN}✅ Response time saved to: {filename}{RESET}")
            
        except Exception as e:
            print(f"{RED}❌ Error: {e}{RESET}")
            
        input(f"\n{YELLOW}Press Enter to continue...{RESET}")
        
    # ============================================
    # FEATURE 18: ALL-IN-ONE SCAN
    # ============================================
    def all_in_one(self):
        """Sab kuch ek saath scan karo"""
        self.set_target()
        print(f"\n{BLUE}[*] Starting All-in-One Scan...{RESET}")
        print(f"{YELLOW}This will run all scans. Please wait...{RESET}")
        
        start_time = time.time()
        
        scans = [
            ("Website Info", self.website_info_silent),
            ("API Endpoints", self.find_apis_silent),
            ("HTML/CSS/JS", self.extract_code_silent),
            ("Links", self.extract_links_silent),
            ("Images", self.extract_images_silent),
            ("Forms", self.extract_forms_silent),
            ("Hidden Elements", self.find_hidden_silent),
            ("Technology", self.detect_tech_silent),
            ("Security Headers", self.security_headers_silent),
            ("Subdomains", self.find_subdomains_silent),
            ("Directories", self.scan_directories_silent),
            ("Parameters", self.find_parameters_silent),
            ("Emails", self.extract_emails_silent),
            ("Phone Numbers", self.extract_phones_silent),
            ("Social Media", self.find_social_silent),
            ("Response Time", self.response_time_silent)
        ]
        
        total = len(scans)
        for i, (name, func) in enumerate(scans, 1):
            print(f"\n{BLUE}[{i}/{total}]{RESET} Scanning: {name}")
            try:
                func()
                print(f"{GREEN}✓ Completed{RESET}")
            except Exception as e:
                print(f"{RED}✗ Failed: {e}{RESET}")
        
        end_time = time.time()
        total_time = (end_time - start_time) / 60
        
        print(f"\n{GREEN}✅ All-in-One Scan Complete!{RESET}")
        print(f"{YELLOW}Total Time: {total_time:.2f} minutes{RESET}")
        print(f"{YELLOW}Results saved in: {self.results_dir}/{RESET}")
        
        input(f"\n{YELLOW}Press Enter to continue...{RESET}")
    
    # Silent versions for all-in-one
    def website_info_silent(self):
        try:
            response = self.session.get(self.url, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            info = {
                'url': self.url,
                'status': response.status_code,
                'title': soup.title.string if soup.title else 'No Title',
                'server': response.headers.get('Server', 'Unknown')
            }
            filename = f"{self.results_dir}/{self.base_url}_info.json"
            with open(filename, 'w') as f:
                json.dump(info, f)
        except:
            pass
    
    def find_apis_silent(self):
        try:
            response = self.session.get(self.url)
            soup = BeautifulSoup(response.text, 'html.parser')
            apis = set()
            for script in soup.find_all('script'):
                if script.string:
                    matches = re.findall(r'["\'](/api/.*?)["\']', script.string)
                    for match in matches:
                        apis.add(urljoin(self.url, match))
            filename = f"{self.results_dir}/{self.base_url}_apis.txt"
            with open(filename, 'w') as f:
                for api in sorted(apis):
                    f.write(f"{api}\n")
        except:
            pass
    
    def extract_code_silent(self):
        try:
            response = self.session.get(self.url)
            soup = BeautifulSoup(response.text, 'html.parser')
            html_file = f"{self.results_dir}/{self.base_url}_page.html"
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(soup.prettify())
        except:
            pass
    
    def extract_links_silent(self):
        try:
            response = self.session.get(self.url)
            soup = BeautifulSoup(response.text, 'html.parser')
            links = {'internal': [], 'external': []}
            for a in soup.find_all('a', href=True):
                href = a['href']
                if href.startswith('http'):
                    if self.base_url in href:
                        links['internal'].append(href)
                    else:
                        links['external'].append(href)
            filename = f"{self.results_dir}/{self.base_url}_links.json"
            with open(filename, 'w') as f:
                json.dump(links, f)
        except:
            pass
    
    def extract_images_silent(self):
        try:
            response = self.session.get(self.url)
            soup = BeautifulSoup(response.text, 'html.parser')
            images = []
            for img in soup.find_all('img', src=True):
                images.append(img['src'])
            filename = f"{self.results_dir}/{self.base_url}_images.txt"
            with open(filename, 'w') as f:
                for img in images:
                    f.write(f"{img}\n")
        except:
            pass
    
    def extract_forms_silent(self):
        try:
            response = self.session.get(self.url)
            soup = BeautifulSoup(response.text, 'html.parser')
            forms = []
            for form in soup.find_all('form'):
                forms.append({
                    'action': form.get('action', ''),
                    'method': form.get('method', 'get')
                })
            filename = f"{self.results_dir}/{self.base_url}_forms.json"
            with open(filename, 'w') as f:
                json.dump(forms, f)
        except:
            pass
    
    def find_hidden_silent(self):
        try:
            response = self.session.get(self.url)
            soup = BeautifulSoup(response.text, 'html.parser')
            hidden = {
                'inputs': [],
                'comments': re.findall(r'<!--(.*?)-->', response.text, re.DOTALL)
            }
            for inp in soup.find_all('input', type='hidden'):
                hidden['inputs'].append({
                    'name': inp.get('name', ''),
                    'value': inp.get('value', '')
                })
            filename = f"{self.results_dir}/{self.base_url}_hidden.json"
            with open(filename, 'w') as f:
                json.dump(hidden, f)
        except:
            pass
    
    def detect_tech_silent(self):
        try:
            response = self.session.get(self.url)
            tech = {'server': response.headers.get('Server', 'Unknown')}
            if 'wp-content' in response.text:
                tech['cms'] = 'WordPress'
            filename = f"{self.results_dir}/{self.base_url}_tech.json"
            with open(filename, 'w') as f:
                json.dump(tech, f)
        except:
            pass
    
    def security_headers_silent(self):
        try:
            response = self.session.get(self.url)
            headers = dict(response.headers)
            filename = f"{self.results_dir}/{self.base_url}_headers.json"
            with open(filename, 'w') as f:
                json.dump(headers, f)
        except:
            pass
    
    def find_subdomains_silent(self):
        try:
            domain = self.base_url.replace('www.', '')
            common = ['www', 'mail', 'admin', 'api']
            found = []
            for sub in common:
                try:
                    requests.get(f"http://{sub}.{domain}", timeout=1)
                    found.append(f"{sub}.{domain}")
                except:
                    pass
            filename = f"{self.results_dir}/{domain}_subdomains.txt"
            with open(filename, 'w') as f:
                for sub in found:
                    f.write(f"{sub}\n")
        except:
            pass
    
    def scan_directories_silent(self):
        try:
            dirs = ['admin', 'wp-admin', 'backup', 'uploads']
            found = []
            for d in dirs:
                try:
                    r = self.session.get(f"{self.url}/{d}/", timeout=1)
                    if r.status_code == 200:
                        found.append(d)
                except:
                    pass
            filename = f"{self.results_dir}/{self.base_url}_dirs.txt"
            with open(filename, 'w') as f:
                for d in found:
                    f.write(f"{d}\n")
        except:
            pass
    
    def find_parameters_silent(self):
        try:
            response = self.session.get(self.url)
            params = re.findall(r'name=["\']([^"\']+)["\']', response.text)
            filename = f"{self.results_dir}/{self.base_url}_params.txt"
            with open(filename, 'w') as f:
                for p in set(params):
                    f.write(f"{p}\n")
        except:
            pass
    
    def extract_emails_silent(self):
        try:
            response = self.session.get(self.url)
            emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', response.text)
            filename = f"{self.results_dir}/{self.base_url}_emails.txt"
            with open(filename, 'w') as f:
                for email in set(emails):
                    f.write(f"{email}\n")
        except:
            pass
    
    def extract_phones_silent(self):
        try:
            response = self.session.get(self.url)
            phones = re.findall(r'\+\d{1,3}[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}', response.text)
            filename = f"{self.results_dir}/{self.base_url}_phones.txt"
            with open(filename, 'w') as f:
                for phone in set(phones):
                    f.write(f"{phone}\n")
        except:
            pass
    
    def find_social_silent(self):
        try:
            response = self.session.get(self.url)
            social = {}
            platforms = ['facebook.com', 'twitter.com', 'instagram.com', 'linkedin.com']
            for platform in platforms:
                if platform in response.text:
                    social[platform] = 'Found'
            filename = f"{self.results_dir}/{self.base_url}_social.json"
            with open(filename, 'w') as f:
                json.dump(social, f)
        except:
            pass
    
    def response_time_silent(self):
        try:
            start = time.time()
            self.session.get(self.url)
            end = time.time()
            filename = f"{self.results_dir}/{self.base_url}_time.txt"
            with open(filename, 'w') as f:
                f.write(f"{(end-start)*1000:.2f}ms")
        except:
            pass
    
    # ============================================
    # FEATURE 19: SAVE ALL RESULTS
    # ============================================
    def save_all(self):
        """Saare results ek folder mein save karo"""
        print(f"\n{BLUE}[*] Creating complete report...{RESET}")
        
        try:
            # Create report folder with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            report_dir = f"{self.results_dir}/report_{self.base_url}_{timestamp}"
            os.makedirs(report_dir, exist_ok=True)
            
            # Copy all files
            import shutil
            for file in os.listdir(self.results_dir):
                if file.startswith(self.base_url):
                    src = os.path.join(self.results_dir, file)
                    dst = os.path.join(report_dir, file)
                    shutil.copy2(src, dst)
            
            # Create summary
            summary = {
                'target': self.url,
                'timestamp': timestamp,
                'files': os.listdir(report_dir),
                'total_files': len(os.listdir(report_dir))
            }
            
            summary_file = f"{report_dir}/summary.json"
            with open(summary_file, 'w') as f:
                json.dump(summary, f, indent=4)
            
            print(f"{GREEN}✅ All results saved to: {report_dir}{RESET}")
            print(f"{GREEN}✅ Total files: {summary['total_files']}{RESET}")
            
        except Exception as e:
            print(f"{RED}❌ Error: {e}{RESET}")
        
        input(f"\n{YELLOW}Press Enter to continue...{RESET}")
    
    # ============================================
    # MAIN LOOP
    # ============================================
    def run(self):
        """Main loop"""
        while True:
            self.print_banner()
            self.print_menu()
            
            choice = input(f"{CYAN}Select option (1-20): {RESET}")
            
            if choice == '1':
                self.website_info()
            elif choice == '2':
                self.find_apis()
            elif choice == '3':
                self.extract_code()
            elif choice == '4':
                self.extract_links()
            elif choice == '5':
                self.extract_images()
            elif choice == '6':
                self.extract_forms()
            elif choice == '7':
                self.find_hidden()
            elif choice == '8':
                self.detect_tech()
            elif choice == '9':
                self.security_headers()
            elif choice == '10':
                self.find_subdomains()
            elif choice == '11':
                self.scan_directories()
            elif choice == '12':
                self.download_website()
            elif choice == '13':
                self.find_parameters()
            elif choice == '14':
                self.extract_emails()
            elif choice == '15':
                self.extract_phones()
            elif choice == '16':
                self.find_social()
            elif choice == '17':
                self.response_time()
            elif choice == '18':
                self.all_in_one()
            elif choice == '19':
                self.save_all()
            elif choice == '20':
                print(f"\n{GREEN}Bye! Thanks for using Website Toolkit{RESET}")
                sys.exit(0)
            else:
                print(f"{RED}Invalid option!{RESET}")
                time.sleep(1)

# ============================================
# MAIN
# ============================================
if __name__ == "__main__":
    try:
        tool = WebsiteToolkit()
        tool.run()
    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}Exiting...{RESET}")
        sys.exit(0)
    except Exception as e:
        print(f"{RED}Error: {e}{RESET}")
        sys.exit(1)