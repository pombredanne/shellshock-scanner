# Shellshock Scanner
A python web crawler that uses the [`scrapy`](http://www.secdev.org/projects/scapy/)
module to scan webpages for the [shellshock vulnerability](http://en.wikipedia.org/wiki/Shellshock_%28software_bug%29).

## Installation
Before running the scanner you will need to install the `scapy` module. The
easiest way to do this is using `pip`, with a command such as `sudo pip
install scapy`. Installation will vary based on your platform/preferences.

## Usage
Open the file `shellshock_scanner/spiders/shellshock_spider.py` and change
the `domains_to_scan` list to the domains you want to scan, along with the HTTP
port numbers:
```
domains_to_scan = [
    ('localhost', 8080),
]
```

Then run `scrapy` with the following command:
```
scrapy crawl shellshock -o output.json
```

Any vulnerable URLs will then be printed in red on the terminal, and the status
of all URLs will be output as json formatted data in the `output.json` file...
```
[{"url": "http://localhost:8080/test.cgi", "vulnerable": true},
{"url": "http://localhost:8080/test2.cgi", "vulnerable": false}]
```

## DISCLAIMER
ONLY RUN THIS AGAINST DOMAINS THAT YOU CONTROL AND/OR HAVE PERMISSION TO SCAN
AGAINST. I ACCEPT NO LIABILITY FOR ANY DAMAGE OR TROUBLE YOU GET YOURSELF INTO!
