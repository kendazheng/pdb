#!/usr/bin/env python
import socket
import sys
import logging
import traceback
import os
from optparse import OptionParser

from file_client import fetch

def args_callback(option, opt, value, parser):
    setattr(parser.values, option.dest, value.split(','))


parser = OptionParser()
parser.add_option('-H', '--Host', action='callback', dest='hosts', type='string',\
    callback=args_callback, help='The host list you want to get, please split with ,')
parser.add_option('-D', '--direction', action='callback', dest='dirs', type='string',\
    callback=args_callback, help='The direction list you want to save resonse file from server, please split with ,')
(options, args) = parser.parse_args()



    
if __name__ == '__main__':
    params = dict()
    if options.hosts:
        params['hosts'] = options.hosts
    if options.dirs:
        params['dirs'] = options.dirs

    fetch(**params)
