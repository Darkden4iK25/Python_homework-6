from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Открываем браузер
driver = webdriver.Chrome()

try:
    # Переходим на страницу
    driver.get("https://uitestingplayground.com/textinput")
    print("Страница загружена")

    # Увеличиваем таймаут до 15 секунд
    wait = WebDriverWait(driver, 15)

    # Диагностический блок: выводим информацию о всех полях ввода на странице
    all_inputs = driver.find_elements(By.TAG_NAME, "input")
    print(f"Найдено полей ввода на странице: {len(all_inputs)}")

    for i, inp in enumerate(all_inputs):
        print(f"Поле ввода {i+1}: type='{inp.get_attribute('type')}', name='{inp.get_attribute('name')}', id='{inp.get_attribute('id')}', placeholder='{inp.get_attribute('placeholder')}'")

    # Пробуем найти поле ввода разными способами
    input_field = None

    # Способ 1: ищем по placeholder (наиболее вероятный рабочий вариант)
    try:
        input_field = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Enter button name']"))
        )
        print("Поле ввода найдено по placeholder")
    except Exception as e:
        print(f"Не удалось найти по placeholder: {e}")

    # Способ 2: ищем по классу
    if input_field is None:
        try:
            input_field = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".form-control"))
            )
            print("Поле ввода найдено по CSS-классу .form-control")
        except Exception as e:
            print(f"Не удалось найти по классу .form-control: {e}")

    # Способ 3: ищем по типу input
    if input_field is None:
        try:
            input_field = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='text']"))
            )
            print("Поле ввода найдено по типу input[type='text']")
        except Exception as e:
            print(f"Не удалось найти по типу input: {e}")

    # Если ни один способ не сработал
    if input_field is None:
        raise Exception("Не удалось найти поле ввода ни одним из способов")

    # Вводим текст в найденное поле
    input_field.send_keys("SkyPro")
    print("Текст 'SkyPro' введён в поле ввода")

    # Находим и кликаем на синюю кнопку
    button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#updatingButton"))
    )
    button.click()
    print("Синяя кнопка нажата")

    # Ждём обновления текста кнопки
    updated_button = wait.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#updatingButton"), "SkyPro")
    )

    # Получаем текст кнопки и выводим в консоль
    button_text = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
    print(f"Текст кнопки: {button_text}")

finally:
    # Закрываем браузер
    driver.quit()
