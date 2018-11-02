#!/usr/bin/env python3

# std
import re

# 3p
from bs4 import BeautifulSoup

# project
from artist import Artist


class ArtistScraper2015(object):
    """
    Use to parse artist web pages from 2015
    """
    def __init__(self, page_content):
        """
        :type page_content: basestring
        """
        self.page_content = page_content
        self.name = None

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
        soup = BeautifulSoup(self.page_content, "html.parser")
        name_heading = soup.h2.text
        self.name = self.clean_name(name_heading)

    def run(self):
        self._scrape()
        return Artist(
            self.name
        )
