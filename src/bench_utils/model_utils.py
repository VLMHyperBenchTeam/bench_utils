"""Модуль для работы с моделями (обратная совместимость)."""

# Универсальная фабрика моделей
from model_interface.model_factory import ModelFactory  # type: ignore

# Специфичные вспомогательные функции для Qwen2.5-VL теперь находятся в своём пакете
from model_qwen2_5_vl import (  # type: ignore
    create_qwen_model_config,
    initialize_qwen_model,
)

# Подготовка промптов остаётся без изменений
from prompt_handler import load_prompt, prepare_prompt  # type: ignore

# Реэкспорт для удобства пользователей bench_utils
initialize_model = ModelFactory.initialize_model

__all__ = [
    "initialize_model",
    "create_qwen_model_config",
    "initialize_qwen_model",
    "load_prompt",
    "prepare_prompt",
    "ModelFactory",
] 