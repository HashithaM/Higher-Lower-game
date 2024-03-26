# Higher-Lower-game
This is a game guessing which account has the highest followers in instagram.
The provided code is a Python program for a simple game that compares the number of followers between two randomly chosen social media accounts. Here's a breakdown of how it works:

Import Statements:

random: This module is imported to facilitate the random selection of social media accounts for comparison.
data: This seems to be a module or variable containing information about social media accounts. It's likely a list of dictionaries where each dictionary represents an account.
logo and vs: These are likely imported from some custom module named art. They're probably ASCII art representing the game's logo and the "versus" sign.
Format Data Function:

format_data(account): This function takes an account dictionary as input and formats its data into a printable string. It extracts the name, description, and country from the account dictionary.
Initialization:

account_a: It randomly selects an account from the data list.
score: This variable is initialized to keep track of the player's score.
continue_game: This boolean variable is initialized as True to control the game loop.
Game Loop:

The game continues as long as continue_game is True.
Inside the loop, a new random account (account_b) is chosen for comparison. A while loop ensures that account_b is different from account_a.
The names and descriptions of the two accounts are printed along with the versus sign.
The player is prompted to input their choice ('A' or 'B') about which account has more followers.
The correct answer is determined by comparing the follower counts of account_a and account_b.
If the player's answer matches the correct answer, their score is incremented, and the loop continues with account_b becoming the new account_a.
If the player's answer is incorrect, the game ends, informing them of the correct answer and their final score.
Code Issues:

The issue with account_a not being updated within the loop is present.
There's no option for the player to play again without restarting the program.
Overall, the code sets up a basic game structure for comparing social media account followers and provides the player with feedback on their answers.
