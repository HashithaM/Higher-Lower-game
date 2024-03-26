import random
from game_data import data
from art import logo,vs

print(logo)


def format_data(account):
    """Format account data into printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}."


account_a = random.choice(data)
score = 0
continue_game = True

while continue_game:
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A :{format_data(account_a)}")
    print(vs)
    print(f"Against B :{format_data(account_b)}")
    answer = input("Who has more followers ? Type 'A' or 'B' :").upper()
    if account_a["follower_count"] > account_b["follower_count"]:
        correct_answer = "A"
    else:
        correct_answer = "B"

    if answer == correct_answer:
        score += 1
        account_a = account_b
        print(f"You are right. Your current score is {score}.")
    else:
        print(f"Sorry, that's wrong. Your score is {score}.")
        continue_game = False


# if a > b:
#     if guess == a:
#         return True
#     if guess == b:
#         return False
# else:
#     if guess == b:
#         return True
#     if guess == a:
#         return False

# if a > b:
#     return guess == a
# else:
#     return guess == b
