import pandas as pd
import matplotlib.pyplot as plt

# Se carga el dataset desde la carpeta datos
df = pd.read_csv('datos/ventas.csv')

# Se calcula el total de ventas (cantidad x precio)
df['total'] = df['cantidad'] * df['precio']

# Ventas totales del período
ventas_totales = df['total'].sum()
print(f"Ventas totales: ${ventas_totales:,.0f}")

# Producto más vendido por cantidad
mas_vendido = df.groupby('producto')['cantidad'].sum().idxmax()
print(f"Producto más vendido: {mas_vendido}")

# Ventas por mes
df['fecha'] = pd.to_datetime(df['fecha'])
df['mes'] = df['fecha'].dt.to_period('M')
ventas_por_mes = df.groupby('mes')['total'].sum()
print("\nVentas por mes:")
print(ventas_por_mes)

# Gráfico de evolución de ventas
ventas_por_mes.plot(kind='bar', color='steelblue')
plt.title('Evolución de Ventas por Mes')
plt.xlabel('Mes')
plt.ylabel('Total ($)')
plt.tight_layout()
plt.savefig('resultados/grafico_ventas.png')
plt.show()
print("Gráfico guardado en resultados/")
