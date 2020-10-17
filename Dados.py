import math
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns',None)
x= pd.read_excel(r"e:/desafio/planilha_de_repasse.xlsx")
x['Teste']=0
x['Estorno']=0
x['Conciliação']=0
x['Teste'] = x['Teste'].mask((x['Método de pagamento']== 'Cartão de Crédito') | (x['Método de pagamento']== 'Boleto'),round((x['Valor bruto da parcela']*x['% Comissão'])/100,ndigits=2))
x['Estorno'] = x['Estorno'].mask(x['Método de pagamento']== 'Estorno',round((x['Valor bruto do pedido']*x['% Comissão'])/100,ndigits=2))
x['Comissão ML por parcela'] = x['Comissão ML por parcela'].mask(x['Método de pagamento']== 'Transferência',x['Valor da antecipação'])
x['Valor bruto da parcela'] = x['Valor bruto da parcela'].mask(x['Método de pagamento']== 'Transferência',x['Valor líquido da parcela'])
x['Conciliação'] = x['Conciliação'].mask((x['Teste']== x['Comissão ML por parcela']) & ((x['Método de pagamento']== 'Boleto') |(x['Método de pagamento']== 'Cartão de Crédito')),'Conciliado')
x['Conciliação'] = x['Conciliação'].mask((x['Teste']!= x['Comissão ML por parcela']) & ((x['Método de pagamento']== 'Boleto') |(x['Método de pagamento']== 'Cartão de Crédito')),'Não Conciliado')
x['Conciliação'] = x['Conciliação'].mask((x['Estorno']!= x['Valor líquido da parcela'])& (x['Método de pagamento']== 'Estorno'),'Não Conciliado')
x['Conciliação'] = x['Conciliação'].mask((x['Estorno']== x['Valor líquido da parcela'])& (x['Método de pagamento']== 'Estorno'),'Não Conciliado')
x['Conciliação'] = x['Conciliação'].mask((x['Valor da antecipação']>0)& (x['Método de pagamento']== 'Transferência'),'Retirada')
x['Conciliação'] = x['Conciliação'].mask((x['Valor da antecipação']<0)& (x['Método de pagamento']== 'Transferência'),'Movimentação')
print(x[['Data da transação','ID do pedido Seller','Método de pagamento','Comissão ML por parcela','Valor bruto da parcela','% Comissão','Conciliação']])
