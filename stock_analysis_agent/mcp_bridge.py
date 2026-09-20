import asyncio
import os
import uuid
import httpx
from fastmcp import FastMCP

from a2a.client import ClientConfig, ClientFactory, minimal_agent_card
from a2a.types import Message, Part, Role, SendMessageRequest

# 1. Initialize FastMCP server
mcp = FastMCP("A2A Agent Bridge")

from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file 

PORT = int(os.getenv("PORT", 8001))  # Default to 8001 if not set

AGENT_URL = f"http://localhost:{PORT}/"


@mcp.tool()
async def ask_agent(prompt: str) -> str:
    """Sends a query/prompt to the A2A agent running on port 8001 and returns the compiled response."""
    
    # Configure httpx client with custom timeouts
    custom_httpx = httpx.AsyncClient(timeout=httpx.Timeout(120.0, connect=10.0))
    config = ClientConfig(httpx_client=custom_httpx)

    card = minimal_agent_card(url=AGENT_URL, transports=["JSONRPC"])
    client = ClientFactory(config=config).create(card)

    request = SendMessageRequest(
        message=Message(
            message_id=str(uuid.uuid4()),
            role=Role.ROLE_USER,
            parts=[Part(text=prompt)],
        )
    )

    responses = []
    try:
        async for response in client.send_message(request):
            # Aggregating response chunks or messages from the stream
            responses.append(str(response))
    finally:
        await custom_httpx.aclose()

    return "\n".join(responses) if responses else "No response received from agent."


if __name__ == "__main__":
    mcp.run()