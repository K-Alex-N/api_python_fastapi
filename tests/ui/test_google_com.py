# https://www.google.com/


import asyncio
from playwright.async_api import Playwright, async_playwright, expect


async def search_on_google(headless=True, slow_mo=0):
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=headless, slow_mo=slow_mo)
        page = await browser.new_page()

        # мб проставить аллюр метки --- "Открываем Google.com..."
        await page.goto("https://www.google.com")
        await page.wait_for_load_state("networkidle")  # Ждем, пока сеть не будет неактивна. зачем это?????

        # закрываем куки. А что если их нет????!!!
        await page.click('.QS5gu.sy4vM"]')

        # 4. Ввод текста в поле поиска
        # Используем селектор CSS, чтобы найти поле ввода по его атрибуту name="q"
        # APjFqb
        print("Ввожу запрос в поиск...")
        await page.fill('APjFqb', "youtube")
        # Или await page.get_by_label("Поиск").fill("Playwright Python example")

        # 5. Нажатие кнопки "Поиск Google"
        # Используем селектор CSS для кнопки или get_by_role для более надежного поиска по ARIA-роли
        print("Нажимаю кнопку поиска...")
        await page.click('input[name="btnK"]')  # Или await page.get_by_role("button", name="Поиск Google").click()

        # 6. Ожидание загрузки страницы результатов
        # Можно ждать конкретного элемента на странице результатов
        await page.wait_for_selector('#search')  # Ждем появления блока с результатами поиска
        print(f"Заголовок страницы результатов: {await page.title()}")

        # 7. Извлечение заголовков первых нескольких результатов поиска
        print("\nЗаголовки первых 5 результатов поиска:")
        # Ищем все элементы с классом 'LC20lb MBeuO DCoPu' (это заголовки результатов)
        # locator() возвращает Locator, который может найти несколько элементов
        # all_text_contents() извлекает текст из всех найденных элементов
        search_results_titles = await page.locator('h3').all_text_contents()
        for i, title in enumerate(search_results_titles[:5]):  # Берем первые 5
            print(f"{i + 1}. {title}")

        # 8. Закрытие браузера
        print("\nЗакрываю браузер.")
        await browser.close()


if __name__ == "__main__":
    asyncio.run(search_on_google(headless=False, slow_mo=500)) # задерживаем каждое действие на 500 мс