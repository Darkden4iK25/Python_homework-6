from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Открываем браузер
driver = webdriver.Chrome()

try:
    # Переходим на страницу
    driver.get("https://uitestingplayground.com/ajax")
    print("Страница загружена")

    # Ждём, пока кнопка станет кликабельной (используем наиболее вероятный рабочий локатор)
    wait = WebDriverWait(driver, 10)
    button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-primary"))
    )
    print("Кнопка найдена по CSS-селектору '.btn-primary'")

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
