# 🖨️ Scanner de Chromebooks para Inventário em Google Sheets

![Status](https://img.shields.io/badge/status-funcional-green)
![Linguagem](https://img.shields.io/badge/python-3.x-blue)

---

## 📖 Descrição

Script em **Python** para escanear **Chromebooks** e registrar os seriais em uma **Planilha Google**. Desenvolvido para facilitar o inventário de dispositivos, utilizando **QR Codes** para identificar o carrinho de Chromebooks e registrar automaticamente os números de série.

---

## ✨ Funcionalidades

- 🔐 **Autenticação Segura:** OAuth 2.0 com geração automática de `token.json`.
- 📋 **Seleção Dinâmica de Planilha:** Identifica o carrinho via QR Code.
- 🔁 **Registro Contínuo:** Escaneia múltiplos dispositivos em sequência.
- 💻 **Interface CLI:** Totalmente operado via terminal.

---

## 🚀 Tecnologias Utilizadas

- 🐍 **Python 3**
- 📄 **gspread** — integração com Google Sheets
- 🔐 **google-auth-oauthlib** — autenticação OAuth 2.0

---

## ⚠️ Pré-requisitos de API do Google

1. Acesse o [Google Cloud Console](https://console.cloud.google.com/) e crie um projeto.
2. Ative as APIs:
   - Google Sheets API
   - Google Drive API
3. Crie as **credenciais OAuth 2.0** (App para computador).
4. Baixe o arquivo `credentials.json`.

---

## ⚙️ Instalação e Configuração

### 1. Clone o Repositório
```bash
git clone https://github.com/andreguiot/scanner-chromebooks.git
cd scanner-chromebooks
```

### 2. Instale as Dependências
Crie um ambiente virtual (opcional) e execute:
```bash
pip install -r requirements.txt
```

**Conteúdo de `requirements.txt`:**
```
gspread
google-auth-oauthlib
google-auth-transport-requests
```

### 3. Adicione as Credenciais
- Copie o `credentials.json` para a raiz do projeto (mesma pasta do script).

### 4. Configure o Script
- Edite o dicionário `MAPA_CARRINHOS` no `scanner.py`.
- Use os QR Codes dos carrinhos como chaves e os nomes das planilhas como valores.

---

## 💻 Como Usar

1. Execute o script:
```bash
python scanner.py
```

2. **Primeira execução:**
   - Será aberto um navegador pedindo autorização do Google.
   - Após aceitar, será gerado o `token.json` localmente.

3. **Escaneamento:**
   - Escaneie o QR Code do carrinho.
   - Depois, escaneie os QR Codes dos Chromebooks.
   - Digite `sair` para encerrar.

---

## 🔒 Segurança

- 🔒 **`credentials.json`** e **`token.json`** são arquivos sensíveis.
- ✔️ Já estão listados no `.gitignore`.
- 🚫 **Nunca envie esses arquivos para o GitHub.**

---

## ✒️ Autor

**André Guiot**

- GitHub: [@andreguiot](https://github.com/andreguiot)
