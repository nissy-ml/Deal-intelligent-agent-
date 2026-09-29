from services.deal_memory import recall_memory


class ExecutiveBriefer:

    def __init__(self):
        self.agent_name = "Executive Briefer"

    async def generate_brief(
        self,
        deal_id
    ):

        memories = await recall_memory(
            f"Deal ID {deal_id}"
        )

        return {
            "deal_id": deal_id,
            "brief": memories
        }
