print("Gerenciamento de Finanças com Python e IA")

Nesse projeto, pude desenvolver habilidades em LLM e análise de dados. Utilizei as seguintes bibliotecas:
  1- ofxparse
  2- pandas
  3- datetime
  4- os
  5- langchain_openai
  6- langchain_groq
  7- langchain_core
  8- openai
  9- dotenv

Trabalhei da seguinte forma:
  1- Coloquei todos os extratos bancários da minha casa (por segurança, removi os extratos, porém não interfere na lógica)
  2- Criei um DataFrame para ler os extratos na pasta "extrato"
  3- Utilizei o ofxparse para unificar os arquivos e corrigi-los baseado no ISO=8859.1
  4- Criei as categorias ("Data", "Valor", "Descrição", "ID") com "transactions_data"
  5- alterei formatos de "Valo" e "Data"
  6- Concatenei os DataFrames
  7- Instanciei o dotenv
  8- Criei o Prompt com o que preciso para a categorização das despezas
  9- Instanciei a IA da GROQ com o modelo de LLM "llama-3.1-8b-instant"
  10- Criei um vetor com as transações e chamei o chat IA para ler todos os extratos e categorizar cada despeza, baseado no promt enviado
  11- Transformei em excel a planilha com as categorias 
