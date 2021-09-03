# Hog-Dice-Game

Poorly written and untested hog implementation in python with a few rules to spice it up.

In Hog, two players alternate turns trying to be the first to end a turn with at least 100 total points. On each turn, the current player chooses some number of dice to roll, up to 10. That player's score for the turn is the sum of the dice outcomes.

Rules:
To spice up the game, we will play with some special rules:

1- Pig Out. If any of the dice outcomes is a 1, the current player's score for the turn is 1.
{
    Example 1: The current player rolls 7 dice, 5 of which are 1's. They score 1 point for the turn.
    Example 2: The current player rolls 4 dice, all of which are 3's. Since Pig Out did not occur, they score 12 points for the turn.
}

2 - Free Bacon. A player who chooses to roll zero dice scores points equal to ten minus the minimum of of the ones and tens digit of the opponent's score.
{
    Example 1: The opponent has 13 points, and the current player chooses to roll zero dice. The minimum of 1 and 3 is 1, so the current player gains 10 - 1 = 9 points.
    Example 2: The opponent has 85 points, and the current player chooses to roll zero dice. The minimum of 8 and 5 is 5, so the current player gains 10 - 5 = 5 points.
    Example 3: The opponent has 7 points, and the current player chooses to roll zero dice. The minimum of 0 and 7 is 0, so the current player gains 10 - 0 = 10 points.
}

3- Swine Swap. After points for the turn are added to the current player's score, if the first (leftmost) digit of the current player's score and the last (rightmost) digit of the opponent player's score are equal, then the two scores are swapped.
{
    Example: The current player has a total score of 31 and the opponent has 83. The current player rolls one dice with value 5. The player's new score is 36, and the opponent's       score is 83. The leftmost digit of the current player's score and the rightmost digit of the opponent's score are both 3, so the scores are swapped.
}
