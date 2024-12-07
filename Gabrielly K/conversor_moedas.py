# Conversão de moedas: reais para dólar e euro
def conversao_moedas():
    try:
        # Taxas de câmbio
        taxa_dolar = float(input("Informe a taxa atual do dólar: "))
        taxa_euro = float(input("Informe a taxa atual do euro: "))

        # Valor em reais
        valor_reais = float(input("Informe o valor em reais: "))

        # Conversões
        valor_dolar = valor_reais / taxa_dolar
        valor_euro = valor_reais / taxa_euro

        # Exibição dos resultados
        print("\n--- Conversão de Moedas ---")
        print(f"Valor em reais: R$ {valor_reais:.2f}")
        print(f"Valor em dólar: US$ {valor_dolar:.2f}")
        print(f"Valor em euro: € {valor_euro:.2f}")
    except ValueError:
        print("Erro: Certifique-se de inserir valores numéricos válidos.")

# Executa a função
if __name__ == "__main__":
    conversao_moedas()
