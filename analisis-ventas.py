import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
df = pd.read_csv("ventas.csv")

# Total ventas
print("Total ventas:", df["Sales"].sum())

# Producto más vendido
top = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)
print(top)

# Gráfico
top.plot(kind="bar")
plt.title("Productos más vendidos")
plt.show()