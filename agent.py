from dotenv import load_dotenv
from typing import TypedDict, Literal, Annotated, List
from operator import add
from langchain_core.messages import HumanMessage, SystemMessage, BaseMessage
from langgraph.graph import END, START, StateGraph,MessagesState
from langgraph.prebuilt import ToolNode
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import AIMessage

load_dotenv()

llm = ChatOpenAI(model="gpt-4o")

tavily_search = TavilySearchResults(max_results=3)



def answer_node(state: MessagesState):
    """answer these questions using the llm"""
    answer = llm.invoke(state["messages"])
    # Add the final answer as an AIMessage to the state
    state["messages"].append(AIMessage(content=answer.content))
    return state

# Construct a simple langgraph graph

graph = StateGraph(MessagesState)

graph.add_node("answer_node",answer_node) 
    # Directly use the answer_node function without a ToolNode
graph.add_edge(START, "answer_node")

graph.add_edge("answer_node",END)

builder = graph.compile()

# if __name__ == "__main__":
#     response = builder.invoke({"messages": [HumanMessage(content="hello from vasanth")]})
#     print(response["messages"][-1].content)
    # Run the graph with a sample state
# sample_state = MessagesState(messages=[HumanMessage(content="Hello")])
# result = graph.run(sample_state)
# print(result["messages"][-1].content)  # Print the final AIMessage content



