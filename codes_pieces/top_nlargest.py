# Importar pandas
import pandas as pd

# Crear dataframe de ejemplo
df = pd.DataFrame({'cliente': ['A', 'B', 'A', 'B', 'C', 'C', 'A', 'B', 'A'], 'gruposhopper': ['G1', 'G1', 'G2', 'G2', 'G1', 'G2', 'G1', 'G2', 'G1'], 'referencia': [
                  'R1', 'R2', 'R2', 'R2', 'R1', 'R2', 'R3', 'R3', 'R4'], 'unidades': [10, 20, 30, 40, 50, 60, 20, 5, 10]})

df=df.sort_values(by=["cliente","gruposhopper",'unidades'],ascending=[False,False,False]) 
print(df)
# Obtener el top 3 por cliente, gruposhopper y referencia a partir de las unidades
df_top3 = df.groupby(['cliente', 'gruposhopper']).apply(lambda x: x.nlargest(2, 'unidades')).reset_index(drop=True) 
# Imprimir resultado
print(df_top3)
