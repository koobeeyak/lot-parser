#!/usr/bin/env python3

GBP_TO_USD_CONVERSION_RATE = 1.34

# TODO decide on if we return rounded int or float
def convert_amount(amount):
    """
    :type amount: basestring
    """
    amount = amount.replace(',', '')
    amount = int(amount)
    return amount


def gbp_to_usd(amount):
    amount = convert_amount(amount)
    return amount * GBP_TO_USD_CONVERSION_RATE


def usd_to_gbp(amount):
    amount = convert_amount(amount)
    return amount / GBP_TO_USD_CONVERSION_RATE
