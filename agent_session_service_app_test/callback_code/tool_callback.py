import copy
from typing import Any, Dict, Optional

from google.adk.tools.base_tool import BaseTool
from google.adk.tools.tool_context import ToolContext
from google.adk.agents.callback_context import CallbackContext

import logging 
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def before_tool_callback(tool: BaseTool, 
                         args: Dict[str, Any], 
                         tool_context: ToolContext) -> Optional[Dict]:

    logger.info("Tool and args")
    logger.info(tool)
    logger.info(args)
    pass 

def after_tool_callback(tool: BaseTool, 
                        args: Dict[str, Any], 
                        tool_context: ToolContext, 
                        tool_response: Dict):
    logger.info("Tool and args")
    logger.info(tool)
    logger.info(args)
    pass 