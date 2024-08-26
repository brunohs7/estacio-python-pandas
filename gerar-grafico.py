import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ler a planilha Excel
df = pd.read_excel('CONTROLE MILHAS 2023.1.xlsx', sheet_name='CTRL 2024')

# Verificar os nomes das colunas
print(df.columns)

# Supondo que as colunas sejam 'MÊS', 'RECEITA', 'CUSTO' e 'LUCRO'
df['MÊS'] = pd.to_datetime(df['MÊS'])  # Converte para datetime

# Filtrar os dados até o mês de julho
df = df[df['MÊS'].dt.month <= 7]

# Converter para o formato 'Jan/2024'
df['MÊS'] = df['MÊS'].dt.strftime('%b/%Y')

# Gerar um gráfico de linha
plt.figure(figsize=(12, 8))

# Plotar as três linhas: Receita, Custo e Lucro
sns.lineplot(data=df, x='MÊS', y='RECEITA', label='Receita', marker='o')
sns.lineplot(data=df, x='MÊS', y='CUSTOS + DESP', label='Custo', marker='o')
sns.lineplot(data=df, x='MÊS', y='LUCRO', label='Lucro', marker='o')

plt.title('Receita, Custo e Lucro Mensal')
plt.xlabel('Mês')
plt.ylabel('Valores (R$)')

# Ajustar os limites e o intervalo do eixo Y
plt.ylim(bottom=0)  # Define o limite inferior do eixo Y como 0
plt.yticks(range(0, int(df[['RECEITA', 'CUSTO', 'LUCRO']].max().max()) + 5000, 5000))  # Define o intervalo dos ticks do eixo Y

# Rotacionar as labels do eixo X para melhor legibilidade
plt.xticks(rotation=45)

# Adicionar uma grade para melhor visualização
plt.grid(True)

# Exibir a legenda
plt.legend()

# Mostrar o gráfico
plt.show()