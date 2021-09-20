# torChecker - A Tor Relay IP checking tool
This is a simple python3 tool that checks if an IP address is a Tor Relay or not.

## Features
- Single target input
- List input

## Requirements
- Python 3.x

## Basic Usage
To check an IP, do the following: \
`python3 torChecker.py -t <ip>` (*where `<ip>` is the IP address you want to check*) \
\
To check an IP list, do the following: \
`python3 torChecker.py -l <filename>.txt` (*where `<filename>` is the file (.txt) with the IPs you want to check*)

For more information, please check the arguments "help" with: \
`python3 torChecker.py -h`

## IP File Example
The file containing the IPs must be a `.txt` and have the following structure for the tool to work:
```
176.10.99.200 
109.70.100.28
51.75.64.23 
82.221.128.191
109.70.100.31 
185.220.100.254 
185.220.103.9 
195.176.3.23
185.220.100.243
185.220.100.245
198.58.107.53
199.249.230.83
```
