#!/usr/bin/env python3

# 3p
from bs4 import BeautifulSoup

# project
from artist_scrapers.artist_scraper import ArtistScraper
from models.artist import Artist
from models.work import Work


class ArtistScraper2017(ArtistScraper):
    """
    Use to parse artist web pages from 2017
    """
    def _parse_name(self, soup):
        name = soup.find_all('h3', {'class': 'artist'})[0].text
        name = self.clean_name(name)
        return name

    @staticmethod
    def _parse_work(soup):
        work_name = soup.h3.text
        work_currency, work_price = [s.text for s in soup.find_all('span')]
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
