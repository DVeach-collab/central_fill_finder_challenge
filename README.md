# Central Fill Finder Challenge 

## Overview

This is a Python program I created for the Central Fill Finder coding challenge.

The program generates a set of Central Fill facilities at random locations
on a coordinate grid (X,Y 2D). Each facility gets a unique three-digit ID and
has three medications (A, B, and C), each with its own price.

The user enters their coordinates, and the program finds the three
closest facilities using Manhattan distance. 
Part of working through this challenge involved learning how Manhattan distance is calculated and applying the formula in Python.

For showing the results or the output, the program displays the facility ID,
the cheapest medication and its price, and the distance from the
user's location.

## Assumptions

I've tried to include assumptions made while reviewing instructions and working through the challenge coding:

- Coordinates are whole numbers between -10 and +10, including
  the boundaries.
- The coordinate grid has 441 possible locations (21 x 21),
  so the program cannot generate more than 441 unique facilities.
- Medication prices must be greater than zero, so they are randomly generated between $0.01 and
  $100.00.  
- A distance of zero is valid if the user and a facility are
  at the same location.
- If two facilities are the same distance from the user, I use the facility ID to determine their order. 
  The challenge didn't specify how to handle ties, so I added this logic to cover that situation.
- The program uses 30 randomly generated facilities. 
  This is a value I chose for testing and can be changed.
- Results show three closest facilities with cheapest medication price for central fill 
  The filter for only 3 can also be changed easily for additional values or data. 



## Design Decisions and Testing

I chose to break the program into separate functions because it
made things easier for me to follow as I worked through the challenge.
I used different functions for generating facilities, calculating
distance, and getting the user's coordinates.

After some initial testing, I decided to use random.sample() to
make sure two facilities wouldn't end up at the same location.
This seemed like a straightforward way to handle that requirement
without having to check for duplicates.

For medication prices, it uses whole numbers to represent
cents instead of working directly with dollars and decimals.
This helps avoid rounding issues when dealing with money.
When displaying the price, I divide by 100 to convert it to
dollars and use .2f to show two decimal places.

I also added automated tests to check that the main parts of
the program were working as expected. These cover distance
calculations, facility counts, unique locations, medication
prices, and some edge cases. 
This also follows along nicely to validate core points included in 
rules for the challenge. 

I tested the program manually as well, trying different
coordinates and incorrect inputs to see how it handled them.
This included negative coordinates, values outside the allowed
range, and locations where the distance was zero.

A lot of the manual testing helped me figure out what needed
to be adjusted as I worked through the code.


## Possible Changes

There are a few things I would change if the requirements
for this program were expanded.

### Multiple Facilities at the Same Location

Right now, I use random.sample() to make sure each facility
has its own coordinates.

If multiple facilities were allowed at the same location,
I would use random.choice() instead. This would allow the
same coordinates to be selected more than once.

Each facility would still have its own unique ID. I would
also need to adjust the current limit of 441 facilities,
since that limit is based on having one facility per location.

### Larger Geographic Area

The program currently uses a small grid with coordinates
between -10 and +10.

If the area were much larger, I would change how the
locations are generated. Right now, the program creates
a list of every possible coordinate before selecting
facility locations.

That works fine for a small grid, but it wouldn't be
practical for a very large area.

I would need to look at generating unique coordinates without
building the entire list first.


If the number of facilities also became much larger,
then consider a more efficient way to find the three
closest facilities instead of sorting the entire list.

For a real-world system with a lot of facilities, I would consider storing the locations in a database 
and using a more efficient way to search for nearby facilities.

### Supporting 3D Coordinates

Another possible change I pondered while coding is adding a third coordinate
(Z) to support three-dimensional locations. I didn't explore how practical this would be for the challenge, but 
I did think through what parts of the program would need to change.

I would update the facility generation and user input
to accept X, Y, and Z coordinates.

The Manhattan distance calculation would also need to
include the difference between the Z coordinates.

I would update the input validation and automated tests
to make sure the program handled the additional coordinate
correctly.

## How to Run Program and Tests

Instructions for running the program and automated tests
can be found in [RUN_INSTRUCTIONS.md](RUN_INSTRUCTIONS.md).
