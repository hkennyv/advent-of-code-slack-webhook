import os
import sys
from datetime import datetime

import pytz
import requests

SLACK_URL = os.environ.get("SLACK_URL", None)


def send_aoc_webhook() -> requests.Response:
    # Get the current date in EST - advent of code challenges get released
    # at midnight EST
    now = datetime.now(tz=pytz.UTC).astimezone(pytz.timezone("US/Eastern"))
    day = now.day
    month = now.month
    year = now.year

    if day > 25 or month != 12:
        sys.exit("Advent of code is only active 12/1 - 12/25")

    res = requests.post(
        SLACK_URL,
        json={
            "text": f"🎄 *Advent of Code day {day} is here, happy coding!* "
            f"https://adventofcode.com/{year}/day/{day}",
        },
    )

    return res


# main.handler
def handler(event, context):
    if SLACK_URL is None:
        return {
            "statusCode": 503,
            "body": "SLACK_URL is not set",
        }

    res = send_aoc_webhook()

    if res.status_code != 200:
        return {"statusCode": res.status_code, "body": res.text}
    else:
        return {"statusCode": 200, "body": "success"}


if __name__ == "__main__":
    send_aoc_webhook()
