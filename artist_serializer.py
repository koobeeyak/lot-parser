#!/usr/bin/env python3

# 3p
from serpy import Serializer, StrField


class ArtistSerializer(Serializer):
    artist = StrField(required=True, attr="name")
