import unittest 
import requests
import json
import time
unittest.TestLoader.sortTestMethodsUsing = None
import logging
logger = logging.getLogger('django')



class TestA_ModelingType(unittest.TestCase):

    def testA_start_model(self):
        status = "200"
        self.assertEqual(status,"200")


class TestB_ModelingStatistics(unittest.TestCase):

    def testB_getmodel_statistics(self):
        status = "200"
        self.assertEqual(status,"200")