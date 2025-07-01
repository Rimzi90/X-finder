#!/usr/bin/env python3
import os, time, random
from googlesearch import search

# Terminal Colors
RED = "\033[91m"; GREEN = "\033[92m"; YELLOW = "\033[93m"
BLUE = "\033[94m"; CYAN = "\033[96m"; RESET = "\033[0m"

# Display Banner
def show_banner():
    os.system("clear")
    print(f"""{RED}
██╗     ██╗███╗   ██╗██╗  ██╗    ███████╗██╗███╗   ██╗██████╗ ███████╗██████╗ 
██║     ██║████╗  ██║██║ ██╔╝    ██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
██║     ██║██╔██╗ ██║█████╔╝     ███████╗██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
██║     ██║██║╚██╗██║██╔═██╗     ╚════██║██║██║╚██╗██║██║  ██║██╔══╝  ╚═══╝  
███████╗██║██║ ╚████║██║  ██╗    ███████║██║██║ ╚████║██████╔╝███████╗██║     
╚══════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝    ╚══════╝╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝     
{CYAN}        LINK FINDER - WhatsApp & Telegram Group Finder by RIMZI{RESET}
""")

# Sample descriptions
descriptions = [
    "🔥 Active Group - Join Fast!", "💬 Daily Discussions & Fun",
    "🔔 24/7 Online Members", "🌐 Public Group Open to All",
    "✅ Verified & Active Group"
]

# Search WhatsApp groups
def find_whatsapp(topic):
    print(f"\n{CYAN}Searching WhatsApp groups for:{RESET} {topic}\n")
    count = 0
    for link in search(f"site:chat.whatsapp.com {topic}", num_results=50, unique=True):
        if "chat.whatsapp.com" in link:
            print(f"{YELLOW}╭──────────────[ ✅ ]──────────────╮")
            print(f"{GREEN} Link       : {link}")
            print(f" Description: {random.choice(descriptions)}")
            print(f"{YELLOW}╰────────────────────────────────╯{RESET}\n")
            count += 1
            if count == 10: break
            time.sleep(0.3)
    if count == 0:
        print(f"{RED}❌ No WhatsApp groups found.{RESET}")

# Search Telegram groups
def find_telegram(topic):
    print(f"\n{CYAN}Searching Telegram groups for:{RESET} {topic}\n")
    count = 0
    seen = set()
    for link in search(f"site:t.me {topic}", num_results=50, unique=True):
        if "t.me/" in link and link not in seen:
            seen.add(link)
            print(f"{YELLOW}╭──────────────[ ✅ ]──────────────╮")
            name = link.split("/")[-1].replace("-", " ").title()
            print(f"{GREEN} Group Name : {name}")
            print(f" Link       : {link}")
            print(f" Description: {random.choice(descriptions)}")
            print(f"{YELLOW}╰────────────────────────────────╯{RESET}\n")
            count += 1
            if count == 10: break
            time.sleep(0.3)
    if count == 0:
        print(f"{RED}❌ No Telegram groups found.{RESET}")

# Main Menu Loop
def main():
    while True:
        show_banner()
        print(f"{GREEN}[1]{RESET} WhatsApp  |  {GREEN}[2]{RESET} Telegram  |  {GREEN}[0]{RESET} Exit")
        choice = input(f"{BLUE}>> {RESET}").strip()
        if choice == "1":
            find_whatsapp(input("📘 Enter topic: ").strip())
        elif choice == "2":
            find_telegram(input("📘 Enter topic: ").strip())
        elif choice == "0":
            print(f"{YELLOW}Exiting... Bye!{RESET}")
            break
        else:
            print(f"{RED}Invalid choice.{RESET}")
        input(f"{CYAN}🔁 Press Enter to return...{RESET}")

if __name__ == "__main__":
    main()
