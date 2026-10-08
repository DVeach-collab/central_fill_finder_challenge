# Central Fill Coding Challenge 
# Code any language - Python with Github selected as initial approach
# State Assumptions - Provide some asssumptions with code and readme file for broader discussion points. 
# The Manhattan distance formula calculates the total distance between two points by adding the absolute differences 
# of their coordinates, moving only in a grid-like path 
# Assumption: Coordinates are integers from -10 through +10 on each axis.
# This creates a 21 x 21 grid with 441 possible unique locations.

#---------------------------------------------------------
# Calculate the Manhattan Distance between two coordinates.
# Research shows this 2D Formula: |x1 - x2| + |y1 - y2| 
#---------------------------------------------------------

def manhattan_distance(x1, y1, x2, y2):
    # abs function added to assure each coordinate difference stays positive
    return abs(x1 - x2) + abs(y1 - y2)

def main():
    # Use fixed coordinates to verify the distance calculation. 
    user_x = 4
    user_y = 2

    fill_x = 0
    fill_y = 1

    filldistance = manhattan_distance(user_x, user_y, fill_x, fill_y)

    print("The Distance to Central Fill:", filldistance)


if __name__ == "__main__":
    main()