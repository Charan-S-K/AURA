from enum import Enum


class Intent(Enum):
    CHAT = "chat"
    MEMORY_STORE = "memory_store"
    MEMORY_RECALL = "memory_recall"
    SCHEDULER = "scheduler"
    TOOL = "tool"
    UNKNOWN = "unknown"