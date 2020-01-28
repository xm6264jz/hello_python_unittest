from unittest import TestCase 
from datetime import date, timedelta

import snow_estimate 

class TestSnowEstimator(TestCase):

    def test_estimate_regular_same_day(self):
        service_date = date.today()
        sidewalk = 'r'
        estimate = snow_estimate.estimate(service_date, sidewalk)
        self.assertEqual(25, estimate) 


    def test_estimate_regular_future(self):
        service_date = date.today() + timedelta(days=1)  # tomorrow 
        sidewalk = 'r'
        estimate = snow_estimate.estimate(service_date, sidewalk)
        self.assertEqual(20, estimate) 


    def test_estimate_corner_same_day(self):
        service_date = date.today()
        sidewalk = 'c'
        estimate = snow_estimate.estimate(service_date, sidewalk)
        self.assertEqual(35, estimate) 


    def test_estimate_corner_future(self):
        service_date = date.today() + timedelta(days=1)
        sidewalk = 'c'
        estimate = snow_estimate.estimate(service_date, sidewalk)
        self.assertEqual(30, estimate) 


    def test_date_in_past_raises_value_error(self):
        service_date = date.today() - timedelta(days=1)  # yesterday
        sidewalk = 'c'
        with self.assertRaises(ValueError):
            estimate = snow_estimate.estimate(service_date, sidewalk)
        

    def test_invalid_sidewalk_type_raises_value_error(self):
        service_date = date.today()  
        sidewalk = 'f'    # only 'r' and 'c' are valid
        with self.assertRaises(ValueError):
            estimate = snow_estimate.estimate(service_date, sidewalk)
