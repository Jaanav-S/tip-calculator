from decimal import Decimal

import pytest

from tipcalc import split, summarize, tip_amount, to_money


def test_to_money_rounds_half_up():
    assert to_money("2.345") == Decimal("2.35")
    assert to_money(1) == Decimal("1.00")


def test_tip_amount():
    assert tip_amount("100", 15) == Decimal("15.00")
    assert tip_amount("84.50", 18) == Decimal("15.21")


def test_tip_amount_rejects_negative():
    with pytest.raises(ValueError):
        tip_amount("10", -5)


def test_split_sums_to_total():
    shares = split(Decimal("99.71"), 3)
    assert sum(shares) == Decimal("99.71")
    assert shares == [Decimal("33.24"), Decimal("33.24"), Decimal("33.23")]


def test_split_round_up():
    assert split(Decimal("99.71"), 3, round_up=True) == [Decimal("34")] * 3


def test_split_needs_people():
    with pytest.raises(ValueError):
        split(Decimal("10"), 0)
