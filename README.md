# Cabinet Game
## Riddle
2 players are facing a cabinet with 2x4 cells, and told 2 cells contain a gold star (e.g. 3 and 6).
| | | | |
|-|-|-|-|
|1|2|**3**|4|
|5|**6**|7|8|
| | | | |

Each need to supply a scanning order to try to find one of the stars. The one which scan finds a
star on the lowest step, wins the game. If both scans find the star on the same step, the game is
a draw.

Player one selects: 1, 2, 3, 4, 5, 6, 7, 8 (Left to right scan)

Player two selects: 1, 5, 2, 6, 3, 7, 4, 8 (Top to bottom scan)

Does one of the players have a better chance of winning?

## Usage
```
usage: cabinet.py [-h] [-v] num_rows cabinets_per_row num_selections

positional arguments:
  num_rows          Number of rows of cabinets
  cabinets_per_row  Number of cabinets per row
  num_selections    Number of cabinets with prizes

options:
  -h, --help        show this help message and exit
  -v, --verbose     Print verbose output
```
To solve the riddle above, run `cabinet.py 2 4 2`. To see why that ratio was calculated, use `-v`.
