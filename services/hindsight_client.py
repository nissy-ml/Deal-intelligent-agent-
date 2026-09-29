# services/hindsight_client.py

class HindsightClient:
    def __init__(self):
        pass

    async def retain_memory(
        self,
        namespace: str,
        content: str,
        metadata: dict = None
    ):
        # call hindsight retain
        pass

    async def recall_memory(
        self,
        query: str,
        namespace: str,
        top_k: int = 5
    ):
        # call hindsight recall
        pass
