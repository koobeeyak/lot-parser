#!/usr/bin/env python3


class Artist(object):
    def __init__(self, name, works):
        """
        :type name: basestring
        :type works: list[basestring]
        """
        self.name = name
        self.works = works
