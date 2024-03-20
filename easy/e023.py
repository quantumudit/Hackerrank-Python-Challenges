#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(s):
    return " ".join(
        [i[0].upper() + i[1:] if len(i) > 1 else i.upper() for i in s.split(" ")]
    )


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    result = solve(s)

    fptr.write(result + "\n")

    fptr.close()
