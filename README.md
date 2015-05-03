# Shellshock Scanner
This is a python web crawler that uses `scrapy` to scan pages for the shellshock
vulerability.

## Installation
```
sudo pip install scrapy
git clone https://github.com/cdodd/shellshock-scanner.git
cd shellshock-scanner
```

### Usage
Open the file `shellshock_scanner/spiders/shellshock_spider.py` and change
the `domains_to_scan` list to the domains you want to scan, along with the HTTP
port numbers:
```
domains_to_scan = [
    ('localhost', 8080),
]
```

Run `scrapy` with the following command:
```
scrapy crawl shellshock -o output.json
```

Any vulnerable URLs will then be printed in red on the terminal, and the status
of all URLs will be output in json to the `output.json` file...
```
[{"url": "http://localhost:8080/test.cgi", "vulnerable": true},
{"url": "http://localhost:8080/test2.cgi", "vulnerable": false}]
```

## DISCLAIMER
ONLY RUN THIS AGAINST DOMAINS THAT YOU CONTROL AND/OR HAVE PERMISSION TO SCAN
AGAINST. I ACCEPT NO LIABILITY FOR ANY DAMAGE OR TROUBLE YOU GET YOURSELF INTO!
