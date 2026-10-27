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


def split(total, people, round_up=False):
    """Split a total between people.

    Shares always sum to the total, except with round_up where everyone
    pays the same whole-dollar amount.
    """
    if people < 1:
        raise ValueError("need at least one person")
    total = to_money(total)
    if round_up:
        share = (total / people).quantize(Decimal("1"), rounding=ROUND_UP)
        return [share] * people
    base = (total / people).quantize(CENT, rounding=ROUND_DOWN)
    shares = [base] * people
    leftover = int((total - base * people) / CENT)
    for i in range(leftover):
        shares[i] += CENT
    return shares


def summarize(subtotal, percent, people, round_up=False):
    """Compute everything needed to print a bill."""
    tip = tip_amount(subtotal, percent)
    total = to_money(subtotal) + tip
    return {
        "subtotal": to_money(subtotal),
        "tip": tip,
        "total": total,
        "shares": split(total, people, round_up),
    }


def format_summary(summary, percent):
    shares = ", ".join(f"${s}" for s in summary["shares"])
    tip_label = f"Tip ({percent}%):"
    return "\n".join([
        f"{'Subtotal:':<12}${summary['subtotal']}",
        f"{tip_label:<12}${summary['tip']}",
        f"{'Total:':<12}${summary['total']}",
        f"{'Each pays:':<12}{shares}",
    ])


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Split a bill, tip included.")
    parser.add_argument("subtotal", type=Decimal, help="bill before tip")
    parser.add_argument("--tip", type=Decimal, default=Decimal("15"), help="tip percent (default 15)")
    parser.add_argument("--people", type=int, default=1, help="number of people splitting")
    parser.add_argument("--round-up", action="store_true", help="round each share up to whole dollars")
    return parser.parse_args(argv)
