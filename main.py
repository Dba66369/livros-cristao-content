#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GERADOR AUTOMÁTICO DE CONTEÚDO PROFÉTICO
Leitura Profética - REQUESTS PURO (v1 API do Gemini)
"""

import os
import json
import requests
from datetime import datetime
import sys

# CONFIGURAÇÃO - LEIA A CHAVE DA API
API_KEY = os.environ.get('GEMINI_API_KEY')
if not API_KEY:
    print("❌ GEMINI_API_KEY não encontrada")
    sys.exit(1)

# URL DIRETA DA API v1
API_URL = f"https://generativelanguage.googleapis.com/v1beta1/models/gemini-1.5-flash:generateContent?key={API_KEY}"
# PERSONA E ELEMENTOS OBRIGATÓRIOS
PERSONA = """Você é o Profeta Henry Otasowere, escritor cristão português.
Sua escrita é profética, profunda e transformadora.
Conecta a antiguidade bíbblica (Abraão, Elias, Jacó, Paulo) com a realidade contemporânea."""

ENDERECO = "Rua Diogo Brandão 63, Porto, PT"
AVISO_AMAZON = "⚠️ Como Associado da Amazon, recebo comissão pelas compras qualificadas."

def generate_content():
    """Gera conteúdo usando REQUEST PURO para API v1 do Gemini"""
    
    # LEITURA DO INPUT
    input_file = 'input.md'
    if not os.path.exists(input_file):
        print(f"❌ {input_file} não encontrado")
        return False
    
    with open(input_file, 'r', encoding='utf-8') as f:
        input_content = f.read()
    
    # PROMPT SIMPLES
    prompt = f"""{PERSONA}
Baseado neste conteúdo:
{input_content}
Gere um JSON com estes campos EXATAMENTE:
{{
    "post_blog_html": "POST HTML PARA BLOG (5 parágrafos com <p> tags)",
    "post_facebook": "POST RÁPIDO PARA FACEBOOK (150 caracteres)",
    "curiosidade_biblica": "CURIOSIDADE BÍBLICA (2 parágrafos sobre Abraão, Elias, Jacó, Paulo e o tema)"
}}
Inclua OBRIGATORIAMENTE:
- Endereço: {ENDERECO}
- Aviso: {AVISO_AMAZON}
Responda APENAS com o JSON, nada mais."""
    
    try:
        print("🤖 Gerando conteúdo via API v1...")
        
        # PAYLOAD PARA REQUESTS
        payload = {
            "contents": [
                {
                    "parts": [
                        {"text": prompt}
                    ]
                }
            ]
        }
        
        # FAZER REQUEST POST
        headers = {"Content-Type": "application/json"}
        response = requests.post(API_URL, json=payload, headers=headers, timeout=30)
        
        # LOG DETALHADO
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {response.headers}")
        print(f"Response Body: {response.text[:500]}")
        
        # VERIFICAR RESPOSTA
        if response.status_code != 200:
            print(f"❌ Erro na API: {response.status_code}")
            print(f"Resposta completa: {response.text}")
            return False
        
        # PARSEAR RESPOSTA
        response_data = response.json()
        
        # EXTRAIR CONTEÚDO GERADO
        if 'candidates' not in response_data or len(response_data['candidates']) == 0:
            print("❌ Nenhuma candidata gerada")
            print(f"Response: {response.text}")
            return False
        
        candidate = response_data['candidates'][0]
        if 'content' not in candidate or 'parts' not in candidate['content']:
            print("❌ Estrutura de resposta inválida")
            return False
        
        generated_text = candidate['content']['parts'][0]['text']
        
        # EXTRAIR JSON DA RESPOSTA
        json_text = generated_text.strip()
        if json_text.startswith('```'):
            json_text = json_text.split('```')[1]
        if json_text.startswith('json'):
            json_text = json_text[4:]
        json_text = json_text.strip()
        
        content_data = json.loads(json_text)
        
        # CRIAR MARKDOWN FINAL
        markdown_content = f"""# 📅 CONTEÚDO GERADO - {datetime.now().strftime('%d/%m/%Y às %H:%M')}
---
## 📱 POST FACEBOOK
{content_data.get('post_facebook', 'N/A')}
---
## 📄 POST BLOG
{content_data.get('post_blog_html', 'N/A')}
---
## 📚 CURIOSIDADE BÍBLICA
{content_data.get('curiosidade_biblica', 'N/A')}
---
**Endereço:** {ENDERECO}
{AVISO_AMAZON}
"""
        
        # SALVAR RESULTADO
        with open('RESULTADO_POST_DIARIO.md', 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        print("✅ Conteúdo gerado com sucesso!")
        print("📁 Salvo em: RESULTADO_POST_DIARIO.md")
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro na requisição: {e}")
        return False
    except json.JSONDecodeError as e:
        print(f"❌ Erro ao fazer parse do JSON: {e}")
        return False
    except Exception as e:
        print(f"❌ Erro geral: {e}")
        return False

if __name__ == "__main__":
    success = generate_content()
    sys.exit(0 if success else 1)
