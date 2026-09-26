
from google.adk.tools.tool_context import ToolContext
from google.adk.agents.callback_context import CallbackContext

import logging 
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def log_toolcontext(tool_context: ToolContext):

    logger.info("Tool logs")
    
    attributes = vars(tool_context.state)
    for key, value in attributes.items():
        logger.info(f"{key}: {value}")

def log_agentstate(callback_context: CallbackContext):

    logger.info("Agent State logs")
    
    attributes = vars(callback_context.state)
    for key, value in attributes.items():
        logger.info(f"{key}: {value}")