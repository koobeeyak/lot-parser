#!/usr/bin/env python3


class Work(object):
    def __init__(self, name, currency, price):
        """
        :type name: basestring
        :type works: basestring
        """
        self.name = name
        self.currency = currency
        self.price = price
