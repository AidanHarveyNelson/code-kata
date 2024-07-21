# Problem 1 Parsing Solution

My solution for building a fixed width parser that outputs into CSV format.
Commands to run and test are below

## Running Python Directly
### Run main script
```
python main.py --output results --records 2000
```

### Run test script
```
python -m unittest discover -s .
```

## Running Through Docker
```
docker build -t problem1 .
```

### Run main script
```
docker run -v $PWD/output:/software/output problem1
```

### Run test script
```
docker run problem1 python -m unittest discover -s .
```
