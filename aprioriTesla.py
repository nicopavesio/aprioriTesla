import numpy as np
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

np.random.seed(0)
num_samples = 100000

# Definición de los datos
data = {
    'Aceleracion': np.random.choice(['aceleracion baja', 'aceleracion media', 'aceleracion alta'], size=num_samples), 
    'Lluvia': np.random.choice(['llueve', 'no llueve'], size=num_samples),   
    'Hora_del_dia': np.random.choice(['mañana', 'tarde',  'noche'], size=num_samples), 
    'Trafico_elevado': np.random.choice(['trafico normal', 'trafico elevado'], size=num_samples), 
    'Obstaculo': np.random.choice(['obstaculo', 'no obstaculo'], size=num_samples),
}

# Agregar las columnas 'Frenar' y 'Cambio_de_carril'
data['Frenar'] = ['frenar' if (((acel == 'aceleracion media') and (traf == 'trafico elevado') and (lluv == 'llueve'))) 
                  or ((acel == 'aceleracion alta') and (obs == 'obstaculo')) 
                  or ((acel == 'aceleracion alta') and (traf == 'trafico elevado')) 
                  or ((acel == 'aceleracion alta') and (lluv == 'llueve')) 
                  or ((((acel == 'aceleracion baja') or (acel == 'aceleracion media')) and (traf == 'trafico elevado') and (lluv == 'llueve') and (obs == 'obstaculo')))
                  or ((acel == 'aceleracion alta') and (hora == 'noche'))
                  or ((acel == 'aceleracion media') and (hora == 'noche') and (lluv == 'llueve'))
                  else 'no frenar' for acel, traf, lluv, obs, hora in zip(data['Aceleracion'], data['Trafico_elevado'], data['Lluvia'], data['Obstaculo'], data['Hora_del_dia'])]

data['Cambio_de_carril'] = ['cambiar' if (((traf == 'trafico normal') and (obs == 'obstaculo') and (lluv == 'no llueve'))) 
                            or (( obs == 'obstaculo') and (traf == 'trafico normal') and  (acel != 'aceleracion alta') and (lluv == 'llueve'))
                            else 'no cambiar' for traf, lluv, obs, acel in zip(data['Trafico_elevado'], data['Lluvia'], data['Obstaculo'], data['Aceleracion'])]

# Convertir cada característica en una lista separada de transacciones
transactions = []
for feature, values in data.items():
    transactions.append(values)

# Aplanar la lista de transacciones y eliminar duplicados
flattened_transactions = [set(trans) for trans in zip(*transactions)]

# Aplicar TransactionEncoder
te = TransactionEncoder()
te_ary = te.fit(flattened_transactions).transform(flattened_transactions)
df_encoded = pd.DataFrame(te_ary, columns=te.columns_)

# Aplicar el algoritmo Apriori
frequent_itemsets = apriori(df_encoded, min_support=0.2, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.8)
print(rules[['antecedents', 'consequents', 'support', 'confidence']])






