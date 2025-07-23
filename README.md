# bench_utils

Простая утилита для бенчмаркинга и вычисления метрик.

## Установка

```bash
uv add bench_utils
```

## Установка из репозитория (Git)

*   **Для пользователей с `uv` и `pyproject.toml` (рекомендуемый способ)**:
    ```bash
    uv add git+https://github.com/VLMHyperBenchTeam/bench_utils.git@main
    uv sync
    ```
*   **Для пользователей с `pip` или `uv` (прямая установка)**:
    ```bash
    pip install git+https://github.com/VLMHyperBenchTeam/bench_utils.git@main
    # или
    uv pip install git+https://github.com/VLMHyperBenchTeam/bench_utils.git@main
    ```

## Установка из локального дистрибутива
1.  Сборка: `uv build` (создает `.whl` и `.tar.gz` в `dist/`)
2.  Установка: `uv pip install dist/bench_utils-0.1.3.dev0-py3-none-any.whl`
    > **Примечание:** `uv add` не поддерживает установку из `.whl` файлов. Для этого всегда используйте `uv pip install`.

## Установка в режиме разработки
```bash
uv pip install -e .
# или для пользователей pip
pip install -e .
```

## Использование

```python
from bench_utils import metrics, utils

# Вычисление метрик классификации
classification_metrics = metrics.calculate_classification_metrics(
    y_true=["class1", "class2"], 
    y_pred=["class1", "class2"],
    document_classes={"class1": "Класс 1", "class2": "Класс 2"}
)

# Закрываем примеры
ordering_metrics = metrics.calculate_ordering_metrics([1, 2, 3], [1, 3, 2])

### Быстрый импорт моделей

`bench_utils.model_utils` делает реэкспорт помощников для моделей Qwen:

```python
from bench_utils.model_utils import (
    initialize_model,            # универсальный способ
    initialize_qwen_model,       # «одна кнопка» для Qwen2.5-VL
    create_qwen_model_config,
)

# получить готовую Qwen-модель
model = initialize_qwen_model(device_map="cuda:0")

# универсальный путь через вложенный конфиг
config = create_qwen_model_config(device_map="auto")
model2 = initialize_model(config)
```
