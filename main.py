#!/usr/bin/env python3

# Created by: Daniel Pawelko
# Created on: Jan 2022
# Volume of cylinder

import math


def volume(height: int, radius: int):
    # volume function to calculate volume of cylinder
    # process
    return math.pi * radius * radius * height


def main():
    # main function for volume of cylinder

    # details
    print("This program calculates the volume of a cylinder.")

    try:
        # input
        radius_inp = input("Radius of cylinder (mm): ")
        radius_inp = int(radius_inp)
        height_inp = input("Height of cylinder (mm): ")
        height_inp = int(height_inp)

        # output/calling function
        print(
            f"The volume of a cylinder with a radius of {radius_inp} mm and\
height of {height_inp} mm is {round(volume(height_inp, radius_inp), 2)}mm³."
        )
    except ValueError:
        print("Input must be an integer")

    # done
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
