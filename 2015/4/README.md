# Day 4 - The Ideal Stocking Stuffer

## Part One

### Problem

Santa needs help [mining](https://en.wikipedia.org/wiki/Bitcoin#Mining) some
AdventCoins (very similar to [bitcoins](https://en.wikipedia.org/wiki/Bitcoin))
to use as gifts for all the economically forward-thinking little girls and boys.

To do this, he needs to find [MD5](https://en.wikipedia.org/wiki/MD5) hashes
which, in [hexadecimal](https://en.wikipedia.org/wiki/Hexadecimal), start with
at least five zeroes. The input to the MD5 hash is some secret key (your puzzle
input, given below) followed by a number in decimal. To mine AdventCoins, you
must find Santa the lowest positive number (no leading zeroes: `1`, `2`, `3`,
...) that produces such a hash.

### Example

- If your secret key is `abcdef`, the answer is `609043`, because the MD5 hash
of `abcdef609043` starts with five zeroes (`000001dbbfa...`), and it is the
lowest such number to do so.
- If your secret key is `pqrstuv`, the lowest number it combines with to make an
MD5 hash starting with five zeroes is `1048970`; that is, the MD5 hash of
`pqrstuv1048970` looks like `000006136ef....`

### Solution

We can make a bash script to calculate every MD5 hash composed of the input
followed by number. We start at 1 and keep going until we find a hash that
fullfils the requirements. We can execute the program with:

```bash partOne.sh```

## Part Two

### Problem

### Example

### Solution
