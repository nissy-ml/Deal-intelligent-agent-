class AgentOrchestrator:

    async def handle_query(
        self,
        query,
        deal_id
    ):

        if "risk" in query:
            return await risk_predictor.run()

        if "objection" in query:
            return await objection_coach.run()

        if "brief" in query:
            return await executive_briefer.run()

        if "history" in query:
            return await deal_historian.run()

        return await pattern_miner.run()
