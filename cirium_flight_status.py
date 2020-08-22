#!/usr/bin/env python3
import requests
import sys
import os

URL = "https://api.flightstats.com/flex/flightstatus/rest/v2/json/flight/status/{}/{}/dep/{}"


def main(fs_code, flight_number, date, airport):
    res = requests.get(
        URL.format(fs_code, flight_number, date),
        params={
            "appId": os.getenv("APP_ID"),
            "appKey": os.getenv("APP_KEY"),
            "utc": "true",
            "airport": airport,
        },
    ).json()

    if "flightStatuses" not in res:
        raise ValueError("key flightStatuses not found")

    if len(res["flightStatuses"]) == 0:
        raise ValueError("flight statuses is empty")

    flight_status = res["flightStatuses"][0]
    if "delays" in flight_status:
        delays = flight_status["delays"]
    else:
        return "0,0"

    departureGateDelayMinutes = (
        delays["departureGateDelayMinutes"] if "departureGateDelayMinutes" in delays else 0
    )
    arrivalGateDelayMinutes = (
        delays["arrivalGateDelayMinutes"] if "arrivalGateDelayMinutes" in delays else 0
    )

    return "{},{}".format(departureGateDelayMinutes, arrivalGateDelayMinutes)


if __name__ == "__main__":
    try:
        print(main(*sys.argv[1:]))
    except Exception as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)
