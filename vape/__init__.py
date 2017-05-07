#! /usr/bin/env python
# -*- coding: utf-8 -*-

# I hate Python 3.
from __future__ import print_function

import argparse
import xerox

def vaporize(vape_me):
    """Solution shamelessly stolen from http://stackoverflow.com/a/8327034
    by Ignacio Vazquez-Abrams"""
    normal = u' 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~'
    wide = u'　０１２３４５６７８９ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ！゛＃＄％＆（）＊＋、ー。／：；〈＝〉？＠［\\］＾＿‘｛｜｝～'
    widemap = dict((ord(x[0]), x[1]) for x in zip(normal, wide))
    vaped = vape_me.translate(widemap)
    return vaped

def get_parser():
    parser = argparse.ArgumentParser(description='ＣＯＭＭＡＮＤ　ＬＩＮＥ　ＡＥＳＴＨＥＴＩＣ　ＧＥＮＥＲＡＴＯＲ.')
    parser.add_argument('query', metavar='QUERY', type=str, nargs='*',
            help='the string to vaporize')
    parser.add_argument('-c','--copy', help='copy result to the clipboard.', default=False, dest='copy', action='store_true')
    return parser

def command_line_runner():
    parser = get_parser()
    margs = vars(parser.parse_args())
    if not margs['query']:
        parser.print_help()
        return

    result = vaporize(u' '.join(margs['query']))
     
    if margs['copy']:
        xerox.copy(result)

    print(result)

if __name__ == '__main__':
    command_line_runner()
