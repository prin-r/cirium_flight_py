#!/usr/bin/env python3
import requests
import sys
import os

URL = "https://api.flightstats.com/flex/ratings/rest/v1/json/flight/{}/{}"


def main(fs_code, flight_number, departure_airport):
    res = requests.get(
        URL.format(fs_code, flight_number),
        params={
            "appId": os.getenv("APP_ID"),
            "appKey": os.getenv("APP_KEY"),
            "departureAirport": departure_airport,
        },
    )
    return res.json()["ratings"][0]["ontimePercent"]


if __name__ == "__main__":
    try:
        print(main(*sys.argv[1:]))
    except Exception as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)
