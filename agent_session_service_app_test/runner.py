from google.adk import Runner
from google.adk.sessions import VertexAiSessionService
from google.genai import types

from .agent import root_agent

from dotenv import load_dotenv
load_dotenv()
import os

print("runner.py")

app_name="stock-analysis-app"
user_id="testuser1"

os.environ["GOOGLE_CLOUD_PROJECT"] = os.getenv("GCP_PROJECT_ID")
os.environ["GOOGLE_CLOUD_REGION"] = os.getenv("GCP_REGION")

# Create the ADK runner with VertexAiSessionService
session_service = VertexAiSessionService(
      project=os.environ["GOOGLE_CLOUD_PROJECT"] ,
      location=os.environ["GOOGLE_CLOUD_REGION"])
runner = Runner(
    agent=root_agent,
    app_name=app_name,
    session_service=session_service)

# Helper method to send query to the runner
async def call_agent(query, session_id, user_id):
  content = types.Content(role='user', parts=[types.Part(text=query)])
  async for event in runner.run_async(
      user_id=user_id, session_id=session_id, new_message=content):
      if event.is_final_response():
          final_response = event.content.parts[0].text
          print("Agent Response: ", final_response)
