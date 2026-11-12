# SystemScope

A local-first, read-only system and storage auditing desktop application.

## Features
- System dashboard: CPU, memory, disk volumes, OS and hardware details
- File Explorer: scan a selected folder, filter files, inspect metadata and sort by size
- Software Inventory: best-effort installed application inventory per operating system
- Security Center: SHA-256 file hashing and basic permission checks
- CSV and JSON exports
- Dark desktop UI with a gold accent

## Safety and privacy
- Scanning is read-only: no files are deleted or modified.
- Do not run as root/Administrator unless you have a specific reason.
- Symlinks are skipped during directory traversal.
- Common sensitive directories are excluded by default.
- File contents are read only when you explicitly request a SHA-256 hash.
- No network requests or automatic uploads are made.

## Requirements
Python 3.10+ recommended.

## Install on Debian / Ubuntu / Kali
```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip -y
cd SystemScope
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

## Install on Arch Linux
```bash
sudo pacman -Syu
sudo pacman -S python python-pip
cd SystemScope
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

If PySide6 fails to install from pip on your Arch setup, install the distro package (`pyside6`) and `python-psutil`, then use the system Python environment according to Arch's package-management policy.

## Install on Windows
Install Python 3.10+ from https://www.python.org/downloads/ and enable "Add Python to PATH".
Open PowerShell in this folder:
```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
py main.py
```

## Install on macOS
Install Python 3.10+ (python.org or Homebrew), then:
```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 main.py
```

## Build an executable
Install PyInstaller in the active virtual environment:
```bash
pip install pyinstaller
```
Build on the operating system you want to package:
```bash
pyinstaller --noconfirm --windowed --name SystemScope main.py
```
The output appears in `dist/`. Build separately on Linux, Windows and macOS; PyInstaller is not a cross-compiler.

## Notes
- Software inventory is best-effort and varies by OS and package manager.
- Folder sizes are logical totals of scanned regular files, not physical disk allocation.
- Hard links may be counted more than once.
- Very large scans can take time. Start with a small test folder.
- This is a system auditing utility, not antivirus software.
