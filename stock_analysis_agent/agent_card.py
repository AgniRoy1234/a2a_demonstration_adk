from a2a.types import (
    AgentCapabilities,
    AgentCard,
    AgentInterface,
    AgentSkill,
)


def build_agent_card(host: str, port: int) -> AgentCard:
    return AgentCard(
        name="stock-performance-agent",
        description=(
            "Calculates historical stock performance and percentage price changes "
            "over specified or relative time windows using live market data."
        ),
        version="1.0.0",
        supported_interfaces=[
            AgentInterface(
                url=f"http://{host}:{port}/",
                protocol_binding="JSONRPC",
                protocol_version="1.0",  # Updated to match A2A v1.0 schema
            )
        ],
        default_input_modes=["text/plain"],
        default_output_modes=["text/plain"],
        capabilities=AgentCapabilities(
            streaming=False,
            push_notifications=False,
        ),
        skills=[
            AgentSkill(
                id="calculate_stock_performance",
                name="Calculate Stock Performance",
                description=(
                    "Fetches historical stock prices across relative "
                    "(e.g., 'last 4 months', 'past year') or explicit date "
                    "ranges and calculates the exact percentage change."
                ),
                tags=[
                    "stock",
                    "finance",
                    "market",
                    "performance",
                    "percentage-change",
                    "price-history",
                    "investing",
                ],
                examples=[
                    "What is the 6-month performance of AAPL?",
                    "Calculate the percentage change for GOOGL over the last year.",
                    "How much did MSFT change between 2023-01-01 and 2023-12-31?",
                    "Check Tesla stock performance over the last 4 months.",
                ],
                input_modes=["text/plain"],
                output_modes=["text/plain"],
            ),
        ],
    )