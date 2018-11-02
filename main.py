#!/usr/bin/env python3

# std
from os import path, walk
import pprint

# project
from models.artist_serializer import ArtistSerializer
from artist_scrapers.artist_scraper_2015 import ArtistScraper2015


SCRAPERS = {
    '2015-03-18': ArtistScraper2015,
}


# TODO implement better logic: read all files first, THEN parse them
def main():
    artists = []
    for root, dirs, files in walk('data'):
        for f in files:
            dir_name = path.basename(root)
            if '2015' in dir_name:  # ignore 2017 in first few steps
                with open(path.join(root, f), "r") as open_file:
                    page_content = open_file.read()
                    scraper = SCRAPERS[dir_name](page_content)
                    artists.append(scraper.run())
    serialized_artists = [ArtistSerializer(artist).data for artist in artists]
    pprint.pprint(serialized_artists)


if __name__ == "__main__":
    main()
