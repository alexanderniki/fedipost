from typing import List, Dict, Protocol


class FediverseClient(Protocol):
    """
    Fediverse client
    """

    def fetch_timeline(self, timeline):
        ...

    def post(self, post):
        ...

    def fetch_post(self, post):
        ...
