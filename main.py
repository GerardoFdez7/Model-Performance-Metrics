# Inteligencia Articial
# José Gerardo Ruiz García - 23719
# Gerardo André Fernández Cruz - 23763

import math

def calculate_rmse(y_true, y_pred):
    """
    Calcula la Raíz del Error Cuadrático Medio (RMSE) desde cero.
    RMSE = sqrt(mean((y_true - y_pred)^2))
    """
    if len(y_true) != len(y_pred):
        raise ValueError("Las listas deben tener la misma longitud")
    
    squared_errors = [(yt - yp) ** 2 for yt, yp in zip(y_true, y_pred)]
    mean_squared_error = sum(squared_errors) / len(squared_errors)
    rmse = math.sqrt(mean_squared_error)
    return rmse

def calculate_mae(y_true, y_pred):
    """
    Calcula el Error Absoluto Medio (MAE) desde cero.
    MAE = mean(|y_true - y_pred|)
    """
    if len(y_true) != len(y_pred):
        raise ValueError("Las listas deben tener la misma longitud")
    
    absolute_errors = [abs(yt - yp) for yt, yp in zip(y_true, y_pred)]
    mae = sum(absolute_errors) / len(absolute_errors)
    return mae

# Datos proporcionados
y_real = [100, 150, 200, 250, 300]
y_pred = [110, 140, 210, 240, 500]

# 3. Comparación: Ejecución
rmse_val = calculate_rmse(y_real, y_pred)
mae_val = calculate_mae(y_real, y_pred)

# 3a. Imprimir ambos resultados
print(f"Resultados de las métricas:")
print(f"RMSE: {rmse_val:.2f}")
print(f"MAE:  {mae_val:.2f}")
print("-" * 30)

# 3b. Explicación final
print("Explicación:")
explanation = """
El RMSE penalizó más el error del último dato.
Esto se debe a que el RMSE eleva las diferencias al cuadrado antes de promediarlas, lo que magnifica
el impacto de los errores grandes como la predicción de 500 vs 300.
En el caso del MAE, todos los errores contribuyen linealmente al promedio.

Importancia en dosis de medicamentos:
Si estamos prediciendo dosis de medicamentos, un error grande (como dar 500mg en lugar de 300mg)
puede ser fatal o causar toxicidad grave, mientras que pequeños errores podrían ser tolerables.
Por lo tanto, preferiríamos el RMSE porque resalta desproporcionadamente esos errores catastróficos,
alertándonos de que el modelo no es seguro, mientras que el MAE podría "diluir" ese error grave
entre los otros aciertos.
"""
print(explanation)
