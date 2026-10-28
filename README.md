# tipcalc

A tiny command-line tool for splitting a restaurant bill between friends,
tip included. Uses `Decimal` so the cents always add up.

## Usage

```
python tipcalc.py 84.50 --tip 18 --people 3
```

```
Subtotal:   $84.50
Tip (18%):  $15.21
Total:      $99.71
Each pays:  $33.24, $33.24, $33.23
```

Add `--round-up` to have everyone pay a whole number of dollars.
