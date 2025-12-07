import requests
import time
import re
import sys
import os

local_time = time.localtime()
match len(sys.argv):
    case 1:
        day = local_time.tm_mday
        year = local_time.tm_year
        if local_time.tm_mon != 12:
            print("Error: use manual mode when outside of december.")
            exit(1)
    case 2:
        day = int(sys.argv[1])
        year = local_time.tm_year
    case 3:
        day = int(sys.argv[1])
        year = int(sys.argv[2])

if (day > 25 and 2015 <= year <= 2024
    or day > 12 and year >= 2025
    or year < 2015):
    print(f"Error: invalid day / year pair")

print(f"Fectching inputs for Advent of Code {year} Day {day}...")

base = "https://adventofcode.com/"
cookies = {"session": open("id.txt", "r").readline().strip()}

input_request = requests.get(base + f"{year}/day/{day}/input", cookies=cookies)
if input_request.status_code != 200:
    print("Error:")
    print(input_request.status_code, input_request.content)
    exit(1)

input = input_request.content.decode()

easy_input_request = requests.get(base + f"{year}/day/{day}", cookies=cookies)
try:
    easy_input = re.search(r"<pre><code>((?>.|\n)*?)<\/code><\/pre>", easy_input_request.content.decode()).group(1)
except AttributeError:
    easy_input = None
    print("No \"easy input\" found. Continuing...")

# Create directory if it doesn't exist
dir_path = f"{year}/Day-{"{:02}".format(day)}"
os.makedirs(dir_path, exist_ok=True)

open(f"{dir_path}/input.txt", "w").write(input)
if easy_input != None:
    open(f"{dir_path}/easyinput.txt", "w").write(easy_input)

print("Done!")