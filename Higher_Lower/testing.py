from game_data import data
from random import choice
import art

print(art.logo)
compareA = choice(data)
compareB = choice(data)
print(f"A = name {compareA['name']}")
print(f"B = name {compareB['name']}")

if compareA["follower_count"] > compareB["follower_count"]:
    print("Bigger")
else:
    print("Lower")
