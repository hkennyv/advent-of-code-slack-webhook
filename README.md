# Advent of Code Slack webhook

## Overview

This repository contains a simple webhook in Python that can posts the latest
Advent of Code exercise to a given `SLACK_URL`.

Currently, the text is non-adjustable and posts something similar to the
following:

---

🎄 **Advent of Code day 5 is here, happy coding!** https://adventofcode.com/2021/day/5

---

## Usage

### Environment

| Environment Variable | Description                                       |
| -------------------- | ------------------------------------------------- |
| `SLACK_URL`          | The webhook URL for the Slack channel to post to. |

### Install dependencies

Install the dependencies with `pip install -r requirements.txt`.

### Run the webhook

Run the webhook with `python main.py`.

## Github actions

If you define the `SLACK_URL` environment variable on your github repository,
you can use the github action located in this repository to post to your own
Slack webhook.

## License

MIT
