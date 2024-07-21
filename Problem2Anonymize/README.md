# Problem 2 Anonymize Solution

My solution for building a tool to anonymize data
Commands to run and test are below

## Running Python Directly

## Run small parser function

```
python main.py -r 10000 -o output
```

## Run large parser function

```
python main.py -r 50000000 -o output -p
```

### Compare speeds of two functions

Compares the execution time of the two functions against the following record counts:
- 100
- 10000
- 1000000
- 10000000
- 50000000

```
python speed_test.py
```
