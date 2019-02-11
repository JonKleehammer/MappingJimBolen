# MappingJimBolen

The Jim Bolen Math Competition is a math test that can be taken for scholarship opportunities.
The format of the test is as follows: 
  There are 20 questions
  Each question has 5 multiple choice answers to chooose from
  A correct answer is worth +2.0 points
  A wrong answer is worth   -0.5 points
  A blank answer is worth    0.0 points
  
Given this information I created a program that simulates testers randomly guessing on the test and their problem and creates a 3d graph of the information
For each of the 100,000 simulated tests we randomly choose a correct answer then randomly select an answer and compare if they're the same or different to see if the tester selected the correct answer.
At the end of the 100,000 simulated tests we print out the number of tests, average score, best score, and worst score of the 100,000 tests.
We display the distribution of all scores on a 3d graph where:
  the X axis is the number of guesses the tester made
  the Y axis is the frequency of how many testers got that score given X guesses
  the Z axis is the score the tester received
