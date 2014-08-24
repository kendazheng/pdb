#!/usr/bin/env python
from optparse import OptionParser
from file_client import fetchAll
# from telnet import fetchAll


def args_callback(option, opt, value, parser):
    setattr(parser.values, option.dest, value.split(','))


parser = OptionParser()
parser.add_option(
    '-H',
    '--Host',
    action='callback',
    dest='hosts',
    type='string',
    callback=args_callback,
    help='The host list you want to get, please split with ,'
)
parser.add_option(
    '-D',
    '--Directions',
    action='callback',
    dest='dirs',
    type='string',
    callback=args_callback,
    help='The directions where to be')
parser.add_option(
    '-C',
    '--Config Files Direction',
    action='callback',
    dest='confs',
    type='string',
    callback=args_callback,
    help='The config file source directions where to be'
)
(options, args) = parser.parse_args()

    
if __name__ == '__main__':
    params = dict()
    if options.hosts:
        params['hosts'] = options.hosts
    if options.dirs:
        params['dirs'] = options.dirs
    if options.confs:
        params['confs'] = options.confs
    code, msg = fetchAll(**params)
    print msg
