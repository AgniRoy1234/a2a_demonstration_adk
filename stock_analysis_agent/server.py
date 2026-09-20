import uvicorn
import os 
import sys
from pathlib import Path
from dotenv import load_dotenv
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

# Add the directory containing 'stock_analysis_agent' to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Import using full package paths
from google.adk.a2a.utils.agent_to_a2a import to_a2a
from stock_analysis_agent.agent import root_agent
from stock_analysis_agent.agent_card import build_agent_card

def main():
    host = "localhost"
    port = int(os.getenv("PORT", 8001)) 

    app = to_a2a(
        root_agent,
        host=host,
        port=port,
        agent_card=build_agent_card(host, port),
    )

    print(f"StockAnalysis A2A server starting at http://{host}:{port}")
    print(f"  Agent card: http://{host}:{port}/.well-known/agent-card.json")

    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    main()