# 🚀 Guia: Make.com Webhook + GitHub + WordPress + Facebook

## FLUXO COMPLETO
```
Você edita input.md
        ↑
Faz git push
        ↑
GitHub Actions executa main.py
        ↑
Gera output.json
        ↑
Webhook GitHub envia para Make.com
        ↑
Make.com lê output.json
        ↑
Envia para Facebook + WordPress
```

## PASSO A PASSO NO MAKE.COM

### 1. Criar Scenario
1. Acesse: https://www.make.com/
2. Clique em "Create a New Scenario"
3. Escolha um nome: "Leitura Profética Automation"
4. Clique em "Create"

### 2. Adicionar Webhook (Trigger)
1. Clique em "Add module"
2. Procure por: "Webhooks"
3. Selecione: "Custom Webhook"
4. Clique em "Add"
5. **IMPORTANTE**: Copie a URL do webhook (começa com https://hook.make.com/...)

### 3. Testar o Webhook
1. Clique em "Determine data structure"
2. Deixe vazio por enquanto
3. Volte ao GitHub Settings e adicione webhook com essa URL
4. Faça um push à branch main para disparar o webhook

### 4. Adicionar Módulo: HTTP Request (ler output.json)
1. Clique em "+" para adicionar novo módulo
2. Procure: "HTTP"
3. Selecione: "Make an HTTP request"
4. Configure:
   - URL: `https://raw.githubusercontent.com/Dba66369/livros-cristao-content/main/output.json`
   - Method: GET
   - Response type: JSON
5. Clique em "OK"

### 5. Adicionar Módulo: Facebook Pages
1. Clique em "+"
2. Procure: "Facebook"
3. Selecione: "Create a Post"
4. Configure:
   - Connection: (Conecte sua página Facebook)
   - Page ID: (selecione sua página)
   - Message: Mapeie para `body.facebook` (do HTTP Request anterior)
5. Clique em "OK"

### 6. Adicionar Módulo: WordPress
1. Clique em "+"
2. Procure: "WordPress"
3. Selecione: "Create a Post"
4. Configure:
   - Connection: (Configure acesso ao seu WordPress)
   - Site: (selecione seu blog)
   - Title: `[Leitura Profética] Novo Conteúdo`
   - Content: Mapeie para `body.blog` (do HTTP Request)
   - Status: Publish
5. Clique em "OK"

### 7. (Opcional) Adicionar Módulo: Email Notification
1. Clique em "+"
2. Procure: "Gmail" (ou seu email)
3. Selecione: "Send an Email"
4. Configure:
   - To: seu@email.com
   - Subject: "[Bot] Novo conteúdo gerado!"
   - Content: Mapeie variáveis do output.json
5. Clique em "OK"

### 8. Salvar Scenario
1. Clique em "Save" (canto superior direito)
2. Dê um nome descritivo
3. Clique em "Save"

## ADICIONAR WEBHOOK NO GITHUB

### Voltar ao GitHub
1. Vá para: https://github.com/Dba66369/livros-cristao-content/settings/hooks
2. Clique em "Add webhook"
3. Cole a URL do Make.com webhook
4. Content type: `application/json`
5. Which events: "Let me select individual events"
6. Selecione: "Push events"
7. Ativo: ✓
8. Clique em "Add webhook"

## TESTAR O FLUXO COMPLETO

### Teste 1: Local
1. Edite o arquivo `input.md`
2. Digite um tema novo
3. Execute:
   ```bash
   git add input.md
   git commit -m "Novo tema para geração"
   git push origin main
   ```
4. Aguarde 2-3 minutos
5. Verifique:
   - GitHub Actions: Workflow "Auto-Generate Content" está rodando
   - output.json: Arquivo foi criado no repositório
   - Facebook: Post foi publicado na página
   - WordPress: Post foi criado no blog
   - Email: Notificação foi recebida

### Teste 2: Manual no Make.com
1. Abra o Scenario no Make.com
2. Clique em "Run once"
3. Verifique se os módulos executam com sucesso

## SOLUCIONANDO PROBLEMAS

### ❌ Webhook não está disparando
- Confirme a URL do webhook
- Vá para GitHub webhook settings e clique em "Edit" → "Test" para enviar um teste
- Verifique o log do webhook no Make.com

### ❌ output.json não está sendo lido
- Confirme que a URL HTTP no Make.com está correta
- Teste a URL em um navegador
- Verifique as credenciais do GitHub

### ❌ Post não está sendo publicado no Facebook
- Confirme que a conexão do Facebook está autorizada
- Verifique se a página tem permissão
- Vá para Facebook App e confirme as permissões

### ❌ Post não está sendo criado no WordPress
- Confirme credenciais de acesso
- Verifique se a conta tem permissão para criar posts
- Vá para WordPress settings → Application Passwords
- Regenere a senha se necessário

## ESTATEGIA DE ESCALA

### Adicionar mais plataformas
Você pode adicionar módulos adicionais no Make.com:
- LinkedIn
- Instagram
- Twitter
- Discord
- Telegram
- Slack
- Email Newsletter (Mailchimp)

Todos mapeados para os campos do `output.json`!

## AUTOMATIZAÇÕES AVANÇADAS

### Schedule
Se quiser gerar conteúdo automaticamente:
1. No Make.com, remova o webhook trigger
2. Adicione: "Scheduler"
3. Configure para: "Diário" ou "Semanal"
4. Configure GitHub para fazer push automaticamente do tema

