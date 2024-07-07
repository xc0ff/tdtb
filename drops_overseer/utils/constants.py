"""Constants for the `twitch_drops_overseer` package"""

import os

from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")

GQL_API_URL = "https://gql.twitch.tv/gql"
