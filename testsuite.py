#!usr/bin/env python
""" BigID POV HealthCheck. """

#
#
# pov_healthcheck.py

# version 0.7.3
# (c) 2023 BigID
# Author: snoynaert@bigid.com
#
# Syntax:
#     python3 pov_healthcheck.py -h
#
#

# Prereqs:
#
#   1) Python version 3.x
#
#      CentOS/RHEL:
#         sudo yum install rh-python36
#      Ubuntu:
#         sudo apt-get install python3.6
#      MacOS:
#         brew install python3
#
#  2)  Extra modules
#      pip3 install --upgrade setuptools requests requests_oauthlib requests-oauth2 urllib3 pandas numpy colorist tabulate simple_colors
#


#########################################################################################
# Import modules

import requests
import json
import time
import sys

import urllib3
import pathlib
import argparse
from datetime import datetime
import pandas as pd
import numpy as np

import io
import zipfile

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from colorist import red, green, blue, bright_blue, bright_cyan, bright_red, bright_green 
from tabulate import tabulate
from simple_colors import *

import re
import os.path

#########################################################################################
# Functions


def refreshToken(initialToken):
    """Obtain systemToken from BigID"""
    url = bigidApiUrl + apiStr + "refresh-access-token"

    header_info = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": initialToken,
    }
    # print("Header: ", header_info)
    print("Target url: ", url)
    print("Connecting to BigID, please wait...")
    response = requests.get(url, headers=header_info)

    if response.status_code == 200:
        print("  Authentication : SUCCESS")
    else:
        print(
            "Status:",
            response.status_code,
            "Headers:",
            response.headers,
            "Response:",
            response.json(),
        )
        print("Cookies", response.cookies)
        print(response)
        sys.exit(
            "Error authenticating using supplied credentials. Please check access token defined in this script."
        )

    print("Retrieving system token...")
    print(response.content)
    token = json.loads(response.content)["systemToken"]

    print("System token: ", token)
    return token





def readConfig(config_file):
    """Read JSON parameter file in local directory."""

    file = pathlib.Path(config_file)
    if file.exists():
        print("File " + config_file + " exists. OK to proceed.\n")
    else:
        print(
            "   ERROR: File "
            + config_file
            + " not found in the current directory or configs subdirectory.\n"
        )
        print("   ACTION: please create the missing file in JSON format.\n")
        exit(1)

    with open(config_file) as f:
        configParams = json.load(f)
        return configParams


def executeBigidApi(url):
    """ Execute GET API """
    headers = {
#        "Content-Type": "application/json",
        "Accept": "application/json, text/plain",
        "Authorization": systemToken,
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            verify=False
        )
        if response.status_code == 200:
            # print(response.status_code)

            return response
        else:
            print('Status:', response.status_code, 'Headers:',
                   response.headers, 'Response:', response.json())
            print('Cookies', response.cookies)
            return "No scan result data"
    except requests.exceptions.ConnectionError as e:
        print(e)
    except urllib3.exceptions.ProtocolError as e:
        print(e)
    except OSError as e:
        print(e)
    except requests.exceptions.ReadTimeout as e:
        print(e)
    except requests.exceptions.JSONDecodeError as e:
        print(e)


def executeBigidApiText(url):
    """ Execute GET API """
    headers = {
#        "Content-Type": "application/json",
        "Accept": "application/json, text/plain",
        "Authorization": systemToken,
        "Content-Type": "text/plain; charset=UTF-8"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            verify=False
        )
        if response.status_code == 200:
            # print(response.status_code)

            return response
        else:
            print('Status:', response.status_code, 'Headers:',
                   response.headers, 'Response:', response.json())
            print('Cookies', response.cookies)
            return "No scan result data"
    except requests.exceptions.ConnectionError as e:
        print(e)
    except urllib3.exceptions.ProtocolError as e:
        print(e)
    except OSError as e:
        print(e)
    except requests.exceptions.ReadTimeout as e:
        print(e)
    except requests.exceptions.JSONDecodeError as e:
        print(e)

def executeBigidApiPost(url, payload):
    """ Execute POST API """
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": systemToken,
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            data=json.dumps(payload),
            verify=False
        )
        if response.status_code == 200:
            print(response.status_code)
            return response
        else:
            print('Status:', response.status_code, 'Headers:',
                   response.headers, 'Response:', response.json())
            print('Cookies', response.cookies)
            return "No scan result data"
    except requests.exceptions.ConnectionError as e:
        print(e)
    except urllib3.exceptions.ProtocolError as e:
        print(e)
    except OSError as e:
        print(e)
    except requests.exceptions.ReadTimeout as e:
        print(e)
    except requests.exceptions.JSONDecodeError as e:
        print(e)


def executeBigidApiDelete(url, payload):
    """ Execute DELETE API """
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": systemToken,
    }

    try:
        response = requests.delete(
            url,
            headers=headers,
            data=json.dumps(payload),
            verify=False
        )
        if response.status_code == 200:
            print(response.status_code)
            print(response.json())
            return response
 
        else:
            print('Status:', response.status_code, 'Headers:',
                   response.headers, 'Response:', response.json())
            print('Cookies', response.cookies)
            return "No scan result data"
    except requests.exceptions.ConnectionError as e:
        print(e)
        ss
    except urllib3.exceptions.ProtocolError as e:
        print(e)
        ss
    except OSError as e:
        print(e)
        ss
    except requests.exceptions.ReadTimeout as e:
        print(e)
        ss
    except requests.exceptions.JSONDecodeError as e:
        print(e)
        ss


def executeBigidApiPut(url, payload):
    """ Execute PUT API """
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": systemToken,
    }

    try:
        response = requests.put(
            url,
            headers=headers,
            data=json.dumps(payload),
            verify=False
        )
        if response.status_code == 200:
            print(response.status_code)
            # print(response.json())
            return response
        else:
            print('Status:', response.status_code, 'Headers:',
                   response.headers, 'Response:', response.json())
            print('Cookies', response.cookies)
            return "No scan result data"
    except requests.exceptions.ConnectionError as e:
        print(e)
    except urllib3.exceptions.ProtocolError as e:
        print(e)
    except OSError as e:
        print(e)
    except requests.exceptions.ReadTimeout as e:
        print(e)
    except requests.exceptions.JSONDecodeError as e:
        print(e)


