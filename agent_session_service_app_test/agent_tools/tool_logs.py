
from google.adk.tools.tool_context import ToolContext

import logging 
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def log_toolcontext(tool_context: ToolContext):

    logger.info("Tool logs")
    
    attributes = vars(tool_context.state)
    for key, value in attributes.items():
        logger.info(f"{key}: {value}")