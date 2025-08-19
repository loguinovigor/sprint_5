import pytest
from utils.urls import BASE_URL

@pytest.mark.logout
class TestLogout:
    def test_logout_placeholder(self, driver):
        driver.get(BASE_URL)
        actual = driver.current_url.startswith(BASE_URL)
        expected = True
        assert actual == expected
