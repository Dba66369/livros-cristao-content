#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GERADOR AUTÓMTICO DE CONTEÚDO PROFÙTICO
Leitura Profética - Minimalista (sem complexidade)
"""

import google.generativeai as genai
import os
import json
from datetime import datetime

# CONFIGURAÇÃO MINIMALISTA - SEM COMPLICAÇÕES
API_KEY = os.environ.get('GEMINI_API_KEY')
if not API_KEY:
    print("❌ GEMINI_API_KEY não encontrada")
    exit(1)

# Configurar API - SEM transport, SEM client_options
genai.configure(api_key=API_KEY)

# Criar modelo - SIMPLES E DIRETO
model = genai.GenerativeModel('gemini-1.5-flash')
# PERSONA INJETADA NO PROMPT
PERSONA = """Você é o Profeta Henry Otasowere, escritor cristão português.
Sua escrita é profética, profunda e transformadora.
Conecta a antiguidade bíbblica com a realidade contemporânea."""

# ELEMENTOS OBRIGATÓRIOS
ENDERECO = "Rua Diogo Brandão 63, Porto, PT"
AVISO_AMAZON = "⚠️ Como Associado da Amazon, recebo comissão pelas compras qualificadas."

def generate_content():
    """Gera conteúdo minimalista - SEM erros de API"""
    
    # LEITURA DO INPUT
    input_file = 'input.md'
    if not os.path.exists(input_file):
        print(f"❌ {input_file} não encontrado")
        return False
    
    with open(input_file, 'r', encoding='utf-8') as f:
        input_content = f.read()
    
    # PROMPT SIMPLES E DIRETO
    prompt = f"""{PERSONA}

Baseado neste conteúdo:
{input_content}

Gere um JSON com estes campos EXATAMENTE:
{{
    "post_blog_html": "POST HTML PARA BLOG (5 parágrafos com <p> tags)",
    "post_facebook": "POST RÁPIDO PARA FACEBOOK (150 caracteres)",
    "curiosidade_biblica": "CURIOSIDADE BÍBLICA (2 parágrafos sobre o tema)"
}}

Inclua OBRIGATORIAMENTE:
- Endereço: {ENDERECO}
- Aviso: {AVISO_AMAZON}

Responda APENAS com o JSON, nada mais."""

    try:
        print("🤖 Gerando conteúdo...")
        response = model.generate_content(prompt)
        
        # EXTRAIR JSON DO RESPONSE
        json_text = response.text.strip()
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
        
    except Exception as e:
        print(f"❌ Erro ao gerar: {e}")
        return False

if __name__ == "__main__":
    success = generate_content()
    exit(0 if success else 1)
