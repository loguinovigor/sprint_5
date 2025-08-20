# sprint_5 — UI автотесты (Selenium + Pytest)

Учебный проект автотестов. Реализация без Page Object Model.

## Структура
- `conftest.py` — фикстура для Selenium WebDriver
- `locators.py` — локаторы
- `tests/` — тесты (registration, login\logout, create_ad)

## Установка
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
