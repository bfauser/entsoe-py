# _*_ encoding utf-8 _*_

import sys
import os
import unittest
import pandas as pd
from bs4 import BeautifulSoup
import entsoe.entsoe as ent

class TestCase(unittest.TestCase):
    """
    test class for entsoe-py package. 
    
    """
    def setUp(self):
        """
        setUp of *UnitTests* for requests we need a SECRET_KEY,
        which we import from an environement variable. Set this
        variable as follows:
        .. code::
        > set ENTSOE_SECRET_KEY=my very secret api keys

        """
        global ENTSOE_SECRET_KEY
        ENTSOE_SECRET_KEY = os.environ.get('ENTSOE_SECRET_KEY') or None
        if ENTSOE_SECRET_KEY == None:
            raise ValueError('You need to set the environment variable ENTSOE_SECRET_KEY to your private app.Key')

    def tearDown(self):
        """tearDown of *UnitTests*, e.g. close db, session and other structures.
           Here we do nothing.

        """
        pass


    def test_basic_request(self):
        """Test *basic_request* of the entsoe package. We make a basic_request
        request for one day 2018-01-27. We have in test_data the XML response
        and check the following:

        - check if the request got status code 200
        - check if test data could be loaded from disk
        - check how many <TimeSeries> tags were found in the present request
          and from the stored test data
        - find start and end time of request and compare that with
          o the time set in the request
          o the time recieved from the online request
          o the time recieved from the test data file

        """
        global ENTSOE_SECRET_KEY
        # set domain and timezone
        domain = ent.DOMAIN_MAPPINGS['DE']
        tmzone = ent.TIMEZONE_MAPPINGS['DE']
        # initialize Enstoe class
        ent_app = ent.Entsoe(ENTSOE_SECRET_KEY)
        params = {'documentType': 'A75',
                  'processType': 'A16',
                  'in_Domain': domain,
                 }
        # setup start and end time for request
        start_tm = pd.datetime(2018,1,27)
        end_tm = pd.datetime(2018,1,28)
        # make request to entso-e
        result = None
        result = ent_app.base_request(params, start_tm, end_tm)
        # check if request worked
        assert result.status_code == 200
        # open test_data (retrieved and checked)
        with open('./tests/test_data/basic_request_2018-01-27_28-PT15M.xml', 'r') as fp:
            text = fp.read()
        # check if text was loaded
        assert len(text) > 0

        soup1 = BeautifulSoup(text, 'html.parser')
        soup2 = BeautifulSoup(result.content, 'html.parser')

        num_tm_series1 = 0
        for tm_series in soup1.find_all('timeseries'):
             num_tm_series1 += 1
        num_tm_series2 = 0
        for tm_series in soup2.find_all('timeseries'):
             num_tm_series2 += 1
        # check if 33 time series were loaded, and retrieved
        assert num_tm_series1 == 33
        assert num_tm_series2 == num_tm_series1

        # find start time in soup
        tm_interval1 = soup1.find('time_period.timeinterval')
        tm_interval2 = soup2.find('time_period.timeinterval')
        start1 = tm_interval1.find('start').get_text()
        start2 = tm_interval2.find('start').get_text()
        pd_start1 = pd.Timestamp(start1, tz=None).to_pydatetime()
        pd_start2 = pd.Timestamp(start2, tz=None).to_pydatetime()
        # check if start date matches
        assert start_tm.year == pd_start1.year
        assert start_tm.day == pd_start1.day
        assert start_tm.hour == pd_start1.hour
        #
        assert start_tm.year == pd_start2.year
        assert start_tm.day == pd_start2.day
        assert start_tm.hour == pd_start2.hour
        # find end time in soup
        end1 = tm_interval1.find('end').get_text()
        end2 = tm_interval2.find('end').get_text()
        pd_end1 = pd.Timestamp(end1, tz=None).to_pydatetime()
        pd_end2 = pd.Timestamp(end2, tz=None).to_pydatetime()
        # check if end date matches
        assert end_tm.year == pd_end1.year
        assert end_tm.day == pd_end1.day
        assert end_tm.hour == pd_end1.hour
        #
        assert end_tm.year == pd_end2.year
        assert end_tm.day == pd_end2.day
        assert end_tm.hour == pd_end2.hour

    def test_price_request(self):
        """test price request"""
        global ENTSOE_SECRET_KEY
        # set domain and timezone
        domain = ent.DOMAIN_MAPPINGS['DE']
        tmzone = ent.TIMEZONE_MAPPINGS['DE']
        # initialize Enstoe class
        ent_app = ent.Entsoe(ENTSOE_SECRET_KEY)
        country_code = 'DE'
        domain = ent.DOMAIN_MAPPINGS[country_code]
        params = {
            'documentType': 'A25',
			'businessType': 'B07',
			'contract_MarketAgreement.Type': 'A01',
            'in_Domain': domain,
            'out_Domain': domain
        }
        # setup start and end time for request
        start_tm = pd.datetime(2018,1,27)
        end_tm = pd.datetime(2018,1,28)
        # make request to entso-e
        result = ent_app.query_price(country_code, start_tm, end_tm)
        # check if request worked
        #assert result.status_code == 200
        print(ent_app.__dict__)
        print(result)

if __name__ == '__main__':
    unittest.main()