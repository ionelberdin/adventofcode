# Day 6: Trash Compactor
https://adventofcode.com/2025/day/6

## Part 1
Parsing needs to be done for the whole file and then apply the operators iteratively.

The reduce function from `functools` comes handy for this purpose:

```python
OPERATORS = {
    '+': lambda x, y: x+y,
    '*': lambda x, y: x*y
}

#...file processing...
# lines:list[list[int]] contains all numeric lines as lists of integers
# operators:list[str] contains a list of all operators in str format

result = 0 
for i, operator in enumerate(operators):
    result += reduce(OPERATORS[operator], [x[i] for x in lines])
```

```
Solving part 1 with: test.txt
Result of part 1: 4277556 (0.0002586999908089638s)
Solving part 1 with: puzzle.txt
Result of part 1: 5877594983578 (0.002976899966597557s)
```

## Part 2
The second part requires a different type of processing, but the idea is the same.

```python
result = 0 
numbers = []
for i in range(len(lines[0])-1,-1,-1):
    numbers.append('')
    for n in range(len(lines)-1):
        numbers[-1] += lines[n][i] if lines[n][i] != ' ' else ''
    if numbers[-1] == '':
        numbers.pop()
    if lines[-1][i] in '+*':
        result += reduce(OPERATORS[lines[-1][i]], map(int, numbers))
        numbers = []
```

```
Solving part 2 with: test.txt
Result of part 2: 3263827 (0.00023799994960427284s)
Solving part 2 with: puzzle.txt
Result of part 2: 11159825706149 (0.004394000046886504s) 
```