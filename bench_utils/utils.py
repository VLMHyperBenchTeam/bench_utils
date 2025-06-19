import json
from pathlib import Path
from typing import Any, Dict


def load_config(config_path: str) -> Dict[str, Any]:
    """Загружает конфигурацию из JSON файла."""
    config_file = Path(config_path)
    if not config_file.exists():
        raise FileNotFoundError(f"Файл конфигурации {config_path} не найден")
    with config_file.open("r") as f:
        return json.load(f)


def get_run_id(model_name: str) -> str:
    """Генерирует идентификатор запуска на основе имени модели."""
    return Path(model_name).stem


def save_results_to_csv(results: Dict[str, float], filename: str, subset_name: str | None = None) -> None:
    """Сохраняет результаты в CSV файл."""
    import pandas as pd  # type: ignore

    results_df = pd.DataFrame([results])
    if subset_name:
        print(f"\n📊 Метрики для сабсета {subset_name}:")
    for key, value in results.items():
        print(f"  {key}: {value:.4f}")
    results_df.to_csv(filename, index=False)


def get_document_type_from_config(config: Dict[str, Any], dataset_path: Path) -> str:
    """Определяет тип документа из конфигурации."""
    document_classes = config.get("document_classes", {})
    dataset_name = dataset_path.name

    for doc_type, doc_name in document_classes.items():
        if doc_type in dataset_name:
            return doc_name

    return dataset_name.replace("_", " ").title() 