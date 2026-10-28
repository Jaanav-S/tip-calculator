from decimal import Decimal

import pytest

from tipcalc import split, summarize, tip_amount, to_money


def test_to_money_rounds_half_up():
    assert to_money("2.345") == Decimal("2.35")
    assert to_money(1) == Decimal("1.00")
