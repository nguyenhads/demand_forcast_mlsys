#!/bin/bash
rm -rf .venv
poetry run python -m venv .venv

# パッケージのインストール
source .venv/bin/activate
poetry run pip install --upgrade pip
poetry install
poetry run pre-commit install --install-hooks
poetry run pip install -r requirements-dev.txt
poetry run pip install -r requirements.txt


# 仮想環境をnotebookに反映させる(この処理は不要な場合もある)
poetry run python -m pip install ipykernel
poetry run python -m ipykernel install --user
poetry run ipython kernel install --user --name=juntendo_disease_diagnosis

# 日本語フォントの登録を反映する
poetry run python -c "import matplotlib, os; os.system('rm -r ' + matplotlib.get_cachedir())"
