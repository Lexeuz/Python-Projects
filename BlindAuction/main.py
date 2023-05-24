from art import logo
import os


def clean_console():
    os.system("cls")


print(logo)
print("Welcome to the secret auction program!")

bidders_dict = {}

on = True
while on:
    bidder_name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    bidders_dict[bidder_name] = bid
    if input("Are there any other bidders? Type 'yes' or 'no'.\n") == "yes":
        clean_console()
    else:
        on = False

top_bid = 0
top_name = ""
for name in bidders_dict:
    if bidders_dict[name] > top_bid:
        top_bid = bidders_dict[name]
        top_name = name

print(f"The winner is {top_name} with a bid of ${top_bid}")
