.PHONY: check
check:
	python3 scripts/check_vendor.py
	python3 -m compileall -q nodes.py see-through/seethrough_modules see-through/seethrough_utils see-through/seethrough_annotators
