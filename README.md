# Port Scanner with Web Dashboard

A network security tool I built using Python and Flask. You enter 
an IP address or domain name, click scan, and it tells you which 
ports are open, what services are running on them, and how risky 
they are from a security perspective.

> Built with AI guidance — concepts, logic, and implementation 
> understood and directed by me.

## What It Does

- Scans any IP address or domain name for open ports
- Grabs service banners to identify what software is running 
  and its version
- Color coded risk levels — green for low, yellow for medium, 
  red for high risk ports
- Resolves domain names to IP addresses automatically
- Export scan results as a report file
- AI powered security analysis of open ports

## Tech Stack

- Python — core scanning engine
- Flask — web server and API
- HTML, CSS, JavaScript — browser dashboard
- Threading — parallel port scanning for speed
- Socket library — TCP connections to check ports

## Key Concepts I Learned

- How TCP port scanning works
- Banner grabbing to identify software versions
- Why threading makes scanning fast (1024 ports in seconds 
  instead of 17 minutes)
- How Flask connects a browser frontend to a Python backend
- Why open ports like 445 (SMB) and 3389 (RDP) are high risk

## How to Run

1. Clone the repository
2. Install dependencies: pip install flask
3. Run: python app.py
4. Open browser at: http://127.0.0.1:5000

## Legal Note

Only scan systems you own or have explicit permission to scan. 
For practice use localhost or legal platforms like HackTheBox 
and TryHackMe.

## Author

Mohammed Fazlian
Cybersecurity Enthusiast
- Mail: mdfazlian30@gmail.com
- Linkedin: www.linkedin.com/in/mohammed-fazlian-86459b197
