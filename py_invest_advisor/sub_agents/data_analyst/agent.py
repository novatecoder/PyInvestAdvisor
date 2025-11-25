# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""data_analyst_agent for finding information using google search"""

from google.adk import Agent
from google.adk.tools import google_search
from py_invest_advisor.tools.tools import get_current_date, mcp_tools
from google.adk.tools.agent_tool import AgentTool


from . import prompt

import os

DATA_ANALYST_MODEL=os.environ['REASONING_MODEL']

# MODEL = "gemini-2.5-flash"

MODEL = "gemini-2.5-flash"

# data_analyst_agent = Agent(
#     model=MODEL,
#     name="data_analyst_agent",
#     instruction=prompt.DATA_ANALYST_PROMPT,
#     output_key="market_data_analysis_output",
#     tools=[get_current_date, google_search],
# )

kis_agent = Agent(
    model=MODEL,
    name="kis_agent",
    instruction=prompt.KIS_AGENT_PROMPT,
    output_key="kis_data_output",
    tools=[get_current_date, mcp_tools],
)

google_search_agent = Agent(
    model=MODEL,
    name="google_search_agent",
    instruction=prompt.GOOGLE_SEARCH_AGENT_PROMPT,
    output_key="google_data_output",
    tools=[google_search],
)

data_analyst_agent = Agent(
    model=DATA_ANALYST_MODEL,
    name="data_analyst_agent",
    instruction=prompt.DATA_ANALYST_PROMPT,
    output_key="market_data_analysis_output",
    tools=[
        AgentTool(agent=kis_agent),
        AgentTool(agent=google_search_agent)
        ], # 하위 에이전트를 도구로 사용
)