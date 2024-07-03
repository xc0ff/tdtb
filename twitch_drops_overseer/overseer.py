from types import SimpleNamespace

import hashlib

import requests


QUERY_STRING = """
query ViewDropCampaigns {
    currentUser {
        dropCampaigns {
            id
            endAt
            game {
                displayName
            }
        }
    }
}
"""


class Overseer:
    _QUERIES = SimpleNamespace(
        ViewDropCampaigns=SimpleNamespace(
            operation="ViewDropCampaigns",
            hash=""
        ),
        ViewCampaignDetails=SimpleNamespace(
            operation="ViewCampaignDetails",
            hash=""
        ),
    )
    _API_URL = "https://gql.twitch.tv/gql"

    def __init__(self, client_id: str, auth_token: str):
        self._client_id = client_id
        self._auth_token = auth_token

    def _make_authorized_request(self, operation: str, query_hash: str):
        headers = {
            "Content-Type": "text/plain;charset=UTF-8",
            # "Client-ID": CLIENT_ID
            "Authorization": f"OAuth {self._auth_token}",
        }

        data = {
            "operationName": operation,
            "extensions": {
                "persistedQuery": {
                    "version": 1,
                    "sha256Hash": query_hash,
                }
            },
        }

        r = requests.post(self._API_URL, timeout=30, headers=headers, json=data)
        print(r.text)

    def get_drop_campaigns(self) -> list:
        hash_object = hashlib.sha256(QUERY_STRING.encode("utf-8"))
        query_hash = hash_object.hexdigest()

        self._make_authorized_request(
            self._QUERIES.ViewDropCampaigns.operation, query_hash
        )

        return []

    def get_campaign_details(self, id: int) -> list:
        return []
