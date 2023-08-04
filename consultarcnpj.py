import requests
import telebot

# CRIADO POR XMROOT(DEIXE OS CREDITOS)
# CRIADO POR XMROOT(DEIXE OS CREDITOS)
# CRIADO POR XMROOT(DEIXE OS CREDITOS)
# CRIADO POR XMROOT(DEIXE OS CREDITOS)
# CRIADO POR XMROOT(DEIXE OS CREDITOS)
# CRIADO POR XMROOT(DEIXE OS CREDITOS)
# CRIADO POR XMROOT(DEIXE OS CREDITOS)
# CRIADO POR XMROOT(DEIXE OS CREDITOS)

bot = telebot.TeleBot('DOIS_CLICKS_COLA') # TOKEN DO BOT

@bot.message_handler(commands=['cnpj'])
def cnpj_handler(message):
    args = message.text.split(' ')[1:]
    if not args:
        bot.reply_to(message, "Por favor, digite um CNPJ.")
        return
    cnpj = "/".join(args)
    url = f"https://hyb.com.br/curl_cnpj.php?action=acessa_curl&cnpj={cnpj}"
    headers = {
        'Host': 'hyb.com.br',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',
        'Accept': '*/*',
        'Origin': 'https://hyb.com.br',
        'Referer': 'https://hyb.com.br/assinatura',
        'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,gl;q=0.6',
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        response_str = (
            f"[CNPJ: {data['cnpj']}\n"
            f"Matriz/Filial: {data['matriz_filial']}\n"
            f"Razão Social: {data['razao_social']}\n"
            f"Nome Fantasia: {data['nome_fantasia']}\n"
            f"Situação: {data['situacao']}\n"
            f"Data Situação: {data['data_situacao']}\n"
            f"Motivo Situação: {data['motivo_situacao']}\n"
            f"Cidade Exterior: {data['nm_cidade_exterior']}\n"
            f"Código País: {data['cod_pais']}\n"
            f"Nome País: {data['nome_pais']}\n"
            f"Código Natureza Jurídica: {data['cod_nat_juridica']}\n"
            f"Data Início Atividade: {data['data_inicio_ativ']}\n"
            f"CNAE Fiscal: {data['cnae_fiscal']}\n"
            f"Tipo Logradouro: {data['tipo_logradouro']}\n"
            f"Logradouro: {data['logradouro']}\n"
            f"Número: {data['numero']}\n"
            f"Complemento: {data['complemento']}\n"
            f"Bairro: {data['bairro']}\n"
            f"CEP: {data['cep']}\n"
            f"UF: {data['uf']}\n"
            f"Código Município: {data['cod_municipio']}\n"
            f"Município: {data['municipio']}\n"
            f"Telefone 1: {data['telefone_1']}\n"
            f"Telefone 2: {data['telefone_2']}\n"
            f"Fax: {data['num_fax']}\n"
            f"Email: {data['email']}\n"
            f"Qualificação Responsável: {data['qualif_resp']}\n"
            f"Capital Social: {data['capital_social']}\n"
            f"Porte: {data['porte']}\n"
            f"Opção Simples: {data['opc_simples']}\n"
            f"Data Opção Simples: {data['data_opc_simples']}\n"
            f"Data Exclusão Simples: {data['data_exc_simples']}\n"
            f"Opção MEI: {data['opc_mei']}\n"
            f"Situação Especial: {data['sit_especial']}\n"
            f"Data Situação Especial: {data['data_sit_especial']}\n"
            f"CRIADO POR XMROOT(DEIXE OS CREDITOS)\n"
        )
        response_str += "CNAE:\n"
        for cnae in data['cnae']:
            response_str += f"- {cnae}\n"
        response_str += "Sócios:\n"
        for socio in data['socios']:
            response_str += f"- {socio}\n"

        bot.reply_to(message, response_str)
    else:
        bot.reply_to(message, "Erro na API.")
bot.polling()

# CRIADO POR XMROOT(DEIXE OS CREDITOS)