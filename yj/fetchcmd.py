#!/usr/bin/env python
import socket
import sys
import logging
import traceback
import os
from optparse import OptionParser

#from file_client import fetchAll
from telnet import fetchAll

def args_callback(option, opt, value, parser):
    setattr(parser.values, option.dest, value.split(','))


parser = OptionParser()
parser.add_option('-H', '--Host', action='callback', dest='hosts', type='string',\
    callback=args_callback, help='The host list you want to get, please split with ,')
parser.add_option('-U', '--Username', action='store', dest='username', type='string',\
    help='Username used to telnet remote host')
parser.add_option('-P', '--Password', action='store', dest='password', type='string',\
    help='Password used to telnet remote host')
(options, args) = parser.parse_args()



    
if __name__ == '__main__':
    params = dict()
    if options.hosts:
        params['hosts'] = options.hosts
    if options.username:
        params['username'] = options.username
    if options.password:
        params['password'] = options.password
    code, msg = fetchAll(**params)
    print msg
