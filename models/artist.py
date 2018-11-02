#!/usr/bin/env python3

# std
from functools import reduce
from operator import add

# project
from models.work import Work


class Artist(object):
    def __init__(self, name, works):
        """
        :type name: basestring
        :type works: list[Work]
        """
        self.name = name
        self.works = works

    @property
    def total_value(self):
        return reduce(add, [w.price for w in self.works])
