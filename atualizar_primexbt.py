import json
import time
import requests


def baixar_candles_primexbt(symbol="BTCUSD", resolution="30m", limit=120):
  # Endpoint público da API da PrimeXBT v3.0 conforme a documentação
  url = "https://api.primexbt.com/v3/trading/bars"
  params = {"symbol": symbol, "resolution": resolution, "limit": limit}

  try:
    resposta = requests.get(url, params=params, timeout=10)
    if resposta.status_code == 200:
      dados_brutos = resposta.json()

      # Estrutura padrão para o site ler
      payload = {"symbol": symbol, "resolution": resolution, "candles": dados_brutos}

      with open("primexbt_candles.json", "w") as f:
        json.dump(payload, f, indent=2)

      print(
          f"[Sucesso] Dados de {symbol} ({resolution}) atualizados da PrimeXBT."
      )
    else:
      print(f"[Erro API PrimeXBT] Status Code: {resposta.status_code}")
  except Exception as e:
    print(f"[Erro de Conexão]: {e}")


# Loop para atualizar a cada 30 segundos
if __name__ == "__main__":
  print("=== Sincronizador PrimeXBT Iniciado ===")
  while True:
    # Podes alterar o símbolo (ex: 'TSLA', 'XAGUSD', 'BTCUSD') e o timeframe ('30m', '1h', etc.)
    baixar_candles_primexbt(symbol="BTCUSD", resolution="30m", limit=120)
    time.sleep(30)
