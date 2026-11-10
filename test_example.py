# ФИО: Кабачкова Мария Артемовна
# Дата: 2026-11-09
# Время: 18:07
# Описание: Проверяет, что открылась нужная страница
# Я скопировала пример из раздела "Writing tests" и запустил его локально.

import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Ожидает подстроку заголовка
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    # Тест ждет пока загрузится страница
    page.goto("https://playwright.dev/")

    # Нажатие запускает ссылку.
    page.get_by_role("link", name="Get started").click()

    # Ожидает заголовок с названием установки.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()

