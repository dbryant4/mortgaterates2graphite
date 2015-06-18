# Mortgage Rate 2 Graphite

A basic Python script that queries the Zillow.com's API for mortgage rates and push that data to a graphite server. This script is designed to be ran once a day since rates change once a day.

# Installation

Simply install the requirements in `requirements.txt`:

```pip install -r requirements.txt```

# Usage

All options are set using command line arguments. The only one the is required is the `--zws-id` which can be obtained from [Zillow](https://www.zillow.com/webservice/Registration.htm).

	$ ./mortgagerate2graphite.py -h
	usage: mortgagerate2graphite.py [-h] [--graphite-host GRAPHITE_HOST]
	                                [--graphite-prefix GRAPHITE_PREFIX]
	                                [--state STATE] --zws-id ZWS_ID

	Push mortgage rates to graphite

	optional arguments:
	  -h, --help            show this help message and exit
	  --graphite-host GRAPHITE_HOST, -g GRAPHITE_HOST
	                        Graphite host to send mortgage rates
	  --graphite-prefix GRAPHITE_PREFIX, -p GRAPHITE_PREFIX
	                        Prefix to prepend to graphite metric name
	  --state STATE, -s STATE
	                        Which state do you want mortgage rates
	  --zws-id ZWS_ID, -z ZWS_ID
	                        zws-id for use with the Zillow.com API

# Tests
There are currently no tests since this is a very basic script. If it becomes more complicated with more logic, then I will add tests.