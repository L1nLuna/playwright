# ФИО: Кабачкова Мария Артемовна
# Дата: 2026-11-11
# Время: 15:01
# Описание: Подготавливает страницу, проверяет URL
# Я скопировала пример из раздела "Writing tests" и запустил его локально.
from playwright.sync_api import Page, BrowserContext
from pytest_playwright.pytest_playwright import CreateContextCallback

def test_foo(page: Page, new_context: CreateContextCallback) -> None:
    page.goto("https://example.com")
    context = new_context()
    page2 = context.new_page()
    # page and page2 are in different contexts