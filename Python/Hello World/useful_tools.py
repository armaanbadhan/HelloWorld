import random

feet_in_miles = 5280
meters_in_kilometers = 1000
books = ["maths", "physics", "chemistry", "history"]


def get_file_ext(filename):
    return filename[filename.index(".") + 1:]


def roll_dice(num):
    return random.randint(1, num)
