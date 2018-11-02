#!/usr/bin/env python3

# 3p
from bs4 import BeautifulSoup

# project
from artist_scrapers.artist_scraper import ArtistScraper
from models.artist import Artist
from models.work import Work
from utils.conversions import gbp_to_usd


class ArtistScraper2015(ArtistScraper):
    """
    Use to parse artist web pages from 2015
    """

    def _parse_name(self, soup):
        name = soup.h2.text
        name = self.clean_name(name)
        return name

    @staticmethod
    def _parse_work(soup):
        work_name = soup.h3.text
        work_currency_and_price = soup.find_all('div')[1].text
        work_currency, work_price = work_currency_and_price.split(' ')
        if work_currency != 'USD':
            work_price = gbp_to_usd(work_price)
            work_currency = 'USD'
        work = Work(work_name, work_currency, work_price)
        return work

    def _scrape(self):
        soup = BeautifulSoup(self.page_content, "html.parser")
        self.name = self._parse_name(soup)
        self.works.append(self._parse_work(soup))

    def run(self):
        self._scrape()
        return Artist(
            self.name,
            self.works,
        )
