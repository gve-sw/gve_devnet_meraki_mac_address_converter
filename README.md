# gve_devnet_meraki_mac_address_converter
This repository contains a script that converts a list of MAC addresses to be converted to lowercase for compatibility between Meraki and FreeRADIUS authentication service. 


## Contacts
* Kevin Chen

## Solution Components
* Meraki

## Installation/Usage

Make sure Python 3 is installed in your environment, and if not, you may download Python [here](https://www.python.org/downloads/).

To use this script, copy the list of MAC addresses to be converted into the folder of this project. 


    $ python MAC_converter.py -i <input file name> -o <output file name>

 e.g. 
    $ python MAC_converter.py -i input.txt -o output.txt



## Docker Usage

This is a template, project owner to update

Add any steps needed for someone to run your project.

To launch an optical service create:


    $ python create_service.py



### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.