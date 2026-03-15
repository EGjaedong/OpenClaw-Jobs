# Makefile for OpenClaw Workspace

.PHONY: help update-rank commit push

help:
	@echo "🦞 OpenClaw Workspace Commands"
	@echo ""
	@echo "  make update-rank   - 更新 LLM 排行榜"
	@echo "  make commit        - 提交所有变更"
	@echo "  make push          - 推送到 GitHub main 分支"
	@echo "  make sync          - 拉取并推送 (同步)"
	@echo ""

update-rank:
	@echo "📊 更新 LLM 排行榜..."
	@bash scripts/update-llm-rank.sh

commit:
	@echo "💾 提交所有变更..."
	@git add -A
	@git commit -m "Update workspace $$(date +%Y-%m-%d)" || echo "⚠️  没有变更需要提交"

push:
	@echo "🚀 推送到 GitHub main 分支..."
	@git push origin main

sync:
	@echo "🔄 同步远程仓库..."
	@git pull origin main --rebase
	@git push origin main
