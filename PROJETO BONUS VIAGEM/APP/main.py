import pandas as pd
import openpyxl
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACbf5a959fecd0de15643499385d5a00b5"
# Your Auth Token from twilio.com/console
auth_token = "a620ec003ce44e9c1810bb865126f312"
client = Client(account_sid, auth_token)


#Para cada arquivo verificar se algum valor na coluna vendas daquele arquivo é maior que 55mil
#Se for maior que 55mil, envia um sms → envia um sms com o nome o mês e as vendas do vendedor
#Caso não seja maior do que 55mil, não acontece nada


#Abrir os arquivos no excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] >= 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] >= 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] >= 55000, 'Vendas'].values[0]
        print(f"No mês de {mes} o vendedor {vendedor} bateu a meta de vendas de 55000, ao todo ele realizou {vendas} vendas")

        message = client.messages.create(
            to="+5515998251528",
            from_="+16283457754",
            body=f"No mês de {mes} o vendedor {vendedor} bateu a meta de vendas de 55000, ao todo ele realizou {vendas} vendas")

        print(message.sid)









