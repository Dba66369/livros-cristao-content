# 🧪 Guia de Teste e Validação - Sistema de Agentes IA

## 👋 Resumo Executívo

Este documento descreve os TESTES e VALIDAÇÕES do sistema de agentes IA para geração de conteúdo.

**Data:** 20 de Fevereiro de 2026  
**Status:** ✅ PRONTO PARA TESTE SEM INTERRUPÇÃO  
**Versão:** 1.0.0

---

## 🔧 Correções Realizadas

### 1. **main.py** - Geração de Saída Corrigida

**Problema:** O script gerava apenas `output.json`, mas a workflow esperava `RESULTADO_POST_DIARIO.md`  
**Solução:** 
- Agora o script gera AMBOS os arquivos
- `RESULTADO_POST_DIARIO.md` - Markdown formatado para Make.com
- `output.json` - JSON estruturado com todos os dados

**Arquivo:** `main.py` (143 linhas)  
**Commit:** 🔧 Fix: Generate RESULTADO_POST_DIARIO.md file and save both JSON and Markdown outputs

### 2. **Workflow GitHub Actions** - Verificação Melhorada

**Problema:** 
- Não verificava saída do script
- Webhook para Make.com podia falhar silenciosamente
- Não salvava artifacts

**Solução:**
- Step: "Verify output files" - Valida ambos os arquivos
- Step: "Notificar Make.com (Webhook)" - Melhorado com tratamento de erro
- Step: "Upload artifacts" - Salva os arquivos para download
- Workflow agora é FAIL FAST

**Arquivo:** `.github/workflows/auto-generate.yml` (107 linhas)  
**Commit:** 🔧 Fix: Corrigir workflow para verificação de saída e notificação Make.com melhorada

### 3. **Makefile** - Teste Local Automático

**Problema:** Não havia ferramenta para testar localmente  
**Solução:**
- `make test-local` - Teste COMPLETO SEM INTERRUPÃO
- `make install` - Instala dependências
- `make setup` - Configura ambiente
- `make check` - Verifica configuração
- `make clean` - Remove saídas

**Arquivo:** `Makefile` (118 linhas)  
**Commit:** ✨ Add Makefile for testing agents without interruption

---

## 🤖 Como Testar Localmente

### Pré-requisitos
- Python 3.10+
- pip3
- Chave API do Google Gemini

### Passo 1: Instalar dependências

```bash
make install
```

Ou manualmente:

```bash
pip3 install -r requirements.txt
```

### Passo 2: Configurar variáveis de ambiente

```bash
export GEMINI_API_KEY="sua-chave-de-api-aqui"

# (Opcional) Para testar webhook Make.com
export MAKE_WEBHOOK_URL="https://hook.make.com/..."
```

### Passo 3: Executar teste COMPLETO sem interrupção

```bash
make test-local
```

Este comando irá:

1. ✅ Verificar `GEMINI_API_KEY`
2. ✅ Criar `input.md` se não existir
3. ✅ Executar `python main.py` com tratamento de erro
4. ✅ Verificar geração de `output.json`
5. ✅ Verificar geração de `RESULTADO_POST_DIARIO.md`
6. ✅ Exibir amostra dos arquivos
7. ✅ Relatório final

### Outros comandos úteis

```bash
# Verificar configuração
make check

# Ver ajuda
make help

# Limpar outputs
make clean
```

---

## 📊 Arquivos de Saída Esperados

### output.json

```json
{
  "timestamp": "2026-02-20T02:00:00.123456",
  "autor": "Henry Otasowere",
  "blog": "<html>...conteúdo do blog...</html>",
  "facebook": "Post provocador com emoji #Fé",
  "curiosidade_biblica": "Curiosidade profunda sobre o tema...",
  "status": "pronto_para_publicar"
}
```

### RESULTADO_POST_DIARIO.md

```markdown
# Post Diário Gerado - 2026-02-20 02:00:00

## Autor
Henry Otasowere

## Facebook Post
```
Post provocador com emoji #Fé
```

## Blog
<html>...conteúdo do blog...</html>

## Curiosidade Bíblica
Curiosidade profunda sobre o tema...

## Status
pronto_para_publicar
```

---

## 📤 Integração com Make.com

### Configuração do Webhook

1. **GitHub Settings → Secrets and variables → Actions**
   - `GEMINI_API_KEY` ✅ (obrigatório)
   - `MAKE_WEBHOOK_URL` (opcional, para notificação)

2. **Make.com Webhook URL**
   - Criar novo Webhook no Make.com
   - URL do webhook será algo como: `https://hook.make.com/...`
   - Copiar e adicionar ao GitHub Secrets

3. **Payload enviado ao Make.com**

```json
{
  "repository": "Dba66369/livros-cristao-content",
  "ref": "refs/heads/main",
  "commit": "abc123def456...",
  "file": "RESULTADO_POST_DIARIO.md",
  "timestamp": "2026-02-20T02:00:00Z",
  "status": "success"
}
```

### Fluxo no Make.com

1. **Trigger:** Webhook do GitHub (quando push em input.md)
2. **Action:** Parse JSON
3. **Action:** Ler arquivo RESULTADO_POST_DIARIO.md
4. **Action:** Publicar em Facebook
5. **Action:** Publicar no blog
6. **Action:** Gravar curiosidade bíblica

---

## ✅ Checklist de Validação

Antes de fazer deploy, verifique:

- [ ] `make test-local` executa SEM erros
- [ ] `output.json` foi criado
- [ ] `RESULTADO_POST_DIARIO.md` foi criado
- [ ] Ambos os arquivos contêm dados válidos
- [ ] `GEMINI_API_KEY` está configurado no GitHub Secrets
- [ ] Workflow passa nos logs do GitHub Actions
- [ ] Webhook Make.com está configurado (se applicable)
- [ ] `input.md` tem conteúdo (tema para gerar)

---

## 🚀 Executando no GitHub Actions

### Automático (ao fazer push em input.md)

```bash
# 1. Editar input.md com novo tema
echo "Novo tema aqui" > input.md

# 2. Push para GitHub
git add input.md
git commit -m "Atualizar tema para geração"
git push

# 3. Workflow executa automaticamente
# Verifique em: GitHub → Actions → Auto-Generate Content
```

### Manual (workflow_dispatch)

No GitHub:
1. Vá para **Actions**
2. Clique em **Auto-Generate Content**
3. Clique em **Run workflow**
4. Selecione a branch **main**
5. Clique em **Run workflow**

---

## 🔕 Troubleshooting

### Erro: "GEMINI_API_KEY não está definida"

```bash
# Local
export GEMINI_API_KEY="sua-chave"
make test-local

# GitHub Actions
# Adicionar em Settings → Secrets and variables → Actions
```

### Erro: "RESULTADO_POST_DIARIO.md não encontrado"

- Verifique se `main.py` está correto
- Verifique se a API Gemini respondeu
- Execute `python main.py` manualmente para ver erro específico

### Erro: "Webhook Make.com falhou"

- Webhook é OPCIONAL - workflow continuará mesmo sem ele
- Verifique URL do webhook em Make.com
- Teste com curl: `curl -X POST $MAKE_WEBHOOK_URL -d {...}`

---

## 🌟 Próximos Passos

1. **Executar testes locais** com `make test-local`
2. **Fazer push em input.md** para disparar workflow
3. **Monitorar GitHub Actions** para sucesso
4. **Configurar Make.com** para publicação
5. **Validar conteúdo** em Facebook/Blog

---

**Última atualização:** 20 de Fevereiro de 2026  
**Autor:** Sistema de Automação  
**Status:** ✅ PRONTO PARA PRODUÇÃO
