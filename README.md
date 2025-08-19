# Sprint_5 — Selenium UI автотесты (QA Desk)

Проект с автотестами на **Selenium + Pytest** для сайта:
`https://qa-desk.stand.praktikum-services.ru/`

## Что внутри
- Page Object Model (`pages/`)
- Локаторы в отдельном модуле (`locators.py`)
- Явные ожидания, **без** `sleep()` и неявных ожиданий
- Генерация уникального email для каждого теста регистрации
- Тесты независимы и завершаются `assert` сравнением фактического и ожидаемого результатов
- Инстанс драйвера поднимается и закрывается в фикстуре `driver`

## Установка
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Запуск
Убедитесь, что установлен Google Chrome.
```bash
pytest -v
```

## Структура
```
Sprint_5/
  pages/
  tests/
  utils/
  locators.py
  conftest.py
  requirements.txt
  README.md
  .gitignore
```

## Переменные окружения (по желанию)
Для тестов логина/логаута и создания объявления используйте заранее существующего пользователя.
Можно передать данные через переменные окружения:
- `QA_DESK_EMAIL`
- `QA_DESK_PASSWORD`

Или задайте прямо в `utils/data.py` (не рекомендуется коммитить реальные данные).
