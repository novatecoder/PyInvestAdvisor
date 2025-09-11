
from datetime import datetime
import os

from google.adk.agents import Agent
from google.adk.tools import google_search
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools.langchain_tool import LangchainTool
from google.adk.tools.mcp_tool import MCPToolset, StreamableHTTPConnectionParams

from dotenv import load_dotenv

# Load environment variables
load_dotenv()


# ----- Example of a Function tool -----
def get_current_date() -> dict:
    """
    Get the current date in the format YYYY-MM-DD
    """
    return {"current_date": datetime.now().strftime("%Y-%m-%d")}


# ----- Example of a Built-in Tool -----
search_agent = Agent(
    model="gemini-2.5-flash",
    name="search_agent",
    instruction="""
    You're a specialist in Google Search.
    """,
    tools=[google_search],
)

search_tool = AgentTool(search_agent)

# ----- Example of an MCP Tool (streamable-http) -----
mcp_tools = MCPToolset(
    connection_params=StreamableHTTPConnectionParams(
        # 서버가 실행 중인 로컬 주소와 포트로 변경
        url="http://127.0.0.1:8080/mcp/", 
        # kis_mcp_server 코드에는 별도 인증 헤더가 없으므로 빈 dict 전달
        headers={},
    ),
    # kis_mcp_server에 정의된 조회(read-only) 도구 목록으로 변경
    tool_filter=[
        "inquery-stock-price",
        "inquery-balance",
        "inquery-order-list",
        "inquery-order-detail",
        "inquery-stock-info",
        "inquery-stock-history",
        "inquery-stock-ask",
        "inquery-overseas-stock-price",
    ],
)