"""Split a bill between friends, with tip and optional rounding."""

import argparse
from decimal import Decimal, ROUND_DOWN, ROUND_HALF_UP, ROUND_UP
