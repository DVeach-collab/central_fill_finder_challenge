# Running the Central Fill Finder

The program uses Python 3 and does not require any additional packages.

## Running the Program

1. Download the repository.
2. Open Command Prompt in the project folder.
3. Enter the following command:

```cmd
python central_fill_finder_challenge.py
```

4. When prompted, enter coordinates in the format x,y (example: 4,2).

The program will display the three closest Central Fill facilities,
including the cheapest medication, its price, and the distance.

## Running the Tests

Open Command Prompt in the same project folder and enter:

```cmd
python -m unittest -v
```

This runs the eight automated tests included in test_central_fill.py.

All eight tests passed during development.