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

# Вычисление метрик упорядочивания
ordering_metrics = metrics.calculate_ordering_metrics([1, 2, 3], [1, 3, 2])
```
