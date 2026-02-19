import os
import json
import google.generativeai as genai
from datetime import datetime

# Configuração da API
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-pro')

# Configurações fixas
AUTOR = "Henry Otasowere"
TONO = "Profético, profundo, profissional"
CONEXAO_TEOLOGICA = "Abraão, Elias, Jacó e Paulo"
CHAMADA_ACAO = "Visitar a igreja local na Rua Diogo Brandão 63, Porto, PT"
DISCLAIMER_AMAZON = "Como Associado Amazon, recebo comissão pelas compras qualificadas efetuadas através deste link."

def ler_input():
    """Lê o arquivo input.md"""
    try:
        with open('input.md', 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print("Erro: Arquivo input.md não encontrado!")
        return ""

def gerar_texto_blog(tema):
    """Gera texto para o blog em HTML"""
    prompt = f"""Você é um teólogo profético chamado {AUTOR}.
    
Gere um artigo profundo e profético sobre: {tema}

REQUISITOS OBRIGATÓRIOS:
1. Tom: {TONO}
2. Conectar teologicamente com: {CONEXAO_TEOLOGICA}
3. Incluir chamada para ação: {CHAMADA_ACAO}
4. Formato: HTML bem estruturado
5. Incluir disclaimer: {DISCLAIMER_AMAZON}

Responda APENAS com o HTML, sem explicações."""
    
    response = model.generate_content(prompt)
    return response.text

def gerar_post_facebook(tema):
    """Gera post para Facebook"""
    prompt = f"""Como {AUTOR}, crie um post provocador e envolvente para Facebook sobre: {tema}

REQUISITOS:
1. Máximo 280 caracteres
2. Tom: {TONO}
3. Menção a {CONEXAO_TEOLOGICA}
4. Include emoji apropriado
5. Insira hashtags relevantes (#LeituraProfética #Teologia #Fé)

Responda APENAS com o texto do post."""
    
    response = model.generate_content(prompt)
    return response.text

def gerar_curiosidade_biblica(tema):
    """Gera curiosidade bíblica"""
    prompt = f"""Crie uma curiosidade bíblica profunda sobre: {tema}

REQUISITOS:
1. Conectar com: {CONEXAO_TEOLOGICA}
2. Incluir versículo bíblico relevante
3. Formato: Texto simples, máximo 150 palavras
4. Tom: {TONO}
5. Incluir: {CHAMADA_ACAO}

Responda APENAS com a curiosidade."""
    
    response = model.generate_content(prompt)
    return response.text

def salvar_output(blog, facebook, curiosidade):
    """Salva o output em JSON para Make.com"""
    data = {
        "timestamp": datetime.now().isoformat(),
        "autor": AUTOR,
        "blog": blog,
        "facebook": facebook,
        "curiosidade_biblica": curiosidade,
        "status": "pronto_para_publicar"
    }
    
    with open('output.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print("✅ Arquivo output.json gerado com sucesso!")
    return data

def main():
    print("🔄 Lendo input.md...")
    tema = ler_input()
    
    if not tema:
        print("❌ Nenhum tema encontrado!")
        return
    
    print(f"📝 Tema lido: {tema[:50]}...")
    print("\n🤖 Gerando conteúdo com IA...")
    
    try:
        blog = gerar_texto_blog(tema)
        print("✅ Blog gerado")
        
        facebook = gerar_post_facebook(tema)
        print("✅ Post Facebook gerado")
        
        curiosidade = gerar_curiosidade_biblica(tema)
        print("✅ Curiosidade bíblica gerada")
        
        output = salvar_output(blog, facebook, curiosidade)
        print("\n🎉 Automação concluída!")
        print(f"📤 Pronto para ser enviado ao Make.com")
        
    except Exception as e:
        print(f"❌ Erro ao gerar conteúdo: {e}")

if __name__ == "__main__":
    main()
