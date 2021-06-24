# Day 3 - Perfectly Spherical Houses in a Vacuum

## Part One

### Problem

Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and
then an elf at the North Pole calls him via radio and tells him where to move
next. Moves are always exactly one house to the north (`^`), south (`v`), east
(`>`), or west (`<`). After each move, he delivers another present to the house
at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so
his directions are a little off, and Santa ends up visiting some houses more
than once. How many houses receive at least one present?

### Example

- `>` delivers presents to `2` houses: one at the starting location, and one to
the east.
- `^>v<` delivers presents to `4` houses in a square, including twice to the
house at his starting/ending location.
- `^v^v^v^v^v` delivers a bunch of presents to some very lucky children at only
`2` houses.

### Solution

If we represent santa by two coordinates, x and y, and update these each time a
new order is given we can save all the pairs so that there are no duplicates and
count them at the end. We can execute the program with:

```python partOne.py```

A total of 2081 houses will be visited

## Part Two

### Problem

The next year, to speed up the process, Santa creates a robot version of
himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the
same starting house), then take turns moving based on instructions from the elf,
who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

### Example

- `^v` delivers presents to `3` houses, because Santa goes north, and then
Robo-Santa goes south.
- `^>v<` now delivers presents to `3` houses, and Santa and Robo-Santa end up
back where they started.
- `^v^v^v^v^v` now delivers presents to `11` houses, with Santa going one
direction and Robo-Santa going the other.

### Solution

A few tweaks to the code from the first part are enough to solve part two. We
just need keep track of Robo-Santa as well as Santa and update the visited list
when either moves with their current position if it has not been visited yet and
count the amount of houses visited. We can execute the program with:

```python partTwo.py```

A total of 2341 houses will be visited
