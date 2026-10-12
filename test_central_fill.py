import unittest

from central_fill_finder_challenge import (
    manhattan_distance,
    generate_central_fills
)


class TestCentralFill(unittest.TestCase):

    def test_manhattan_distance(self):
        # Verify the distance between two different locations.
        self.assertEqual(manhattan_distance(4, 2, 1, 1), 4)

    def test_zero_distance(self):
        # Two identical locations should have a distance of zero.
        self.assertEqual(manhattan_distance(4, 2, 4, 2), 0)

    def test_negative_coordinates(self):
        # Verify that negative coordinates are handled correctly.
        self.assertEqual(manhattan_distance(4, 2, -6, -8), 20)

    def test_facility_count(self):
        # The number of generated facilities should match the request.
        central_fills = generate_central_fills(30)
        self.assertEqual(len(central_fills), 30)

    def test_unique_locations(self):
        # No two Central Fills should occupy the same coordinates.
        central_fills = generate_central_fills(100)

        locations = [
            (fill["x"], fill["y"])
            for fill in central_fills
        ]

        self.assertEqual(len(locations), len(set(locations)))

    def test_positive_medication_prices(self):
        # Every facility must have medications A, B, and C.
        # Each medication must have a price greater than zero.
        central_fills = generate_central_fills(30)

        for fill in central_fills:
            medications = fill["medications"]

            self.assertEqual(set(medications), {"A", "B", "C"})

            for price in medications.values():
                self.assertGreater(price, 0)

    def test_facility_limit(self):
        # The grid supports at most 441 unique locations.
        with self.assertRaises(ValueError):
            generate_central_fills(442)

    def test_zero_facilities(self):
        # At least one facility must be generated.
        with self.assertRaises(ValueError):
            generate_central_fills(0)


if __name__ == "__main__":
    unittest.main()