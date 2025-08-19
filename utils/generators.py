import random, string, time

def unique_email(domain="example.com", prefix="autotest"):
    # Надёжная генерация уникального email для регистрации
    salt = f"{int(time.time()*1000)}{random.randint(1000,9999)}"
    name = f"{prefix}.{salt}"
    return f"{name}@{domain}"
