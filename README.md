API Sentinel

API Sentinel is a modular API security scanner built in Python to test REST endpoints for common security issues.

The tool performs automated checks aligned with the OWASP API Security Top 10 and generates structured JSON reports.

Features

Injection payload testing

Authentication enforcement checks

Rate limiting detection

Basic BOLA (ID parameter manipulation) testing

JSON report generation

CLI-based execution

Installation

Clone the repository and install dependencies:

git clone https://github.com/S-Anagha/API-Sentinel
cd API-Sentinel
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
pip install -r requirements.txt

Usage
python sentinel.py --url https://httpbin.org/get

Reports are saved in the output/ directory.

Disclaimer

For educational and authorized security testing only.
Do not scan systems without permission.
