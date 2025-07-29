import gspread
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os

# --- CONFIGURAÇÃO ---
# Escopos definem o nível de acesso que estamos solicitando.
SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

# Mapeamento dos códigos dos carrinhos para os nomes das planilhas
MAPA_CARRINHOS = {
    "073990": "Inventário Carrinho 1",
    "CARRINHO_2": "Inventário Carrinho 2",
    "CARRINHO_3": "Inventário Carrinho 3",

}


# --- FUNÇÕES ---

def autenticar():
    """
    Autentica com a API do Google usando um fluxo de OAuth 2.0.
    Cria um 'token.json' para armazenar as credenciais para execuções futuras.
    """
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    return gspread.authorize(creds)

def main():
    """Função principal para executar o scanner."""
    print("Iniciando o sistema de scanner...")
    
    try:
        client = autenticar()
        print("✓ Autenticação com a Google bem-sucedida.")
    except FileNotFoundError:
        print("✗ ERRO: Ficheiro 'credentials.json' não encontrado.")
        print("   Certifique-se de que transferiu o ficheiro e o guardou na mesma pasta que este script.")
        return
    except Exception as e:
        print(f"✗ Ocorreu um erro inesperado durante a autenticação: {e}")
        return

    # PASSO 1: Escanear o carrinho para selecionar a planilha correta
    worksheet = None
    nome_planilha = ""
    while not worksheet:
        print("\n--- SELEÇÃO DE CARRINHO ---")
        codigo_carrinho = input("➡️  Por favor, escaneie o QR Code do CARRINHO: ")

        if codigo_carrinho in MAPA_CARRINHOS:
            try:
                nome_planilha = MAPA_CARRINHOS[codigo_carrinho]
                spreadsheet = client.open(nome_planilha)
                worksheet = spreadsheet.sheet1 # Acede à primeira aba da planilha
                print(f"✓ Carrinho reconhecido! A trabalhar com a planilha: '{nome_planilha}'.")
            except gspread.exceptions.SpreadsheetNotFound:
                print(f"   ✗ ERRO: Planilha '{nome_planilha}' não encontrada no seu Google Drive.")
                print("      Por favor, crie uma planilha com este nome exato e tente novamente.")
            except Exception as e:
                print(f"   ✗ Ocorreu um erro ao abrir a planilha: {e}")
        else:
            print(f"   ✗ ERRO: QR Code do carrinho inválido ('{codigo_carrinho}'). Tente novamente.")
            
    # PASSO 2: Escanear os Chromebooks
    print("\n✔️ --- Scanner de Chromebooks Ativado ---")
    print("Comece a escanear os códigos dos CHROMEBOOKS.")
    print("Digite 'sair' e pressione Enter para finalizar.")

    while True:
        serial = input()

        if serial.lower() == 'sair':
            break
        
        if not serial:
            continue

        try:
            worksheet.append_row([serial])
            print(f"  ✔️ ADICIONADO: Serial '{serial}' registado na planilha '{nome_planilha}'.")
        except Exception as e:
            print(f"  ✗ ERRO ao enviar para a planilha: {e}")

    print("\nA finalizar o scanner...")
    print("Sistema encerrado.")

if __name__ == '__main__':
    main()
