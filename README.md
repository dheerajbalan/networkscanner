 Network Scanner Tool

This is a simple network scanner tool built with Python using the `scapy` library. The tool sends ARP requests to the specified target network or IP range and displays the IP and MAC addresses of the devices on the network.

 Features

- Scans a specified IP range to find devices on the network.
- Displays the IP and MAC addresses of the devices found.
- Uses ARP requests for scanning the network.

 Requirements

- Python 3.x
- `scapy` library
- `colorama` library (optional, used for colored output)

 Installation

1. Clone the repository or download the script file.
2. Install the required Python packages using `pip`:

bash
	pip install scapy colorama
Usage

To run the network scanner, use the following command:

bash

	python3 network_scanner.py -t <target>

Replace <target> with the target IP range or network. For example:

bash

	python3 network_scanner.py -t 192.168.1.0/24

Example Output

markdown

-----------------------------------------
 IP                     MAC ADDRESS
-----------------------------------------
192.168.1.1             00:11:22:33:44:55
192.168.1.2             66:77:88:99:AA:BB
...


License

This project is licensed under the MIT License. See the LICENSE file for details.
Acknowledgments

This tool uses the scapy library for network scanning.
Inspired by various network scanning scripts and tutorials.test
