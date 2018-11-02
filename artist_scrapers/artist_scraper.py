#!/usr/bin/env python3

# std
import re


class ArtistScraper(object):
    """
    Use to parse artist web pages
    """
    def __init__(self, page_content):
        """
        :type page_content: basestring
        """
        self.page_content = page_content
        self.name = None
        self.works = []

    @staticmethod
    def clean_name(name):
        """
        Regex clean name.
        Louis Marcoussis (1883-1941) --> Louis Marcoussis
        Rembrandt Harmensz. --> Rembrandt Harmensz.
        """
        # TODO improve, make faster, for now only replaces numbers and '(', '-', ')'
        name = re.sub('([\d\(\)\-])+', '', name)
        name = name.strip()
        return name

    def _scrape(self):
        pass

    def run(self):
        pass
