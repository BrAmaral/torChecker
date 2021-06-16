import urllib.request   # Import needed for collecting Tor IP`s from the web
import argparse as ap   # Import needed for CLI arguments

def parse_args():
    # This block creates an parser object instance responsible to collect the user arguments
    parser = ap.ArgumentParser()  # This line creates a parser instance
    attribute = parser.add_mutually_exclusive_group()
    attribute.add_argument('-t', '--target', help='The target IP that will be checked', type=str)  # This line adds an argument for the target IP.
    attribute.add_argument('-l', '--list', help='The IP list path that will be checked', type=str) # This line adds an argument for the IP list path.
    return parser.parse_args()   # Return the parsed arguments

def validateFile(list_path):
     if list_path.find(".txt") != -1:  # This line adds a conditional to validade if the file specified is a .txt
        with open(list_path, newline='\n', encoding="utf-8") as txtfile: # This line opens the .txt file
            for line in txtfile:                        # For each line from the opened file do...
                line = line.replace("\n","")            # Remove the line break
                try:                                    # Then try to execute the following command...
                    line = line.replace("\r","")        # If the line has "\r" too, remove it
                finally:                                # Then...
                    checkTor(line)                      # check if the IP is a Tor node

def checkTor(ip):       # This method uses a very simple linear search algorithm... and it is quite slow. --- NEEDS TO BE IMPROVED --- https://stackabuse.com/search-algorithms-in-python
    tor = urllib.request.urlopen('https://check.torproject.org/exit-addresses')     # Access Tor URL
    for ip_tor in tor:                      # For each line from the opened page do...
        ip_tor = str(ip_tor)                # Convert bytes to string (not really)
        if "ExitAddress" in ip_tor:         # If the line contains "ExitAddress"
           ip_tor = ip_tor.split(" ")[1]    # Collect the IP address from the line
           if ip == ip_tor:                 # If the IP is found to be a Tor node
               print(ip,"---> True")            # Bag & Tag
               return                           # Exit the function
    print(ip,"---> False")                  # If, after searching through all Tor node IPs, and the given IP is not found to be a Tor node, print "False"

# Main code --- CODE EXECUTION STARTS HERE ---
def main():
    parsed_args = parse_args()              # Args Init
    if parsed_args.target != None:          # If the argument "Target/-t" exists then...
        checkTor(parsed_args.target)        # Check if the given IP is a Tor node
    elif parsed_args.list != None:          # If the argument "List/-l" exists then...
        validateFile(parsed_args.list)      # Check if the given IPs are Tor nodes

# Python module detection
if __name__ == '__main__':
    main()