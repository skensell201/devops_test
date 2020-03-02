Сборка проекта:
```
python3.8 setup.py bdist_wheel
```

Запуск тестов:
```
pip3 install -r requirements/development.txt
pytest tests --cov package
```
