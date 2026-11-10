# ФИО: Кабачкова Мария Артемовна
# Дата: 2026-11-09
# Время: 18:23
# Описание: Подготавливает страницу, проверяет URL
# Я скопировала пример из раздела "Writing tests" и запустил его локально.
import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    
    print("before the test runs")

    # Перед каждым тестированием переходит на начальный URL адрес.
    page.goto("https://playwright.dev/")
    yield
    
    print("after the test runs")

def test_main_navigation(page: Page):
    # Утверждение успользует API
    expect(page).to_have_url("https://playwright.dev/")