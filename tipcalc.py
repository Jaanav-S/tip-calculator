"""Split a bill between friends, with tip and optional rounding."""

import argparse
from decimal import Decimal, ROUND_DOWN, ROUND_HALF_UP, ROUND_UP

CENT = Decimal("0.01")


def to_money(value):
    """Round a value to whole cents."""
    return Decimal(str(value)).quantize(CENT, rounding=ROUND_HALF_UP)


def tip_amount(subtotal, percent):
    """Return the tip for a subtotal at the given percentage."""
    if Decimal(str(percent)) < 0:
        raise ValueError("tip percent cannot be negative")
    return to_money(to_money(subtotal) * Decimal(str(percent)) / 100)
