#!/usr/bin/env python3

# 3p
from serpy import Serializer, StrField, Field

# project
from models.work_serializer import WorkSerializer


class ArtistSerializer(Serializer):
    artist = StrField(required=True, attr="name")
    works = WorkSerializer(required=True, many=True)
    total_value = Field(required=True, label="totalValue")
