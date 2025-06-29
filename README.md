# bench_utils

Простая утилита для бенчмаркинга и вычисления метрик.

## Установка

```bash
uv add bench_utils
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
