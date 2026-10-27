"""Split a bill between friends, with tip and optional rounding."""

import argparse
from decimal import Decimal, ROUND_DOWN, ROUND_HALF_UP, ROUND_UP

CENT = Decimal("0.01")


def to_money(value):
    """Round a value to whole cents."""
    return Decimal(str(value)).quantize(CENT, rounding=ROUND_HALF_UP)
