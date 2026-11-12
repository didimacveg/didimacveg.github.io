# Usage:  make cv     -> rebuilds both CV PDFs from cv/cv.en.json and cv/cv.es.json
#         make check  -> fails if an em dash or the old orange accent sneaks back in
#         make serve  -> preview the site at http://localhost:8000
VENV := .venv
PY   := $(VENV)/bin/python

.PHONY: cv check serve

$(PY):
	python3 -m venv $(VENV)
	$(PY) -m pip install --quiet --upgrade pip
	$(PY) -m pip install --quiet -r cv/requirements.txt

cv: $(PY)
	$(PY) cv/build.py

check:
	@! grep -n "—" index.html docs/LINKEDIN.md cv/*.json || (echo "em dash found" && exit 1)
	@! grep -n -i "f97316\|c2410c\|e8590c\|fdba74\|9a3412" index.html || (echo "orange accent found" && exit 1)
	@echo "ok: no em dashes, no orange"

serve:
	python3 -m http.server 8000
