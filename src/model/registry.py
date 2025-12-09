
from typing import Dict, Type, Union

from src.model.mllm.registry import MLLM_REGISTRY
from src.model.mllm.base_mllm import BaseMLLM

from src.model.embedder.registry import EMBEDDER_REGISTRY
from src.model.embedder.base_embedder import BaseEmbedder

MODEL_REGISTRY = MLLM_REGISTRY | EMBEDDER_REGISTRY
