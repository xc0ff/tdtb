import requests
import hashlib


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
    def __init__(self, client_id: str, auth_token: str):
        self._client_id = client_id
        self._auth_token = auth_token

    def get_drop_campaigns(self) -> list:
        hash_object = hashlib.sha256(QUERY_STRING.encode("utf-8"))
        hash_hex = hash_object.hexdigest()

        headers = {
            "Content-Type": "text/plain;charset=UTF-8",
            # "Client-ID": CLIENT_ID
            "Authorization": f"OAuth {self._auth_token}",
        }

        data = {
            "operationName": "ViewDropCampaigns",
            "extensions": {
                "persistedQuery": {
                    "version": 1,
                    "sha256Hash": hash_hex
                }
            },
        }

        r = requests.post("https://gql.twitch.tv/gql", headers=headers, json=data)
        print(r.text)

        return []

    def get_campaign_details(self, id: int) -> list:
        return []
