#!/usr/bin/env python

"""
This is a little script that pulls the current mortage rates for the US from
Zillow.com and sends the results to graphite.
"""

import os
import argparse
import requests
import graphiteudp


parser = argparse.ArgumentParser(description='Push mortgage rates to graphite')
parser.add_argument('--graphite-host', '-g', default='localhost', help='Graphite host to send mortgage rates')
parser.add_argument('--graphite-prefix', '-p', default='mortgate-rates', help='Prefix to prepend to graphite metric name')
parser.add_argument('--state', '-s', default='DC', help='Which state do you want mortgage rates')
parser.add_argument('--zws-id', '-z', required=True, help='zws-id for use with the Zillow.com API')
args = parser.parse_args()

graphite = graphiteudp.GraphiteUDPClient(args.graphite_host,
                                        prefix = args.graphite_prefix.replace(" ","_"))

payload = {
            'zws-id': args.zws_id,
            'state': args.state,
            'output': 'json'
          }

r = requests.get('http://www.zillow.com/webservice/GetRateSummary.htm', params=payload)
rates = r.json()['response']['today']

for mortgage, rate in rates.iteritems():
    graphite.send(mortgage, float(rate))
