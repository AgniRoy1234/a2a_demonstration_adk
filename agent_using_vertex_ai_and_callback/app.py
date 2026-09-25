from google.adk.apps.app import App
from google.adk.apps.app import EventsCompactionConfig

from .agent import root_agent

print("Starting the Stock Analysis App...")

app = App(
    name='stock-analysis-app',
    root_agent=root_agent,
    events_compaction_config=EventsCompactionConfig(
        compaction_interval=3,  # Trigger compaction every 3 new invocations.
        overlap_size=1          # Include last invocation from the previous window.
    ),
)