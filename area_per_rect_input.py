#!/usr/bin/env python3
# Created by: Alex
# Created on: sep. 28, 2023
# This program asks the user for the length and
# width of the rectangle in mm. It then
# calculates and displays the area and
# perimeter.
import math


def main():
    # ask user for length and width
    print("Today we will calculate the area and")
    print("perimeter of a rectangle")
    length = int(input("Enter the length (mm): "))
    width = int(input("Enter the width (mm): "))

    # calculate the area and perimeter
    area = length * width
    perimeter = 2 * (length + width)

    # display your area and perimeter
    print("")
    print("Area = {} mm^2".format(area))
    print("Perimeter = {} mm".format(perimeter))


if __name__ == "__main__":
    main()
