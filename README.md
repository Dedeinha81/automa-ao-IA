# 📞 Phone Extractor with Python & AI

Projeto desenvolvido para **extração automática de números de telefone** a partir de sites, combinando **Web Scraping** e **Inteligência Artificial**.

Este projeto foi criado com foco em **automação**, **tratamento de dados reais da web** e **integração com APIs de IA**, sendo ideal para portfólio profissional.

---

## 🚀 Funcionalidades

* Leitura de múltiplos sites a partir de um arquivo `.txt`
* Download do conteúdo HTML dos sites
* Limpeza e normalização do HTML (remoção de scripts, estilos, etc.)
* Análise do conteúdo usando IA para identificar telefones comerciais
* Tratamento de erros reais (SSL, timeout, indisponibilidade)
* Exportação dos resultados em arquivo `.csv`

---

## 🧠 Tecnologias Utilizadas

* **Python 3**
* **Requests** (requisições HTTP)
* **BeautifulSoup** (Web Scraping)
* **OpenAI API** (análise inteligente do conteúdo)
* **Manipulação de arquivos** (.txt e .csv)

---

## 📂 Estrutura do Projeto


phone_extractor_project/
│

├── main.py                 # Script principal

├── sites.txt               # Lista de sites para análise

├── requirements.txt        # Dependências do projeto

├── resultado_telefones.csv # Arquivo gerado com os resultados

└── README.md               # Documentação


---

## ▶️ Como Executar o Projeto

### 1️⃣ Clonar o repositório

git clone https://github.com/seu-usuario


### 2️⃣ Instalar as dependências

pip install -r requirements.txt
```

### 3️⃣ Configurar a API Key

No arquivo `main.py`, informe sua chave da OpenAI:

```python
API_KEY = "SUA_CHAVE_AQUI"
```

> ⚠️ **Observação:** a API da OpenAI pode exigir créditos ativos para execução completa.

---

### 4️⃣ Inserir os sites

No arquivo `sites.txt`, adicione um site por linha:

```
https://www.exemplo.com
www.empresa.com.br
```

### 5️⃣ Executar o script


python main.py


O resultado será gerado no arquivo:


resultado_telefones.csv

---

## 📊 Exemplo de Saída

URL;Telefone
https://www.exemplo.com;(41) 99999-9999
https://www.outrosite.com;Não encontrado

---

## ⚠️ Limitações Conhecidas

* Alguns sites possuem restrições de acesso ou certificados SSL inválidos
* A execução completa da IA depende de créditos disponíveis na API
* Sites com conteúdo altamente dinâmico podem não retornar telefones

Esses cenários são tratados no código e fazem parte do ambiente real de produção.

---

## 🎯 Objetivo do Projeto

Este projeto foi desenvolvido com fins **educacionais e de portfólio**, demonstrando habilidades em:

* Automação com Python
* Web Scraping
* Integração com IA
* Tratamento de exceções
* Organização de código

---

## 👩‍💻 Autora

**Andrea Leonardo**
Desenvolvedora Back-End | Python | Web Scraping | IA

🔗 LinkedIn: [https://www.linkedin.com/in/andrea-cruz-leonardo/](https://www.linkedin.com/in/andrea-cruz-leonardo/)

---

⭐ Se você gostou do projeto, deixe uma estrela no repositório!
