"""Constants for the `twitch_drops_overseer` package"""

from os import getenv


CLIENT_ID = getenv("CLIENT_ID")
AUTH_TOKEN = getenv("AUTH_TOKEN")

GQL_API_URL = "https://gql.twitch.tv/gql"
