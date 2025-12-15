
# IMPORTS 
import os
import requests
from bs4 import BeautifulSoup
from openai import OpenAI

# CONFIGURAÇÃO
API_KEY = "Sua Chave Aqui"

INPUT_FILE = "sites.txt"
OUTPUT_FILE = "resultado_telefones.csv"

MODELO = "gpt-4.1-mini"   # MAIS BARATO

# Inicializa o cliente
client = OpenAI(api_key=API_KEY)


def limpar_html(html_content):
    """
    Remove partes desnecessárias do HTML para economizar tokens.
    """
    soup = BeautifulSoup(html_content, 'html.parser')

    for element in soup(["script", "style", "meta", "noscript", "header", "svg", "path"]):
        element.extract()

    return soup.get_text(separator="\n")


def extrair_telefone_com_ia(texto_site, url):
    """
    Usa a IA da OpenAI para extrair número de telefone.
    Agora utilizando a NOVA API (responses.create).
    """
    sistema = (
        "Você é especialista em extrair telefones de HTML. "
        "Procure números visíveis e também números dentro de links (href, parâmetros phone= etc). "
        "Retorne APENAS o telefone encontrado, no formato mais limpo possível. "
        "Se não houver, retorne 'Não encontrado'."
    )

    usuario = f"URL: {url}\n\nConteúdo do site:\n{texto_site}\n\nExtraia o telefone:"

    try:
        resposta = client.responses.create(
            model=MODELO,
            input=[
                {"role": "system", "content": sistema},
                {"role": "user", "content": usuario}
            ]
        )

        return resposta.output_text.strip()

    except Exception as e:
        return f"Erro IA: {e}"


def processar_sites():
    if not os.path.exists(INPUT_FILE):
        print(f"Erro: arquivo '{INPUT_FILE}' não encontrado.")
        return

    # Lê os sites do arquivo
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        sites = [s.strip() for s in f.readlines() if s.strip()]

    print(f"Iniciando extração de {len(sites)} sites...\n")

    # Cabeçalho do CSV
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f_out:
        f_out.write("URL;Telefone\n")

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    for site in sites:
        url = site if site.startswith("http") else f"https://{site}"
        print(f"Processando: {url}...", end="\r")

        try:
            resposta = requests.get(url, headers=headers, timeout=15)
            resposta.raise_for_status()

            html_limpo = limpar_html(resposta.content)
            telefone = extrair_telefone_com_ia(html_limpo, url)

            print(f"[OK] {url} -> {telefone}")

            with open(OUTPUT_FILE, 'a', encoding='utf-8') as f_out:
                f_out.write(f"{url};{telefone}\n")

        except requests.exceptions.RequestException as e:
            print(f"[ERRO] {url}: {e}")
            with open(OUTPUT_FILE, 'a', encoding='utf-8') as f_out:
                f_out.write(f"{url};Erro de conexão\n")

        except Exception as e:
            print(f"[ERRO GERAL] {url}: {e}")
            with open(OUTPUT_FILE, 'a', encoding='utf-8') as f_out:
                f_out.write(f"{url};Erro desconhecido\n")


if __name__ == "__main__":
    processar_sites()
