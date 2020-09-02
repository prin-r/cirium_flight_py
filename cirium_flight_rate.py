#!/usr/bin/env python3
import requests
import sys
import os

URL = "https://jzjsymorj3.execute-api.ap-southeast-1.amazonaws.com/live/CIRIUM_FLIGHT_RATE/"


def main(input):
    res = requests.get(URL + input)
    return res.json()["result"]["ratings"][0]["ontimePercent"]


if __name__ == "__main__":
    try:
        print(main(*sys.argv[1:]))
    except Exception as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)
