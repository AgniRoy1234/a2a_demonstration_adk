from datetime import datetime
from typing import Optional

from google.adk.agents.callback_context import CallbackContext
from google.genai import types 

from agent_sqlite.session_service_queries import (execute_query,
                                                  fetch_query)

from logging.logging import log_agentstate

import os
from dotenv import load_dotenv

load_dotenv()

SQLITE_DATABASE=os.getenv("SQLITE_DATABASE", "agent_logs.db")
SQLITE_TABLE_NAME=os.getenv("SQLITE_TABLE_NAME",'agent_logs')

def before_agent_callback_price_retrieval_agent(callback_context: CallbackContext) -> Optional[types.Content]:

     # Get the session state
    state = callback_context.state

    log_agentstate(callback_context)

    if "chat_id" not in state:
        now = datetime.now()
        chat_id = now.strftime("%Y-%m-%d %H:%M:%S")
        
        state["chat_id"] = chat_id
        insert_query = f"""insert into {SQLITE_TABLE_NAME} (chat_id,agent_name) VALUES 
        ('{chat_id}', 'price_retrieval_agent') """ 
        execute_query(insert_query)

    else:
        chat_id = state["chat_id"]
        update_query = f"""update {SQLITE_TABLE_NAME} set agent_name = 'price_retrieval_agent' 
                where chat_id = '{chat_id}' """ 
        execute_query(update_query) 

    return None 

    


