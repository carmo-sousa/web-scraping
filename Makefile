black:
	@echo "Format code with black"
	@black .

clean:
	@echo "Remove folder dist"
	@echo ""
	@rm -frv ./dist