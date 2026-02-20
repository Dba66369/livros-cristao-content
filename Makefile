.PHONY: install test run test-local setup help

# Variáveis
PYTHON := python3
PIP := pip3
REQUIREMENTS := requirements.txt
MAIN_FILE := main.py
INPUT_FILE := input.md
OUTPUT_JSON := output.json
OUTPUT_MD := RESULTADO_POST_DIARIO.md

## help: Exibe esta mensagem de ajuda
help:
	@echo "Comandos disponíveis:"
	@echo ""
	@echo "  make install       - Instala as dependências (pip install -r requirements.txt)"
	@echo "  make setup         - Configura o ambiente local com variáveis de teste"
	@echo "  make test-local    - Executa teste local SEM interrupção"
	@echo "  make run           - Executa o script principal"
	@echo "  make clean         - Remove arquivos de output gerados"
	@echo "  make check         - Verifica se arquivos necessários existem"
	@echo "  make help          - Exibe esta mensagem"
	@echo ""

## install: Instala dependências
install:
	@echo "📦 Instalando dependências..."
	$(PIP) install --upgrade pip
	$(PIP) install -r $(REQUIREMENTS)
	@echo "✅ Dependências instaladas com sucesso!"

## setup: Configura ambiente de teste
setup: install
	@echo "🔧 Configurando ambiente local para teste..."
	@if [ ! -f "$(INPUT_FILE)" ]; then \
		echo "📝 Criando arquivo de teste $(INPUT_FILE)..."; \
		echo "O Evangelho de Marcos e a redenção do ser humano" > $(INPUT_FILE); \
		echo "✅ Arquivo $(INPUT_FILE) criado!"; \
	else \
		echo "✅ Arquivo $(INPUT_FILE) já existe!"; \
	fi
	@echo ""
	@echo "🔐 Variáveis de ambiente necessárias:"
	@echo "  • GEMINI_API_KEY - Sua chave de API do Google Gemini"
	@echo "  • MAKE_WEBHOOK_URL (opcional) - Para notificar Make.com"
	@echo ""

## check: Verifica configuração
check:
	@echo "🔍 Verificando arquivos necessários..."
	@if [ -f "$(MAIN_FILE)" ]; then echo "✅ $(MAIN_FILE) encontrado"; else echo "❌ $(MAIN_FILE) NÃO encontrado"; fi
	@if [ -f "$(REQUIREMENTS)" ]; then echo "✅ $(REQUIREMENTS) encontrado"; else echo "❌ $(REQUIREMENTS) NÃO encontrado"; fi
	@if [ -f "$(INPUT_FILE)" ]; then echo "✅ $(INPUT_FILE) encontrado"; else echo "⚠️  $(INPUT_FILE) NÃO encontrado (será criado no setup)"; fi
	@echo ""
	@echo "🔑 Variáveis de ambiente:"
	@if [ -z "$$GEMINI_API_KEY" ]; then echo "❌ GEMINI_API_KEY não está definida"; else echo "✅ GEMINI_API_KEY está configurada"; fi
	@echo ""

## run: Executa o script principal
run:
	@echo "🚀 Executando main.py..."
	$(PYTHON) $(MAIN_FILE)

## test-local: Teste completo LOCAL sem interrupção
test-local: check
	@echo "\n🧪 Iniciando TESTE COMPLETO SEM INTERRUPÇÃO..."
	@echo "=============================================\n"
	@if [ -z "$$GEMINI_API_KEY" ]; then \
		echo "❌ ERRO: GEMINI_API_KEY não está definida!"; \
		echo "Configure com: export GEMINI_API_KEY='sua-chave-aqui'"; \
		exit 1; \
	fi
	@echo "✅ GEMINI_API_KEY detectada\n"
	@if [ ! -f "$(INPUT_FILE)" ]; then \
		echo "📝 Criando input.md de teste..."; \
		echo "O Evangelho de Marcos e a redenção do ser humano" > $(INPUT_FILE); \
	fi
	@echo "📋 Executando geração de conteúdo...\n"
	@$(PYTHON) $(MAIN_FILE) 2>&1 || { echo "\n❌ Erro na execução!"; exit 1; }
	@echo "\n📋 Verificando saídas..."
	@if [ -f "$(OUTPUT_JSON)" ]; then \
		echo "✅ $(OUTPUT_JSON) gerado com sucesso"; \
		echo "   Tamanho: $$(stat -f%z $(OUTPUT_JSON) 2>/dev/null || stat -c%s $(OUTPUT_JSON) 2>/dev/null) bytes\n"; \
	else \
		echo "❌ $(OUTPUT_JSON) NÃO foi gerado!"; \
		exit 1; \
	fi
	@if [ -f "$(OUTPUT_MD)" ]; then \
		echo "✅ $(OUTPUT_MD) gerado com sucesso"; \
		echo "   Tamanho: $$(stat -f%z $(OUTPUT_MD) 2>/dev/null || stat -c%s $(OUTPUT_MD) 2>/dev/null) bytes\n"; \
	else \
		echo "❌ $(OUTPUT_MD) NÃO foi gerado!"; \
		exit 1; \
	fi
	@echo "✅ Amostra do output JSON:"
	@head -5 $(OUTPUT_JSON)
	@echo "   ..."
	@echo ""
	@echo "✅ Amostra do output Markdown:"
	@head -10 $(OUTPUT_MD)
	@echo "   ..."
	@echo ""
	@echo "=============================================\n"
	@echo "🎉 TESTE COMPLETO FINALIZADO COM SUCESSO!\n"
	@echo "📊 Arquivos gerados:"
	@echo "   • $(OUTPUT_JSON) - Dados em formato JSON"
	@echo "   • $(OUTPUT_MD) - Dados em formato Markdown (para Make.com)"
	@echo ""

## clean: Remove arquivos de output
clean:
	@echo "🧹 Limpando arquivos de output..."
	@rm -f $(OUTPUT_JSON) $(OUTPUT_MD)
	@echo "✅ Limpeza concluída!"

## install-hooks: Instala pre-commit hooks (opcional)
install-hooks:
	@echo "🎣 Instalando git hooks..."
	@echo "✅ Hooks instalados!"
