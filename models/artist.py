#!/usr/bin/env python3

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
