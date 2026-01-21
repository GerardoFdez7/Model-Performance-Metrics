# Model Performance Metrics

Este proyecto implementa y compara dos métricas de evaluación de errores para modelos de regresión: **RMSE** (Raíz del Error Cuadrático Medio) y **MAE** (Error Absoluto Medio).

El código está escrito en Python puro, sin dependencias externas como `sklearn`.

## Requisitos

- Python 3.x instalado.

## Ejecución

Para ejecutar el script y ver los resultados de la comparación:

```bash
python main.py
```

## Descripción

El script `main.py` contiene:
1.  Implementación manual de las funciones `calculate_rmse` y `calculate_mae`.
2.  Un conjunto de datos de prueba (`y_real` vs `y_pred`).
3.  Cálculo y comparación de ambas métricas.
4.  Una explicación sobre por qué el RMSE penaliza más los errores grandes (outliers) en comparación con el MAE.
