from typing import annotated
from typing_extensions import TypedDict


from langgraph import StateGraph, START, END
from langgraph.graph.message import add_messages


class State(TypedDict):
    messages: Annotated[list,add_messages]


graph_builder = StateGraph(State)