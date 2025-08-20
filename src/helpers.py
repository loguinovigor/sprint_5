import os
import random

BASE_URL = os.getenv("BASE_URL", "https://qa-desk.stand.praktikum-services.ru")

def generate_email() -> str:
    return f"test{random.randint(1000, 9999)}@test.com"

def generate_password() -> str:
    return f"Test{random.randint(1000, 9999)}!"

def get_test_user():

    email = os.getenv("TEST_USER_EMAIL", "test_user@test.com")
    password = os.getenv("TEST_USER_PASSWORD", "Qwerty123!")
    return email, password
