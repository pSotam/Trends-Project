import pandas as pd

#transforma a planilha em tabela manipulável
data_frame = pd.read_excel('skus.xlsx')
data_frame['Valor unitário'] = 0 #Muda a coluna inteira para 0 (Os preços não tem importancia aqui)

print(data_frame.head())
print('='*20)

print(data_frame.head())
print('='*20)
print(data_frame.columns)
print('='*20)
print(data_frame.info())

#Detecta quantos anúncios tem anúncio e quantos não tem
print('='*20)
sku_com_anuncio = data_frame['ID_MercadoLivre'].notnull().sum()
sku_sem_anuncio = data_frame['ID_MercadoLivre'].isnull().sum()

print(f'com anúncio: {sku_com_anuncio}')
print(f'sem anúncio: {sku_sem_anuncio}')
print(f'total: {len(data_frame)}')

#Detecta exatamente quais SKUs estão sem anúncio
print('='*20)
oportunidade = data_frame[(data_frame['Quantidade'] > 0) &
                          (data_frame['ID_MercadoLivre'].isnull())]
print(oportunidade[['SKU','Produto','Quantidade']])
