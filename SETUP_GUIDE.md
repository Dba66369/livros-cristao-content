# 🚀 Guia Completo de Configuração

## PARTE 1: CONFIGURAR SECRETS NO GITHUB

### Passo 1: Obter API Key do Google Gemini
1. Acesse: https://ai.google.dev/
2. Clique em "Get API Key"
3. Crie um novo projeto
4. Copie a chave (começa com "AIza...")

### Passo 2: Adicionar Secret no GitHub
1. Vá para: `https://github.com/Dba66369/livros-cristao-content/settings/secrets/actions`
2. Clique em "New repository secret"
3. Nome: `GEMINI_API_KEY`
4. Cole a chave que copiou
5. Clique em "Add secret"

## PARTE 2: COMO USAR A AUTOMAÇÃO

### Método 1: Via Push
1. Edite o arquivo `input.md`
2. Digite o tema ou versículo
3. Faça `git push`
4. O GitHub Actions dispara automaticamente
5. Aguarde 2-3 minutos
6. O arquivo `output.json` é criado

### Método 2: Manualmente
1. Vá para: `https://github.com/Dba66369/livros-cristao-content/actions`
2. Clique em "Auto-Generate Content"
3. Clique em "Run workflow"
4. Selecione a branch "main"
5. Clique em "Run workflow"

## PARTE 3: INTEGRAÇÃO COM MAKE.COM

### Passo 1: Criar Webhook no GitHub
1. Vá para: `https://github.com/Dba66369/livros-cristao-content/settings/hooks`
2. Clique em "Add webhook"
3. Payload URL: (você recebe do Make.com)
4. Content type: application/json
5. Eventos: Push events
6. Ativo: ✓
7. Salve

### Passo 2: Configurar Make.com
1. Crie um novo Scenario
2. Clique em "Add module" → Webhooks
3. Selecione "Custom Webhook"
4. Copie a URL fornecida
5. Cole em GitHub (veja Passo 1 acima)

### Passo 3: Conectar Módılos do Make.com
1. **Módulo 1: HTTP Request** (para ler output.json)
   - URL: `https://raw.githubusercontent.com/Dba66369/livros-cristao-content/main/output.json`
   - Método: GET

2. **Módulo 2: Facebook Pages**
   - Configure sua página do Facebook
   - Mapeie para o campo: `facebook` do output.json

3. **Módulo 3: WordPress**
   - Configure seu blog WordPress
   - Mapeie para o campo: `blog` do output.json
   - Cria automaticamente post com HTML

4. **Módulo 4: Email/Notificação**
   - Configure para notificar quando pronto

## TROUBLESHOOTING

### ❌ Erro: "Arquivo input.md não encontrado"
- Certifique-se que o arquivo está na raiz do repositório
- Verifique se o nome é exato: `input.md`

### ❌ Erro: "GEMINI_API_KEY não configurada"
- Volte para PARTE 1
- Confirme que adicionou o secret corretamente
- Aguarde alguns minutos após adicionar

### ❌ output.json não foi criado
1. Vá para Actions
2. Clique no workflow mais recente
3. Veja o log para erros
4. Se houver erro na API, verifique a quota Google Gemini

## PERSONALIZANDO

Todos os valores estão no `main.py`:

- **AUTOR**: Henry Otasowere (linha 7)
- **TONO**: Profético, profundo, profissional (linha 8)
- **CONEXAO_TEOLOGICA**: Abraão, Elias, Jacó e Paulo (linha 9)
- **CHAMADA_ACAO**: Endereço da igreja (linha 10)
- **DISCLAIMER_AMAZON**: Texto do disclaimer (linha 11)

Basta editar e fazer push novamente!

## TESTES

1. Edite `input.md`
2. Faça push
3. Vá para Actions tab
4. Veja o workflow rodando em tempo real
5. Quando terminar, verifique `output.json` no repositório

