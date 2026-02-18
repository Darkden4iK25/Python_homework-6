from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Открываем браузер
driver = webdriver.Chrome()

try:
    # Переходим на страницу
    driver.get("https://uitestingplayground.com/ajax")
    print("Страница загружена")

    # Даём немного времени на первичную загрузку
    time.sleep(2)

    # Диагностический блок: выводим информацию о всех кнопках на странице
    all_buttons = driver.find_elements(By.TAG_NAME, "button")
    print(f"Найдено кнопок на странице: {len(all_buttons)}")

    for i, btn in enumerate(all_buttons):
        print(f"Кнопка {i+1}: текст='{btn.text}', class='{btn.get_attribute('class')}', id='{btn.get_attribute('id')}'")

    # Увеличиваем таймаут до 20 секунд для надёжности
    wait = WebDriverWait(driver, 20)

    # Пробуем найти кнопку разными способами
    button = None

    # Способ 1: ищем по классу (наиболее вероятный рабочий вариант)
    try:
        button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-primary"))
        )
        print("Кнопка найдена по CSS-селектору '.btn-primary'")
    except Exception as e:
        print(f"Не удалось найти по .btn-primary: {e}")

    # Способ 2: ищем по XPath с частичным совпадением текста
    if button is None:
        try:
            button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Trigger')]"))
            )
            print("Кнопка найдена по XPath с частичным текстом")
        except Exception as e:
            print(f"Не удалось найти по XPath: {e}")

    # Способ 3: ищем по полному тексту (если он точно известен)
    if button is None:
        try:
            button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Trigger AJAX Request']"))
            )
            print("Кнопка найдена по XPath с точным текстом")
        except Exception as e:
            print(f"Не удалось найти по точному тексту: {e}")

    # Если ни один способ не сработал — выводим отладочную информацию
    if button is None:
        print("Не удалось найти кнопку ни одним из способов!")
        print("Попробуйте вручную проверить структуру страницы через F12")
        raise Exception("Кнопка не найдена")

    # Кликаем на кнопку
    button.click()
    print("Кнопка успешно нажата!")

    # Ждём появления зелёной плашки с текстом
    green_alert = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-success"))
    )
    print("Зелёная плашка найдена")

    # Получаем текст из плашки и выводим в консоль
    text = green_alert.text
    print(f"Текст из зелёной плашки: {text}")

finally:
    # Закрываем браузер
    driver.quit()
