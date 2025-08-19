import random, string

def random_email(domain: str = "example.com") -> str:
    name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=12))
    return f"{name}@{domain}"
