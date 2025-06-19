"""Модуль для работы с моделями (обратная совместимость)."""
from model_interface.model_factory import ModelFactory, load_prompt  # type: ignore

initialize_model = ModelFactory.initialize_model
create_qwen_model_config = ModelFactory.create_qwen_model_config
initialize_qwen_model = ModelFactory.initialize_qwen_model

__all__ = [
    "initialize_model",
    "create_qwen_model_config",
    "initialize_qwen_model",
    "load_prompt",
    "ModelFactory",
] 