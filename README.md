# SpaceOctopi

A short game about placing tiles, and collecting stars on your journey through space. 
Uses the Pygame library.

## How to play

To begin, each player places a tile, with at least one path connected to the outer lines of the board.
Each consecutive tile placed must have a path from a tile of the same color (this is not hard-coded, ensure you watch your enemies!)
You can place tiles on top of any other tile, so long as it connects to your "path".
Placing a tile on top of a tile with a yellow star on it earns you 1 point.

## Tile placing mechanics
Use keys 'a' or 'd' to change your tile selection. 
Use arrow keys <- or -> to rotate your tile.
Once you are happy with your tile selection, hover your mouse over the square you would like to place it on, then press SPACE to place it.

## Future improvements
- Show transparent tile on board moving with cursor before placement.
- Reduce pixellisation from rotation.
- Hard code path connection rules.
- Remove ability to get star points from your own tiles.