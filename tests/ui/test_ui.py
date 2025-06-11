import asyncio
from playwright.async_api import Playwright, async_playwright, expect

headless = True
slow_mo = 0

VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"
INVALID_USERNAME = "asd"
INVALID_PASSWORD = "asd"


async def test_user_successfully_logs_in_with_valid_credentials():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=headless, slow_mo=slow_mo)
        page = await browser.new_page()



        # locators
        # pas --- #user-name    standard_user
        # pas --- #password     secret_sauce
        # but -  #login-button
        # если не верный логин или пароль    .error-message-container

        # мб проставить аллюр метки --- "Открываем Google.com..."
        await page.goto("https://www.saucedemo.com/")
        # await page.wait_for_load_state("networkidle")  # Ждем, пока сеть не будет неактивна. зачем это?????

        # закрываем куки. А что если их нет????!!!
        await page.click(".QS5gu.sy4vM")

        print("Ввожу запрос в поиск...")
        await page.fill('#APjFqb', "youtube")
        # Или await page.get_by_label("Поиск").fill("Playwright Python example")

        print("Нажимаю кнопку поиска...")
        await page.click('input[name="btnK"]')

        # что делать если появиться проверка что я робот

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


        # Лучше сделать LOGOUT на следуюшей странице


async def test_user_can_not_logs_in_with_invalid_username():
    pass


async def test_user_can_not_logs_in_with_invalid_password():
    pass


if __name__ == "__main__":
    headless = False
    slow_mo = 200
    asyncio.run(test_user_successfully_logs_in_with_valid_credentials(headless=headless, slow_mo=slow_mo))
