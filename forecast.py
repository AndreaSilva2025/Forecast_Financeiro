import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import os

# --- EXECUTAR COM ARQUIVO CSV ---
def forecast_de_csv(caminho_csv, meses_previsao=12):
    df = pd.read_csv(caminho_csv)
    df['Mes'] = pd.to_datetime(df['Mes'])
    df.set_index('Mes', inplace=True)
    df = df.sort_index()

    # ⚠️ Previsão só com tendência (sem sazonalidade)
    modelo = ExponentialSmoothing(df['Receita'], trend='add')
    ajustado = modelo.fit()
    previsao = ajustado.forecast(meses_previsao)

    # Gráfico
    plt.figure(figsize=(10, 5))
    plt.plot(df['Receita'], label='Histórico', marker='o')
    plt.plot(previsao, label='Previsão', linestyle='--', marker='x')
    plt.title(f'Forecast Financeiro - Próximos {meses_previsao} Meses')
    plt.xlabel('Data')
    plt.ylabel('Receita (R$)')
    plt.legend()
    plt.grid(True)

    # Salvar imagem
    os.makedirs("imagens", exist_ok=True)
    caminho_imagem = "imagens/grafico_forecast.png"
    plt.savefig(caminho_imagem)
    plt.close()

    print("✅ Gráfico salvo em:", caminho_imagem)
    print("📈 Previsão para os próximos", meses_previsao, "meses:")
    print(previsao.round(2))


# 🟢 Rodar função com o arquivo CSV
forecast_de_csv("dados_receita.csv", meses_previsao=12)
