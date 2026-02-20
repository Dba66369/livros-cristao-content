# -*- coding: utf-8 -*-
import os
import json
import google.generativeai as genai
from datetime import datetime

# Configuracao da API
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# Force a versao estavel da API para evitar o erro 404 do v1beta
# Use o modelo flash, que e o mais rapido e estavel para automacoes
model = genai.GenerativeModel(
    model_name='gemini-1.5-flash',
    generation_config={
        "temperature": 0.7,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
    }
)
# Configuracoes fixas
AUTOR = "Henry Otasowere"
TONO = "Profetico, profundo, profissional"
CONEXAO_TEOLOGICA = "Abraao, Elias, Jaco e Paulo"
CHAMADA_ACAO = "Visitar a igreja local na Rua Diogo Brandao 63, Porto, PT"
DISCLAIMER_AMAZON = "Como Associado Amazon, recebo comissao pelas compras qualificadas efetuadas atraves deste link."

def ler_input():
    """Le o arquivo input.md"""
    try:
        with open('input.md', 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print("[ERRO] Arquivo input.md nao encontrado!")
        return ""

def gerar_texto_blog(tema):
    """Gera texto para o blog em HTML"""
    prompt = f"""Voce e um teologo profetico chamado {AUTOR}.
    
Gere um artigo profundo e profetico sobre: {tema}
REQUISITOS OBRIGATORIOS:
1. Tom: {TONO}
2. Conectar teologicamente com: {CONEXAO_TEOLOGICA}
3. Incluir chamada para acao: {CHAMADA_ACAO}
4. Formato: HTML bem estruturado
5. Incluir disclaimer: {DISCLAIMER_AMAZON}
Responda APENAS com o HTML, sem explicacoes."""
    
    response = model.generate_content(prompt)
    return response.text

def gerar_post_facebook(tema):
    """Gera post para Facebook"""
    prompt = f"""Como {AUTOR}, crie um post provocador e envolvente para Facebook sobre: {tema}
REQUISITOS:
1. Maximo 280 caracteres
2. Tom: {TONO}
3. Mencao a {CONEXAO_TEOLOGICA}
4. Include emoji apropriado
5. Insira hashtags relevantes (#LeituraProfética #Teologia #Fe)
Responda APENAS com o texto do post."""
    
    response = model.generate_content(prompt)
    return response.text

def gerar_curiosidade_biblica(tema):
    """Gera curiosidade biblica"""
    prompt = f"""Crie uma curiosidade biblica profunda sobre: {tema}
REQUISITOS:
1. Conectar com: {CONEXAO_TEOLOGICA}
2. Incluir versículo bíblico relevante
3. Formato: Texto simples, maximo 150 palavras
4. Tom: {TONO}
5. Incluir: {CHAMADA_ACAO}
Responda APENAS com a curiosidade."""
    
    response = model.generate_content(prompt)
    return response.text

def salvar_output(blog, facebook, curiosidade):
    """Salva o output em JSON e Markdown para Make.com"""
    data = {
        "timestamp": datetime.now().isoformat(),
        "autor": AUTOR,
        "blog": blog,
        "facebook": facebook,
        "curiosidade_biblica": curiosidade,
        "status": "pronto_para_publicar"
    }
    
    # Salvar JSON
    with open('output.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    # Salvar Markdown (arquivo que a workflow espera)
    markdown_content = f"""# Post Diario Gerado - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Autor
{AUTOR}

## Facebook Post
```
{facebook}
```

## Blog
{blog}

## Curiosidade Biblica
{curiosidade}

## Status
{data['status']}
"""
    
    with open('RESULTADO_POST_DIARIO.md', 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    print("[OK] Arquivo output.json gerado com sucesso!")
    print("[OK] Arquivo RESULTADO_POST_DIARIO.md gerado com sucesso!")
    return data

def main():
    print("[INICIANDO] Lendo input.md...")
    tema = ler_input()
    
    if not tema:
        print("[ERRO] Nenhum tema encontrado!")
        return
    
    print(f"[LIDO] Tema recebido: {tema[:50]}...")
    print("[PROCESSANDO] Gerando conteudo com IA...")
    
    try:
        blog = gerar_texto_blog(tema)
        print("[OK] Blog gerado")
        
        facebook = gerar_post_facebook(tema)
        print("[OK] Post Facebook gerado")
        
        curiosidade = gerar_curiosidade_biblica(tema)
        print("[OK] Curiosidade biblica gerada")
        
        output = salvar_output(blog, facebook, curiosidade)
        print("\n[SUCESSO] Automacao concluida!")
        print("[PRONTO] Arquivos prontos para serem enviados ao Make.com")
        
    except Exception as e:
        print(f"[ERRO] Erro ao gerar conteudo: {e}")
        raise

if __name__ == "__main__":
    main()
