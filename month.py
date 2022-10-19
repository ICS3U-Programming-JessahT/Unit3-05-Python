#!/usr/bin/env python3

# Created By: Jessah
# Date: Oct 13, 2022
# This program generates months depending on user number


def main():
    # Get number equal to month from user
    user_month = input("Enter a number equivalent to months: ")

    # Match case/Switch case statements depending on user input
    match user_month:
        case "1":
            print("The equivalent month is January")
        case "2":
            print("The equivalent month is February")
        case "3":
            print("The equivalent month is March")
        case "4":
            print("The equivalent month is April")
        case "5":
            print("The equivalent month is May")
        case "6":
            print("The equivalent month is June")
        case "7":
            print("The equivalent month is July")
        case "8":
            print("The equivalent month is August")
        case "9":
            print("The equivalent month is September")
        case "10":
            print("The equivalent month is October")
        case "11":
            print("The equivalent month is November")
        case "12":
            print("The equivalent month is December")

        case _:  # If the user doesn't write valid number
            print("Invalid month")


if __name__ == "__main__":
    main()
