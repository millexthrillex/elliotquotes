# Quotes that Elliot says:
# ------------------------

import random

def randElliotQuote():
    elliotquotes = [
    ". . . for the sake of argument.",
    "so let's say, (for the sake of argument)",
    "I don't have the foggiest of ideas.",
    "ah, fair enough.",
    "oh that's straaaaaaaaaaange.",
    "my pleasure.",
    "weird. weeeeeeeeird.",
    "suffice it to say. . .",
    "that's my () and i'm sticking to it.",
    "that's my comment and i'm sticking to it.",
    "sure thing.",
    "a lot of words with dog in them. that's kind of weird."]

    return random.choice(elliotquotes)

# main() for testing and anything else really
def main():
    quote = randElliotQuote()
    print(quote)

if __name__ == "__main__":
    main()
