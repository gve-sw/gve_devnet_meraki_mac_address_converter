#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Python example script showing proper use of the Cisco Sample Code header.
Copyright (c) 2023 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
               https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""


from __future__ import absolute_import, division, print_function


__author__ = "Kevin Chen  <kevchen3@cisco.com>"
__contributors__ = [
    "Josh Ingeniero <jingenie@cisco.com>",
]
__copyright__ = "Copyright (c) 2023 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"



# convert mac address to lower case

import sys, getopt

def main(argv):
    inputfile = ''
    outputfile = ''
    opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    for opt, arg in opts:
        if opt == '-h':
            print ('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
           inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print ('Input file is ', inputfile)
    print ('Output file is ', outputfile)

    try: 
        with open(inputfile, 'r') as f:
            address_list = f.readlines()
            results = [address.lower() for address in address_list]
    except:
        print("input file error, please check your input file path")
    
    try:
        with open(outputfile, 'w') as f:
            f.writelines(address_list)
            f.writelines('\n')
            f.writelines(results)
            print("new MAC address list is complete")
    except:
            print("output file error, please check your output file path")


if __name__ == "__main__":
   main(sys.argv[1:])



