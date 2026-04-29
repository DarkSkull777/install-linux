# Distribution Installer for Termux
Coded by @XSkull7 (telegram)

---

## What is this?
A Python script that helps you install popular Linux distributions inside Termux with a nice menu, colors, and ASCII banner.  
No extra dependencies needed — just Python 3 and Termux.

---

## How to run
Clone the repo and run the script:

```bash
pkg install git python -y
git clone https://github.com/DarkSkull777/install-linux.git
cd install-linux
python install.py
```

---

## Features
- Auto install with one click
- Option to add autorun alias into ~/.bashrc
  - Example: alias ubuntu='./start-ubuntu22.sh'
- No external libraries required

---

## Available Distros
Here’s what you can install right now:

Ubuntu
- 18.04
- 20.04
- 22.04

Debian
- 10.00

Manjaro
- 21

Kali Linux
- 21.22

Void
- latest

Fedora
- 33

Arch Linux
- 2021.07.71

---

##  Example Run
When you start the script you’ll see something like:

==========
Available Categories & Distributions:
[ Ubuntu ]
  1. Ubuntu 18.04
  2. Ubuntu 20.04
  3. Ubuntu 22.04
[ Debian ]
  4. Debian 10.00
[ Manjaro ]
  5. Manjaro 21
[ Kali Linux ]
  6. Kali Linux 21.22
[ Void ]
  7. Void latest
[ Fedora ]
  8. Fedora 33
[ Arch Linux ]
  9. Arch Linux 2021.07.71

Pick a number, let it install, and you’re good to go.

---

## ⚡ Notes
- Works only inside Termux (Android).
- Alias setup is optional — if you skip, you can still run the distro manually.
- Tested with Python 3. No requirements.txt needed.
