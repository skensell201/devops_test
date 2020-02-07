Сборка проекта:
python setup.py bdist_wheel

Запуск тестов:
pip install -r requirements/development.txt
pytest tests --cov package