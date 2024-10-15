import ofxparse
import ofxparse.ofxparse
import pandas as pd
import os
from datetime import datetime

df = pd.DataFrame()
for extrato in os.listdir("extratos"):
   # PARA VER OS EXTRATOS print(extrato)
   with open(f'extratos/{extrato}', encoding='ISO=8859-1') as ofx_file:
      ofx = ofxparse.OfxParser.parse(ofx_file)
      
      transactions_data = []
      for account in ofx.accounts:
        for transaction in account.statement.transactions: 
           transactions_data.append({
              "Data": transaction.date,
              "Valor": transaction.amount,
              "Descrição": transaction.memo,
              "ID": transaction.id,
       })
    
# PARA VISUALIZAR O QUE TEM DENTRO DO VETOR TRANSACTION dir(transaction)
df_temp = pd.DataFrame(transactions_data)
df_temp["Valor"] = df_temp["Valor"].astype(float)
df_temp["Data"] = df_temp["Data"].apply(lambda x: x.date())
df = pd.concat([df, df_temp])
df = pd.concat([df, df_temp])
# PARA OS VALORES SEREM IGUAL A 1 df["Valor"] = 1

#LLM =================
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

template = """
Você é um Analista de dados, trabalhando em um projeto de limpeza de dados.
Seu trabalho é escolher uma categoria adequada para cada lançamento financeiro que vou te enviar.

Todos são transações financeiras de uma pessoa física.

Escolha uma dentre as seguintes categorias:
- Despesas Eventuais
- Necessidades
- Roupa
- Saúde
- Presentes
- Beleza
- Desenvolvimento
- Lazer
- Assinaturas
- Uber/Transporte
- iFood/Restaurante
- Moradia
- Contas
- Mercado

Escolha a categoria deste item:
{text}

Responda apenas com a categoria
"""
prompt = PromptTemplate.from_template(template=template)
# chat = ChatGroq(model="llama-3.1.70b-versatile")
chat = ChatGroq(model="llama-3.1-8b-instant")
chain = prompt | chat


category = []
for transaction in list(df["Descrição"].values):
   category += [chain.invoke(transaction).content]
df["Categoria"] = category
df = df[df["Data"] >= datetime(2024, 1, 1).date()]
df.to_csv("finances.csv")
