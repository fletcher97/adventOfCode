# Day 1 - Not Quite Lisp

## Part One

### Problem

Santa is trying to deliver presents in a large apartment building, but he can't
find the right floor - the directions he got are a little confusing. He starts
on the ground floor (floor 0) and then follows the instructions one character at
a time

An opening parenthesis, `(`, means he should go up one floor, and a closing
parenthesis, `)`, means he should go down one floor.

The apartment building is very tall, and the basement is very deep; he will
never find the top or bottom floors.

### Example

- `(())` and `()()` both result in floor 0.
- `(((` and `(()(()(` both result in floor 3.
- `))(((((` also results in floor 3.
- `())` and `))(` both result in floor -1 (the first basement level).
- `)))` and `)())())` both result in floor -3.

### [Solution](partOne.sh)

To get the right floor one need to get the amount of occurences of each simbol
`(`, `)` and subtract the amount of floors santa needs to go down from the
amount of floors he needs to go up. Assuming a file named input contains the
instructions, to get the amount of occurences of a given character we can use
the followinf line in a terminal

```cat input | awk -F"<character>" '{print NF-1}'```

There are a total of 3616 `(` and 3384 `)`. Santa needs to go up 3616 and down
3384 which means he will end up at floor 232

## Part Two

### Problem

Now, given the same instructions, find the position of the first character that
causes him to enter the basement (floor -1). The first character in the
instructions has position 1, the second character has position 2, and so on.

### Example

- `)` causes him to enter the basement at character position 1.
- `()())` causes him to enter the basement at character position 5.

### [Solution](partTwo.sh)

To know the character's position when santa first enters the basement it's best
to write a script. We keep track of santa's position and when he goes
underground we print the number of instructions executed so far.

Running the script we get the position 1783
