# aprioriTesla
Usando el algoritmo apriori para predecir comportamientos en coches
Requisitos:
  numpy
  pandas
  mlxtend

DEFINICIÓN DE LOS DATOS

En esta etapa, se han creado datos simulados que representan el comportamiento de conducción de una flota de vehículos Tesla. Estos datos incluyen características como la aceleración, la lluvia, la hora del día, el tráfico elevado y la presencia de obstáculos. Cada característica se ha asignado valores aleatorios para simular diferentes condiciones de conducción.
Se han agregado dos nuevas características, 'Frenar' y 'Cambio_de_carril', en función de condiciones específicas de las características existentes. Por ejemplo, 'Frenar' se activa si la aceleración es alta en situaciones de tráfico elevado o lluvia, entre otras condiciones. De manera similar, 'Cambio_de_carril' se activa en base a condiciones particulares de tráfico y la presencia de obstáculos.


PREPARACIÓN DE LOS DATOS


Para preparar los datos para el análisis de reglas de asociación, cada característica se convierte en una lista separada de transacciones, donde cada transacción representa un viaje individual. Estas listas se combinan y se aplanan para obtener una lista única de transacciones que contenga todas las características.
El TransactionEncoder es una herramienta clave de preprocesamiento que convierte las transacciones en un formato de matriz binaria. Cada fila representa una transacción (es decir, un viaje de conducción) y cada columna representa un valor posible para una característica específica


APLICACIÓN DEL ALGORITMO


El algoritmo Apriori es un método popular para encontrar patrones frecuentes en conjuntos de datos. En este contexto, se aplica al conjunto de datos transformado por el TransactionEncoder. Configurado con un umbral de soporte mínimo en 0.2 y mostrando los que tienen una confianza mayor al 80%, el algoritmo identifica conjuntos de características que ocurren con una frecuencia significativa, lo que permite descubrir patrones de comportamiento de conducción relevantes.


CONCLUSIONES


Aceleración Alta:
Se observa una alta confianza (91.86%) en la asociación entre la aceleración alta y la necesidad de frenar. Esto sugiere que el coche va a tener que frenar con mayor frecuencia cuando acelere rápidamente. También hay una alta confianza (87.63%) en que la aceleración alta está asociada con la decisión de no cambiar de carril. Esto indica que el coche debe ser más propenso a mantenerse en su carril cuando acelera rápidamente para evitar accidentes por pérdida de control.

Aceleración Baja:
La aceleración baja está fuertemente asociada (87.69% de confianza) con la decisión de no frenar. Esto sugiere que los coches que aceleran lentamente tienen menos necesidad de frenar con frecuencia.

Cambio de Carril:
Cambiar de carril está altamente asociado con la presencia de obstáculos y el tráfico normal, con una confianza del 100% en ambas reglas. Esto indica que los coches pueden cambiar de carril para evitar obstáculos o para navegar en condiciones de tráfico fluido.

Frenar:
El frenar está fuertemente asociado con la lluvia y el tráfico elevado, con una confianza del 95.51% y del 100% respectivamente. Esto sugiere que los conches deben tender a frenar más en condiciones de lluvia y en presencia de tráfico pesado.

Lluvia:
La lluvia está asociada con un alto índice de frenado (95.51% de confianza) y con la decisión de no cambiar de carril (83.19% de confianza). Esto indica que los coches deben ser más cautelosos y deben tender a mantenerse en su carril durante la lluvia.

Tráfico Elevado:
El tráfico elevado está fuertemente asociado con la decisión de no cambiar de carril (100% de confianza) y con la necesidad de frenar (100% de confianza). Esto sugiere que, en situaciones de tráfico pesado, los coches deben mantenerse en su carril y a frenar con más frecuencia para adaptarse a las condiciones del tráfico.
