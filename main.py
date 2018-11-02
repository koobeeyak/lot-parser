#!/usr/bin/env python3

# std
from os import path, walk
import pprint

# project
from models.artist_serializer import ArtistSerializer
from artist_scrapers.artist_scraper_2015 import ArtistScraper2015
from artist_scrapers.artist_scraper_2017 import ArtistScraper2017


SCRAPERS = {
    '2015-03-18': ArtistScraper2015,
    '2017-12-20': ArtistScraper2017,
}


# TODO implement better logic: read all files first, THEN parse them. This way, we add works to an existing artist
def main():
    artists = []
    for root, dirs, files in walk('data'):
        for f in files:
            dir_name = path.basename(root)
            with open(path.join(root, f), "r") as open_file:
                page_content = open_file.read()
                scraper = SCRAPERS[dir_name](page_content)
                artists.append(scraper.run())
    serialized_artists = [ArtistSerializer(artist).data for artist in artists]
    pprint.pprint(serialized_artists)


if __name__ == "__main__":
    main()
