BIN := bb
INSTALL_DIR := $(shell uv tool dir)/../bin

.PHONY: install uninstall dev

install:
	uv tool install . --force
	@echo "$(BIN) installed to $(INSTALL_DIR)"
	@echo "Ensure $(INSTALL_DIR) is in your PATH (run: uv tool update-shell)"

uninstall:
	uv tool uninstall bbcli

dev:
	uv sync --group dev
