#!/usr/bin/env python3

# 3p
from serpy import Serializer, StrField


class WorkSerializer(Serializer):
    name = StrField(required=True)
    currency = StrField(required=True)
    price = StrField(required=True)
