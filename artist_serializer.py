#!/usr/bin/env python3

# 3p
from serpy import Serializer, StrField, Field


class ArtistSerializer(Serializer):
    artist = StrField(required=True, attr="name")
    works = Field(required=True)
