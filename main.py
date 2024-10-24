from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

# Функция для запроса у пользователя первоначального запроса
def get_initial_query():
    query = input("Введите запрос для поиска на Википедии: ")
    return query

# Функция для выполнения поиска на Википедии
def search_wikipedia(query, browser):
    url = f"https://ru.wikipedia.org/wiki/{query}"
    browser.get(url)
    time.sleep(2)  # Ждем загрузки страницы

# Функция для вывода параграфов статьи
def scroll_through_paragraphs(browser):
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    for i, paragraph in enumerate(paragraphs):
        print(f"Параграф {i+1}:")
        print(paragraph.text)
        input("Нажмите Enter для перехода к следующему параграфу...")

# Функция для перехода на связанную страницу
def go_to_related_page(browser):
    links = browser.find_elements(By.TAG_NAME, "a")
    related_links = []

    for link in links:
        href = link.get_attribute("href")
        if href and "wikipedia.org/wiki/" in href:
            related_links.append(link)

    if related_links:
        random_link = random.choice(related_links)
        print(f"Переход на страницу: {random_link.get_attribute('href')}")
        browser.get(random_link.get_attribute("href"))
        time.sleep(2)
    else:
        print("Связанных статей не найдено.")

# Основная функция программы
def main():
    # Инициализация браузера
    browser = webdriver.Chrome()

    try:
        # Запрос пользователя
        query = get_initial_query()

        # Поиск статьи на Википедии
        search_wikipedia(query, browser)

        # Основной цикл программы
        while True:
            print("\nВыберите действие:")
            print("1. Листать параграфы статьи")
            print("2. Перейти на одну из связанных страниц")
            print("3. Выйти")

            choice = input("Введите номер действия: ")

            if choice == "1":
                scroll_through_paragraphs(browser)
            elif choice == "2":
                go_to_related_page(browser)
            elif choice == "3":
                print("Выход из программы.")
                break
            else:
                print("Некорректный ввод. Попробуйте снова.")

    finally:
        # Закрытие браузера
        browser.quit()

if __name__ == "__main__":
    main()
