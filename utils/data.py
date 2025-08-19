import os

# Данные заранее существующего пользователя для login/logout/создания объявления
EXISTING_EMAIL = os.environ.get("QA_DESK_EMAIL", "user@example.com")
EXISTING_PASSWORD = os.environ.get("QA_DESK_PASSWORD", "Secret1234")

# Данные для регистрации
NEW_USER_NAME = "User"
VALID_PASSWORD = "Secret1234"
