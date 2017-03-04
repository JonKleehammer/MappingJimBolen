import random
import numpy as np

# Test class

class Test:

    # class variables  used for all the classes
    # test count starts as 0
    test_count = 0

    # test data
    test_questions = 20
    correct_points = 2
    incorrect_points = -.5

    # could have used an int, but char is more understandable for non comp sci majors
    answer_choices = ['a', 'b', 'c', 'd', 'e']

    # initializing with g as # of guesses
    def __init__(self, g):

        # setting the id and then adding to the test count
        self.test_id = Test.test_count
        Test.test_count += 1

        # clipping guesses to between 1 and 20 then declaring the right, wrong, score variables
        self.guesses = np.clip(g, 1, Test.test_questions)
        self.right = 0
        self.wrong = 0
        self.score = 0

        # calling the method 'take_test' to process guesses and score
        self.take_test()

    # simulate the guesses
    def take_test(self):
        for g in range(0, self.guesses):
            # randomly picking the questiosn answer and the given answer
            q = random.sample(Test.answer_choices, 1)
            a = random.sample(Test.answer_choices, 1)

            # checking if they are equal to each other
            if q != a:
                self.wrong += 1
            else:
                self.right += 1

        # calculate score
        self.score = (self.right * 2) + (self.wrong * -.5)
