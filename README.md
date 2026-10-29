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

## How the split works

The total is divided into whole cents and any leftover cents go to the first
few people, so the shares always add up to exactly the total.

## Running the tests

```
python -m pytest
```

## Ideas

- Per-person items instead of an even split
- Currency symbols other than `$`
- Tax as a separate line
