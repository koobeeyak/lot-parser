#!/usr/bin/env python3

# std
import re

# 3p
from bs4 import BeautifulSoup

# project
from models.artist import Artist
from models.work import Work


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
        soup = BeautifulSoup(self.page_content, "html.parser")
        name_heading = soup.h2.text
        self.name = self.clean_name(name_heading)
        work_name = soup.h3.text
        work_currency_and_price = soup.find_all('div')[1].text
        work_currency, work_price = work_currency_and_price.split(' ')
        work = Work(work_name, work_currency, work_price)
        self.works.append(work)

    def run(self):
        self._scrape()
        return Artist(
            self.name,
            self.works,
        )
