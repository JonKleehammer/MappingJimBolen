import random
import TestScript
import MappingData

# Program by Jonathan Kleehammer
# Program is designed to simulate 100,000 tests of random guessing
# wrong answers are -.5 points and correct answers are 2 points
# test is 20 questions long. After finishing the simulation we map the data
# data mapped as a 3d bargraph

# how many tests?
test_count = 100000

# data stored in a dictonary of test# as key and the guesses, score for value
test_data = dict()

# initilizing the best and worst scores as the opposite
best_score = -10
worst_score = 40

# test_sum is used to calculate the average after the tests are done
# (maybe more efficient this way)
test_sum = 0

for t in range(0, test_count):
    # instantiating a test with 1 to 20 guesses
    test = TestScript.Test(random.randint(1 , TestScript.Test.test_questions))

    # recording best and worst scores
    if test.score > best_score:
        best_score = test.score
    if test.score < worst_score:
        worst_score = test.score

    # adding up the average which will be divided upon later
    test_sum += test.score
    # adding the data to the dictionary
    test_data[test.test_id] = (test.guesses, test.score)

# finally calculating the aerage
test_avg = test_sum / test_count

print ('\n({} Tests taken) (Average score: {}) (Best score: {}) (Worst score: {})'.format(test.test_count, test_avg, best_score, worst_score)

# calling the map_data method from the mappingdata file
MappingData.map_data(test_data)