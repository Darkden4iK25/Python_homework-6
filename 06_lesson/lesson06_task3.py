from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Открываем браузер
driver = webdriver.Chrome()

try:
    # Переходим на страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    # Ждём загрузки всех картинок (4 картинки на странице)
    wait = WebDriverWait(driver, 15)
    images = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "img.img-fluid"))
    )

    # Проверяем, что загрузилось минимум 3 картинки
    if len(images) >= 3:
        # Получаем атрибут src у 3-й картинки (индекс 2)
        third_image_src = images[2].get_attribute("src")
        print(third_image_src)
    else:
        print("Недостаточно загруженных изображений")

finally:
    # Закрываем браузер
    driver.quit()
