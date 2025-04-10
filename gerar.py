import pandas as pd
import numpy as np

valor = [100.,50.,50.,60.,40.,50.,60.,60.,50.,60.0]
regioes = ['Sudeste', 'Norte','Sul']
produtos = ['Smartphone','Camisa','Arroz','Radio','Feijão','Tênis']

data = pd.DataFrame({
'Valor': np.random.choice(valor,100),
'Produtos':np.random.choice(produtos,100),
'Região':np.random.choice(regioes,100)},
)
print(data)

data.to_csv('dado.csv', index=True)
print('Ação realizada')
