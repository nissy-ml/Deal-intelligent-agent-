from hindsight_client import Hindsight

client = Hindsight(
    base_url="http://localhost:8888"
)

BANK_ID = "deal-oracle"


async def retain_memory(content):
    return client.retain(
        bank_id=BANK_ID,
        content=content
    )


async def recall_memory(query):
    return client.recall(
        bank_id=BANK_ID,
        query=query
    )
