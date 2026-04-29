#!/usr/bin/env python3
import os
import sys

# Colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"

# ASCII Banner
banner = f"""{CYAN}==========================================
   Distribution Installer for Termux v1.0
   
 - github.com/DarkSkull777/install-linux
        Coded by @XSkull7 (telegram)
=========================================={RESET}
"""

# Menu options
menu = {
    "Ubuntu": {
        "Ubuntu 18.04": "wget https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Ubuntu/ubuntu.sh -O ubuntu.sh && chmod +x ubuntu.sh && bash ubuntu.sh",
        "Ubuntu 20.04": "wget https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Ubuntu20/ubuntu20.sh -O ubuntu20.sh && chmod +x ubuntu20.sh && bash ubuntu20.sh",
        "Ubuntu 22.04": "wget https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Ubuntu22/ubuntu22.sh -O ubuntu22.sh && chmod +x ubuntu22.sh && bash ubuntu22.sh",
    },
    "Debian": {
        "Debian 10.00": "wget https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Debian/debian.sh -O debian.sh && chmod +x debian.sh && bash debian.sh",
    },
    "Manjaro": {
        "Manjaro 21": "wget https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Manjaro/manjaro.sh -O manjaro.sh && chmod +x manjaro.sh && bash manjaro.sh",
    },
    "Kali Linux": {
        "Kali Linux 21.22": "wget https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Kali/kali.sh -O kali.sh && chmod +x kali.sh && bash kali.sh",
    },
    "Void": {
        "Void latest": "wget https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Void/void.sh -O void.sh && chmod +x void.sh && bash void.sh",
    },
    "Fedora": {
        "Fedora 33": "wget https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Fedora/fedora.sh -O fedora.sh && chmod +x fedora.sh && bash fedora.sh",
    },
    "Arch Linux": {
        "Arch Linux 2021.07.71": "wget https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Arch/armhf/arch.sh -O arch.sh && chmod +x arch.sh && bash arch.sh",
    }
}

def run_install(command):
    os.system("pkg update -y && pkg install wget curl proot tar -y")
    os.system(command)

def add_alias(alias, distro_script):
    bashrc = os.path.expanduser("~/.bashrc")
    alias_cmd = f"alias {alias}='./{distro_script}'\n"
    with open(bashrc, "a") as f:
        f.write(alias_cmd)
    os.system(f"source {bashrc}")
    print(f"{GREEN}Alias '{alias}' added successfully!{RESET}")

def main():
    print(banner)
    print(f"{YELLOW}Available Categories & Distributions:{RESET}")
    idx_map = {}
    idx = 1
    for category, distros in menu.items():
        print(f"{MAGENTA}[ {category} ]{RESET}")
        for distro, cmd in distros.items():
            print(f"  {idx}. {distro}")
            idx_map[idx] = (distro, cmd)
            idx += 1
    
    choice = int(input(f"{BLUE}[ ? ] Enter your choice number: {RESET}"))
    if choice not in idx_map:
        print(f"{RED}Invalid choice!{RESET}")
        sys.exit(1)
    
    distro, command = idx_map[choice]
    print(f"{GREEN}Installing {distro}...{RESET}")
    run_install(command)
    
    autorun = input(f"{CYAN} [ i ] Do you want to add autorun alias to ~/.bashrc? (y/n): {RESET}").lower()
    if autorun == "y":
        alias_name = input(f"{YELLOW}[ ! ]Enter alias name you want: {RESET}")
        script_name = f"start-{distro.lower().replace(' ', '').replace('.', '')}.sh"
        add_alias(alias_name, script_name)
    else:
        print(f"{GREEN}Installation completed without alias.{RESET}")

if __name__ == "__main__":
    main()
