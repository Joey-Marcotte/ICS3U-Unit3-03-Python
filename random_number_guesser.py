#!/usr/bin/env python3

# Created by: Joey Marcotte
# Created on: October 2019
# This program gets the user to guess a number

import random


def main():

    while True:
        # imput
        number_guessed = int(input("pick a number between 0-9:"))

        # process
        if number_guessed == (random.randint(0, 9+1)):
            # output
            print("You win, you guessed the number")
            break
        else:
            print("wrong, try again")


if __name__ == "__main__":
    main()
