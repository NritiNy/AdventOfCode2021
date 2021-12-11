import os
import argparse
import requests
import importlib
from timeit import default_timer as timer

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("day", type=int)
    parser.add_argument("-t", "--test", action="store_true", dest="run_test", default=False)
    parser.add_argument("-sID","--sessionID", type=str, dest="sessionID", default="")

    args = parser.parse_args()
    
    input_path = os.path.join(".", "Inputs", f"input_{args.day:02}.txt")
    test_path = os.path.join(".", "test.txt")

    if not os.path.exists(input_path):
        url = f"https://adventofcode.com/2021/day/{args.day}/input"
        c = {'session': os.environ.get("AoC_SESSION", args.sessionID)}

        r = requests.get(url, cookies=c)
        if r.status_code == 200:
            with open(input_path, "w") as file:
                file.write(r.text)
        else:
            print(f"Failed to download input (Status {r.status_code}).")
            exit()

    if args.run_test:
        with open(test_path) as file:
            lines = [line.strip() for line in file.readlines() if len(line) > 0]
    else:
        with open(input_path) as file:
            lines = [line.strip() for line in file.readlines() if len(line) > 0]

    impl = importlib.import_module(f"Implementations.day{args.day:02}")

    s = timer()
    print(f"Part 01: {impl.part1(lines)} \t in {timer() - s:.06f}s")
    s = timer()
    print(f"Part 02: {impl.part2(lines)} \t in {timer() - s:.06f}s")

