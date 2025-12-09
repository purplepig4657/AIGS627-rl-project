from src.model.mllm.mllms.chatgpt5._base import ChatGPT5, ChatGPT5_Factory
from src.model.mllm.mllms.chatgpt5.local import ChatGPT5_Local
from src.model.mllm.mllms.chatgpt5.client import ChatGPT5_Client
from src.model.mllm.utils.constants import LoadMode

# Register implementations with the factory
ChatGPT5_Factory.register(LoadMode.LOCAL, ChatGPT5_Local)
ChatGPT5_Factory.register(LoadMode.REMOTE, ChatGPT5_Client)

__all__ = [
    "ChatGPT5",
    "ChatGPT5_Factory",
    "ChatGPT5_Local",
    "ChatGPT5_Client",
]
