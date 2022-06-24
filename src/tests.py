"""
Starter Unit Tests using the built-in Python unittest library.
See https://docs.python.org/3/library/unittest.html

You can expand these to cover more cases!

To run the unit tests, use the following command in your terminal,
in the folder where this file exists:

    python src/tests.py -v

"""
from lib2to3.pgen2.tokenize import untokenize
import unittest
from unittest import result

import logic

class AvoidSelfTest(unittest.TestCase):
    def setUp(self) -> None:
        self.possible_moves =["up", "down", "left", "right"]

    def test_avoid_neck_all(self):
        # Arrange
        test_body = [{"x": 5, "y": 5}, {"x": 5, "y": 5}, {"x": 5, "y": 5}]
        # Act
        result_moves = logic._avoid_self(test_body, self.possible_moves)
        # Assert
        self.assertEqual(len(result_moves), 4)
        self.assertEqual(self.possible_moves, result_moves)

    def test_avoid_neck_left(self):
        # Arrange
        test_body = [{"x": 5, "y": 5}, {"x": 4, "y": 5}, {"x": 3, "y": 5}]
        expected = ["up", "down", "right"]

        # Act
        result_moves = logic._avoid_self(test_body, self.possible_moves)

        # Assert
        self.assertEqual(len(result_moves), 3)
        self.assertEqual(expected, result_moves)

    def test_avoid_neck_right(self):
        # Arrange
        test_body = [{"x": 5, "y": 5}, {"x": 6, "y": 5}, {"x": 7, "y": 5}]
        expected = ["up", "down", "left"]

        # Act
        result_moves = logic._avoid_self(test_body, self.possible_moves)

        # Assert
        self.assertEqual(len(result_moves), 3)
        self.assertEqual(expected, result_moves)

    def test_avoid_neck_up(self):
        # Arrange
        test_body = [{"x": 5, "y": 5}, {"x": 5, "y": 6}, {"x": 5, "y": 7}]
        expected = ["down", "left", "right"]

        # Act
        result_moves = logic._avoid_self(test_body, self.possible_moves)

        # Assert
        self.assertEqual(len(result_moves), 3)
        self.assertEqual(expected, result_moves)

    def test_avoid_neck_down(self):
        # Arrange
        test_body = [{"x": 5, "y": 5}, {"x": 5, "y": 4}, {"x": 5, "y": 3}]
        expected = ["up", "left", "right"]

        # Act
        result_moves = logic._avoid_self(test_body, self.possible_moves)

        # Assert
        self.assertEqual(len(result_moves), 3)
        self.assertEqual(expected, result_moves)

    def test_tail_chase_two_sides(self):
        # Arrange
        test_body = [{"x": 5, "y": 5}, {"x": 5, "y": 4}, {"x": 4, "y": 4},{"x": 4, "y": 5}]
        expected = ["up","left", "right"]

        # Act
        result_moves = logic._avoid_self(test_body, self.possible_moves)

        # Assert
        self.assertEqual(len(result_moves), 3)
        self.assertEqual(expected, result_moves)

    def test_body_two_sides(self):
        # Arrange
        test_body = [{"x": 5, "y": 5}, {"x": 5, "y": 4},
        {"x": 4, "y": 4},{"x": 4, "y": 5},{"x": 4, "y": 6}]
        expected = ["up","right"]

        # Act
        result_moves = logic._avoid_self(test_body, self.possible_moves)

        # Assert
        self.assertEqual(len(result_moves), 2)
        self.assertEqual(expected, result_moves)

    def test_tail_chase_three_sides(self):
        # Arrange
        test_body = [{"x": 5, "y": 5}, {"x": 5, "y": 4},
        {"x": 4, "y": 4},{"x": 4, "y": 5},{"x": 4, "y": 6},{"x": 5, "y": 6}]
        expected = ["up", "right"]

        # Act
        result_moves = logic._avoid_self(test_body, self.possible_moves)

        # Assert
        self.assertEqual(len(result_moves), 2)
        self.assertEqual(expected, result_moves)

    def test_body_three_sides(self):
        # Arrange
        test_body = [{"x": 5, "y": 5}, {"x": 5, "y": 4},
        {"x": 4, "y": 4},{"x": 4, "y": 5},{"x": 4, "y": 6},{"x": 5, "y": 6},{"x": 6, "y": 6}]
        expected = ["right"]

        # Act
        result_moves = logic._avoid_self(test_body, self.possible_moves)

        # Assert
        self.assertEqual(len(result_moves), 1)
        self.assertEqual(expected, result_moves)

class AvoidSelfTrap(unittest.TestCase):
    pass
    #Tail chase other snakes
    #tail chase myself
    #prefer hitting myself over others unless head to head and will win
    #unless bigger head to head
    #go after biggest snake if more than 1
    #"""{'id': 'gs_XXcDWBMbV8wgS3BwwJ9hxQC4', 'name': 'Monty', 'latency': '165', 'health': 77, 'body': [{'x': 4, 'y': 1}, {'x': 3, 'y': 1}, {'x': 2, 'y': 1}, {'x': 1, 'y': 1},
# {'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 3}, {'x': 3, 'y': 3}, {'x': 4, 'y': 3}, {'x': 4, 'y': 4}, {'x': 4, 'y': 5}, {'x': 4, 'y': 6}, {'x': 4, 'y': 7},
# {'x': 5, 'y': 7}, {'x': 6, 'y': 7}, {'x': 6, 'y': 8}, {'x': 6, 'y': 9}], 'head': {'x': 4, 'y': 1}, 'length': 17, 'shout': '', 'squad': '',
 #'customizations': {'color': '#885588', 'head': 'silly', 'tail': 'bolt'}},

#{'id': 'gs_pPXPVBSS3bPWcfDX9vchP49b', 'name': 'Monty-Dev', 'latency': '181', 'health': 97, 'body': [{'x': 6, 'y': 1}, {'x': 7, 'y': 1}, {'x': 8, 'y': 1}, {'x': 9, 'y': 1},
# {'x': 10, 'y': 1}, {'x': 10, 'y': 2}, {'x': 10, 'y': 3}, {'x': 11, 'y': 3}, {'x': 12, 'y': 3}, {'x': 12, 'y': 4}, {'x': 12, 'y': 5}, {'x': 11, 'y': 5}, {'x': 10, 'y': 5},
# {'x': 9, 'y': 5}], 'head': {'x': 6, 'y': 1}, 'length': 14, 'shout': '', 'squad': '', 'customizations': {'color': '#885588', 'head': 'silly', 'tail': 'bolt'}}],
#""""


class AvoidOthersTest(unittest.TestCase):
    #tail chase others
    # head hunt only if bigger
    def setUp(self) -> None:
        self.possible_moves =["up", "down", "left", "right"]
    
    def test_avoid_others_body_left(self):
        # Arrange 
        test_my_snake = {'id': 'gs_pPXPVBSS3bPWcfDX9vchP49b',
        'body': [{'x': 6, 'y': 1},{'x': 7, 'y': 1}, {'x': 8, 'y': 1},
         {'x': 9, 'y': 1}],'length': 14,}

        test_snakes =[
        {'id': 'gs_pPXPVBSS3bPWcfDX9vchP49b',
        'body': [{'x': 6, 'y': 1},{'x': 7, 'y': 1}, {'x': 8, 'y': 1}],
         'length': 3,},
         
         {'id': 'gs_XXcDWBMbV8wgS3BwwJ9hxQC4',
         'body': [{'x': 5, 'y': 2}, {'x': 5, 'y': 1}, {'x': 5, 'y': 0},{'x': 4, 'y': 0}],
         'length': 4}]

        expected = ["up","down","right"]
        # Act
        result_moves = logic._avoid_others(test_my_snake,self.possible_moves,test_snakes)
        # Assert
        self.assertEqual(len(result_moves), 3)
        self.assertEqual(expected, result_moves)

    def test_avoid_others_body_right(self):
        # Arrange 
        test_my_snake = {'id': 'gs_pPXPVBSS3bPWcfDX9vchP49b',
        'body': [{'x': 6, 'y': 1},{'x': 5, 'y': 1}, {'x': 4, 'y': 1},
         {'x': 9, 'y': 1}],'length': 14,}

        test_snakes =[
        {'id': 'gs_pPXPVBSS3bPWcfDX9vchP49b',
        'body': [{'x': 6, 'y': 1},{'x': 5, 'y': 1}, {'x': 4, 'y': 1}],
         'length': 3,},
         
         {'id': 'gs_XXcDWBMbV8wgS3BwwJ9hxQC4',
         'body': [{'x': 7, 'y': 2}, {'x': 7, 'y': 1}, {'x': 7, 'y': 0}, {'x': 8, 'y': 0}],
         'length': 4}]

        expected = ["up","down","left"]
        # Act
        result_moves = logic._avoid_others(test_my_snake,self.possible_moves,test_snakes)
        # Assert
        self.assertEqual(len(result_moves), 3)
        self.assertEqual(expected, result_moves)

    def test_avoid_others_body_up(self):
        # Arrange 
        test_my_snake = {'id': 'gs_pPXPVBSS3bPWcfDX9vchP49b',
        'body': [{'x': 6, 'y': 1},{'x': 7, 'y': 1}, {'x': 8, 'y': 1},
         {'x': 9, 'y': 1}],'length': 14,}

        test_snakes =[
        {'id': 'gs_pPXPVBSS3bPWcfDX9vchP49b',
        'body': [{'x': 6, 'y': 1},{'x': 7, 'y': 1}, {'x': 8, 'y': 1}],
         'length': 3,},
         
         {'id': 'gs_XXcDWBMbV8wgS3BwwJ9hxQC4',
         'body': [{'x': 5, 'y': 2}, {'x': 6, 'y': 2}, {'x': 7, 'y': 2},{'x': 8, 'y': 2}],
         'length': 4}]

        expected = ["down","left","right"]
        # Act
        result_moves = logic._avoid_others(test_my_snake,self.possible_moves,test_snakes)
        # Assert
        self.assertEqual(len(result_moves), 3)
        self.assertEqual(expected, result_moves)

    def test_avoid_others_body_down(self):
        # Arrange 
        test_my_snake = {'id': 'gs_pPXPVBSS3bPWcfDX9vchP49b',
        'body': [{'x': 6, 'y': 1},{'x': 7, 'y': 1}, {'x': 8, 'y': 1},
         {'x': 9, 'y': 1}],'length': 14,}

        test_snakes =[
        {'id': 'gs_pPXPVBSS3bPWcfDX9vchP49b',
        'body': [{'x': 6, 'y': 1},{'x': 7, 'y': 1}, {'x': 8, 'y': 1}],
         'length': 3,},
         
         {'id': 'gs_XXcDWBMbV8wgS3BwwJ9hxQC4',
         'body': [{'x': 5, 'y': 0}, {'x': 6, 'y': 0}, {'x': 7, 'y': 0},{'x': 8, 'y': 0}],
         'length': 4}]

        expected = ["up","left","right"]
        # Act
        result_moves = logic._avoid_others(test_my_snake,self.possible_moves,test_snakes)
        # Assert
        self.assertEqual(len(result_moves), 3)
        self.assertEqual(expected, result_moves)  



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
        
    def test_hazards_left(self)-> None:
        #Arrange
        test_head =  {"x": 1, "y": 1}
        possible_moves = ["up", "down", "left", "right"]
        expected = ["up", "down", "right"]
        #Act
        result_moves = logic.avoid_hazards(test_head,self.test_board,possible_moves)
        #Assert
        self.assertEqual(len(result_moves), 3)
        self.assertEqual(expected, result_moves)

    def test_hazards_right(self)-> None:
        #Arrange
        test_head =  {"x": 17, "y": 1}
        possible_moves = ["up", "down", "left", "right"]
        expected = ["up", "down", "left"]
        #Act
        result_moves = logic.avoid_hazards(test_head,self.test_board,possible_moves)
        #Assert
        self.assertEqual(len(result_moves), 3)
        self.assertEqual(expected, result_moves)

    def test_hazards_up(self)-> None:
        #Arrange
        test_head =  {"x": 4, "y": 19}
        possible_moves = ["up", "down", "left", "right"]
        expected = ["down", "left","right"]
        #Act
        result_moves = logic.avoid_hazards(test_head,self.test_board,possible_moves)
        #Assert
        self.assertEqual(len(result_moves), 3)
        self.assertEqual(expected, result_moves)

    def test_hazards_down(self)-> None:

        #Arrange
        test_head =  {"x": 8, "y": 1}
        possible_moves = ["up", "down", "left", "right"]
        expected = ["up", "left","right"]
        #Act
        result_moves = logic.avoid_hazards(test_head,self.test_board,possible_moves)
        #Assert
        self.assertEqual(len(result_moves), 3)
        self.assertEqual(expected, result_moves)

    def test_hazards_tunnel(self)-> None:
        #Arrange
        test_head =  {"x": 2, "y": 11}
        possible_moves = ["up", "down", "left", "right"]
        expected = ["left","right"]
        #Act
        result_moves = logic.avoid_hazards(test_head,self.test_board,possible_moves)
        #Assert
        self.assertEqual(len(result_moves), 2)
        self.assertEqual(expected, result_moves)

    def test_hazards_corner(self)->None:
        #Arrange
        test_head =  {"x": 1, "y": 3}
        possible_moves = ["up", "down", "left", "right"]
        expected = ["down","right"]
        #Act
        result_moves = logic.avoid_hazards(test_head,self.test_board,possible_moves)
        #Assert
        self.assertEqual(len(result_moves), 2)
        self.assertEqual(expected, result_moves)

if __name__ == "__main__":
    unittest.main()
