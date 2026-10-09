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
# Dont forget Import random:) 
import random

def manhattan_distance(x1, y1, x2, y2):
    # abs function added to it returns absolute value of each coordinate difference
    return abs(x1 - x2) + abs(y1 - y2)

# Seed or Generate Central Fill facilities with unique random coordinates.
def generate_central_fills(count):

    # Assumption per the challenge,coordinate range is -10 to 10 (includes 0). This means a 441 possible locations on a 21 x 21 grid.
    if count < 1 or count > 441:
        raise ValueError("Central Fill count must be between 1 and 441.")

    # Create all options for the pair of coordinates. 
    # Assumption: By setting up this logic, one could expand to the 3D Manhattan model for Z coordinates by adding changes for z below and revising 441 limit above
    available_locations = [
        (x, y)
        for x in range(-10, 11)
        for y in range(-10, 11)
    ]

    # Select random locations without selecting the same one twice.
    selected_locations = random.sample(available_locations, count)

    central_fills = []

    # Create each Central Fill with an ID, location, and medication prices (1 to 10000 cents)
    for number, (x, y) in enumerate(selected_locations, start=1):

        fill = {
            "id": f"{number:03}",
            "x": x,
            "y": y,
            "medications": {
                "A": random.randint(1, 10000),
                "B": random.randint(1, 10000),
                "C": random.randint(1, 10000)
            }
        }

        # Add this facility to our list.
        central_fills.append(fill)

    # Return the completed list after all facilities are generated.
    return central_fills

def main():
    # Use fixed coordinates to verify the distance calculation. 
    user_x = 4
    user_y = 2

    # Generate random Central Fill facilities 10x 
    central_fills = generate_central_fills(10)

    # Display fill and its distance from the location 
    for fill in central_fills:

        fill_distance = manhattan_distance(
            user_x,
            user_y,
            fill["x"],
            fill["y"]
        )

        # Identify the least expensive medication at this Central Fill.
        medications = fill["medications"]

        cheapest_medication = min(medications, key=medications.get)
        cheapest_price = medications[cheapest_medication]

        # Output for Fill ID, Location, Distance, and Medication (converted to dollars using 2f option for floating integer 2 places) 
        print(
            f"Central Fill {fill['id']} - "
            f"Location ({fill['x']}, {fill['y']}), "
            f"Distance {fill_distance}, "
            f"Medication A: ${fill['medications']['A'] / 100:.2f}, "
            f"Medication B: ${fill['medications']['B'] / 100:.2f}, "
            f"Medication C: ${fill['medications']['C'] / 100:.2f}, "
            f"Cheapest: Medication {cheapest_medication}, "
            f"${cheapest_price / 100:.2f}"
        )

if __name__ == "__main__":
    main()
