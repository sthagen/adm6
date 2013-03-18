#!/usr/bin/env python
#encoding:utf8
#
# file:    device_tests.py
# author: sl0
# date:   2013-03-18
#

import unittest
from adm6.adm6configparser import Adm6ConfigParser
from adm6.filter6 import IP6_Filter, Ip6_Filter_Rule
from adm6.device import ThisDevice
from adm6.hostnet6 import HostNet6
from sys import stdout
from os.path import expanduser as homedir
from ipaddr import IPv6Network

rule = {}

class ThisDevice_tests(unittest.TestCase):
    """
    some tests for class Ip6_Filter_Rule
    """

    def test_d_01_adm6_is_instance(self):
        """
        dv-01 ThisDevice: adm6 is instance
        """
        cfg = Adm6ConfigParser(".adm6.conf")
        hn6 = HostNet6()
        dev = ThisDevice('adm6', cfg, hn6)
        self.assertIsInstance(dev, ThisDevice)

    def test_d_02_unkn_is_not_instance(self):
        """
        dv-01 ThisDevice: unknown is not instance
        """
        cfg = Adm6ConfigParser(".adm6.conf")
        hn6 = HostNet6()
        try:
            dev = ThisDevice('unknown', cfg, hn6)
            value = True
        except:
            value = False
        self.assertFalse(value)
        #self.assertIsInstance(dev, ThisDevice)
        #print "F:", dev.interfaces_file
        #print "I:", dev.interfaces
        #print "L:", len(dev.interfaces)
        #self.assertFalse(True)
    