"""
Starter Unit Tests using the built-in Python unittest library.
See https://docs.python.org/3/library/unittest.html

You can expand these to cover more cases!

To run the unit tests, use the following command in your terminal,
in the folder where this file exists:

    python src/tests.py -v

"""
import unittest

import logic


class AvoidHazardsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.test_board ={"height": 21, "width": 19, "food": [],"hazards":[
                {"x": 0, "y": 20},
                {"x": 2, "y": 20},
                {"x": 3, "y": 20},
                {"x": 4, "y": 20},
                {"x": 5, "y": 20},
                {"x": 6, "y": 20},
                {"x": 7, "y": 20},
                {"x": 8, "y": 20},
                {"x": 9, "y": 20},
                {"x": 10, "y": 20},
                {"x": 11, "y": 20},
                {"x": 12, "y": 20},
                {"x": 13, "y": 20},
                {"x": 14, "y": 20},
                {"x": 15, "y": 20},
                {"x": 16, "y": 20},
                {"x": 18, "y": 20},
                {"x": 0, "y": 19},
                {"x": 9, "y": 19},
                {"x": 18, "y": 19},
                {"x": 0, "y": 18},
                {"x": 2, "y": 18},
                {"x": 3, "y": 18},
                {"x": 5, "y": 18},
                {"x": 6, "y": 18},
                {"x": 7, "y": 18},
                {"x": 9, "y": 18},
                {"x": 11, "y": 18},
                {"x": 12, "y": 18},
                {"x": 13, "y": 18},
                {"x": 15, "y": 18},
                {"x": 16, "y": 18},
                {"x": 18, "y": 18},
                {"x": 0, "y": 17},
                {"x": 18, "y": 17},
                {"x": 0, "y": 16},
                {"x": 2, "y": 16},
                {"x": 3, "y": 16},
                {"x": 5, "y": 16},
                {"x": 7, "y": 16},
                {"x": 8, "y": 16},
                {"x": 9, "y": 16},
                {"x": 10, "y": 16},
                {"x": 11, "y": 16},
                {"x": 13, "y": 16},
                {"x": 15, "y": 16},
                {"x": 16, "y": 16},
                {"x": 18, "y": 16},
                {"x": 0, "y": 15},
                {"x": 5, "y": 15},
                {"x": 9, "y": 15},
                {"x": 13, "y": 15},
                {"x": 18, "y": 15},
                {"x": 0, "y": 14},
                {"x": 3, "y": 14},
                {"x": 5, "y": 14},
                {"x": 6, "y": 14},
                {"x": 7, "y": 14},
                {"x": 9, "y": 14},
                {"x": 11, "y": 14},
                {"x": 12, "y": 14},
                {"x": 13, "y": 14},
                {"x": 15, "y": 14},
                {"x": 18, "y": 14},
                {"x": 0, "y": 13},
                {"x": 3, "y": 13},
                {"x": 5, "y": 13},
                {"x": 13, "y": 13},
                {"x": 15, "y": 13},
                {"x": 18, "y": 13},
                {"x": 0, "y": 12},
                {"x": 1, "y": 12},
                {"x": 2, "y": 12},
                {"x": 3, "y": 12},
                {"x": 5, "y": 12},
                {"x": 7, "y": 12},
                {"x": 9, "y": 12},
                {"x": 11, "y": 12},
                {"x": 13, "y": 12},
                {"x": 15, "y": 12},
                {"x": 16, "y": 12},
                {"x": 17, "y": 12},
                {"x": 18, "y": 12},
                {"x": 7, "y": 11},
                {"x": 11, "y": 11},
                {"x": 0, "y": 10},
                {"x": 1, "y": 10},
                {"x": 2, "y": 10},
                {"x": 3, "y": 10},
                {"x": 5, "y": 10},
                {"x": 7, "y": 10},
                {"x": 9, "y": 10},
                {"x": 11, "y": 10},
                {"x": 13, "y": 10},
                {"x": 15, "y": 10},
                {"x": 16, "y": 10},
                {"x": 17, "y": 10},
                {"x": 18, "y": 10},
                {"x": 0, "y": 9},
                {"x": 3, "y": 9},
                {"x": 5, "y": 9},
                {"x": 13, "y": 9},
                {"x": 15, "y": 9},
                {"x": 18, "y": 9},
                {"x": 0, "y": 8},
                {"x": 3, "y": 8},
                {"x": 5, "y": 8},
                {"x": 7, "y": 8},
                {"x": 8, "y": 8},
                {"x": 9, "y": 8},
                {"x": 10, "y": 8},
                {"x": 11, "y": 8},
                {"x": 13, "y": 8},
                {"x": 15, "y": 8},
                {"x": 18, "y": 8},
                {"x": 0, "y": 7},
                {"x": 9, "y": 7},
                {"x": 18, "y": 7},
                {"x": 0, "y": 6},
                {"x": 2, "y": 6},
                {"x": 3, "y": 6},
                {"x": 5, "y": 6},
                {"x": 6, "y": 6},
                {"x": 7, "y": 6},
                {"x": 9, "y": 6},
                {"x": 11, "y": 6},
                {"x": 12, "y": 6},
                {"x": 13, "y": 6},
                {"x": 15, "y": 6},
                {"x": 16, "y": 6},
                {"x": 18, "y": 6},
                {"x": 0, "y": 5},
                {"x": 3, "y": 5},
                {"x": 15, "y": 5},
                {"x": 18, "y": 5},
                {"x": 0, "y": 4},
                {"x": 1, "y": 4},
                {"x": 3, "y": 4},
                {"x": 5, "y": 4},
                {"x": 7, "y": 4},
                {"x": 8, "y": 4},
                {"x": 9, "y": 4},
                {"x": 10, "y": 4},
                {"x": 11, "y": 4},
                {"x": 13, "y": 4},
                {"x": 15, "y": 4},
                {"x": 17, "y": 4},
                {"x": 18, "y": 4},
                {"x": 0, "y": 3},
                {"x": 5, "y": 3},
                {"x": 9, "y": 3},
                {"x": 13, "y": 3},
                {"x": 18, "y": 3},
                {"x": 0, "y": 2},
                {"x": 2, "y": 2},
                {"x": 3, "y": 2},
                {"x": 4, "y": 2},
                {"x": 5, "y": 2},
                {"x": 6, "y": 2},
                {"x": 7, "y": 2},
                {"x": 9, "y": 2},
                {"x": 11, "y": 2},
                {"x": 12, "y": 2},
                {"x": 13, "y": 2},
                {"x": 14, "y": 2},
                {"x": 15, "y": 2},
                {"x": 16, "y": 2},
                {"x": 18, "y": 2},
                {"x": 0, "y": 1},
                {"x": 18, "y": 1},
                {"x": 0, "y": 0},
                {"x": 2, "y": 0},
                {"x": 3, "y": 0},
                {"x": 4, "y": 0},
                {"x": 5, "y": 0},
                {"x": 6, "y": 0},
                {"x": 7, "y": 0},
                {"x": 8, "y": 0},
                {"x": 9, "y": 0},
                {"x": 10, "y": 0},
                {"x": 11, "y": 0},
                {"x": 12, "y": 0},
                {"x": 13, "y": 0},
                {"x": 14, "y": 0},
                {"x": 15, "y": 0},
                {"x": 16, "y": 0},
                {"x": 18, "y": 0}]
        }
        
    def test_hazards_left(self):
        #Arrange
        test_head =  {"x": 1, "y": 1}
        possible_moves = ["up", "down", "left", "right"]
        expected = ["up", "down", "right"]
        #Act
        result_moves = logic.avoid_hazards(test_head,self.test_board,possible_moves)
        #Assert
        self.assertEqual(len(result_moves), 3)
        self.assertEqual(expected, result_moves)

    def test_hazards_right(self):
        #Arrange
        test_head =  {"x": 17, "y": 1}
        possible_moves = ["up", "down", "left", "right"]
        expected = ["up", "down", "left"]
        #Act
        result_moves = logic.avoid_hazards(test_head,self.test_board,possible_moves)
        #Assert
        self.assertEqual(len(result_moves), 3)
        self.assertEqual(expected, result_moves)

    def test_hazards_up(self):
        #Arrange
        test_head =  {"x": 4, "y": 19}
        possible_moves = ["up", "down", "left", "right"]
        expected = ["down", "left","right"]
        #Act
        result_moves = logic.avoid_hazards(test_head,self.test_board,possible_moves)
        #Assert
        self.assertEqual(len(result_moves), 3)
        self.assertEqual(expected, result_moves)

    def test_hazards_down(self):

        #Arrange
        test_head =  {"x": 8, "y": 1}
        possible_moves = ["up", "down", "left", "right"]
        expected = ["up", "left","right"]
        #Act
        result_moves = logic.avoid_hazards(test_head,self.test_board,possible_moves)
        #Assert
        self.assertEqual(len(result_moves), 3)
        self.assertEqual(expected, result_moves)

    def test_hazards_tunnel(self):
        #Arrange
        test_head =  {"x": 2, "y": 11}
        possible_moves = ["up", "down", "left", "right"]
        expected = ["left","right"]
        #Act
        result_moves = logic.avoid_hazards(test_head,self.test_board,possible_moves)
        #Assert
        self.assertEqual(len(result_moves), 2)
        self.assertEqual(expected, result_moves)

    def test_hazards_corner(self):
        #Arrange
        test_head =  {"x": 1, "y": 3}
        possible_moves = ["up", "down", "left", "right"]
        expected = ["down","right"]
        #Act
        result_moves = logic.avoid_hazards(test_head,self.test_board,possible_moves)
        #Assert
        self.assertEqual(len(result_moves), 2)
        self.assertEqual(expected, result_moves)


class AvoidNeckTest(unittest.TestCase):
    def test_avoid_neck_all(self):
        # Arrange
        test_body = [{"x": 5, "y": 5}, {"x": 5, "y": 5}, {"x": 5, "y": 5}]
        possible_moves = ["up", "down", "left", "right"]

        # Act
        result_moves = logic._avoid_my_neck(test_body, possible_moves)

        # Assert
        self.assertEqual(len(result_moves), 4)
        self.assertEqual(possible_moves, result_moves)

    def test_avoid_neck_left(self):
        # Arrange
        test_body = [{"x": 5, "y": 5}, {"x": 4, "y": 5}, {"x": 3, "y": 5}]
        possible_moves = ["up", "down", "left", "right"]
        expected = ["up", "down", "right"]

        # Act
        result_moves = logic._avoid_my_neck(test_body, possible_moves)

        # Assert
        self.assertEqual(len(result_moves), 3)
        self.assertEqual(expected, result_moves)

    def test_avoid_neck_right(self):
        # Arrange
        test_body = [{"x": 5, "y": 5}, {"x": 6, "y": 5}, {"x": 7, "y": 5}]
        possible_moves = ["up", "down", "left", "right"]
        expected = ["up", "down", "left"]

        # Act
        result_moves = logic._avoid_my_neck(test_body, possible_moves)

        # Assert
        self.assertEqual(len(result_moves), 3)
        self.assertEqual(expected, result_moves)

    def test_avoid_neck_up(self):
        # Arrange
        test_body = [{"x": 5, "y": 5}, {"x": 5, "y": 6}, {"x": 5, "y": 7}]
        possible_moves = ["up", "down", "left", "right"]
        expected = ["down", "left", "right"]

        # Act
        result_moves = logic._avoid_my_neck(test_body, possible_moves)

        # Assert
        self.assertEqual(len(result_moves), 3)
        self.assertEqual(expected, result_moves)

    def test_avoid_neck_down(self):
        # Arrange
        test_body = [{"x": 5, "y": 5}, {"x": 5, "y": 4}, {"x": 5, "y": 3}]
        possible_moves = ["up", "down", "left", "right"]
        expected = ["up", "left", "right"]

        # Act
        result_moves = logic._avoid_my_neck(test_body, possible_moves)

        # Assert
        self.assertEqual(len(result_moves), 3)
        self.assertEqual(expected, result_moves)


if __name__ == "__main__":
    unittest.main()
