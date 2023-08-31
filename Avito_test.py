from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException


def first_test(ad_url):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(ad_url)
    try:
        driver.find_element(By.LINK_TEXT, "Вход и регистрация")
    except NoSuchElementException:
        print("Пользователь авторизован")
    try:
        favorites_button = driver.find_element(By.CLASS_NAME, "style-header-add-favorite-M7nA2")
        favorites_button.click()
    except NoSuchElementException:
        print("Отсутствует возможность добавить в Избранное")
    try:
        favorites_button2 = driver.find_element(By.CLASS_NAME, "index-counter-UxPCj")
        favorites_button2.click()
        try:
            href = driver.find_element(By.XPATH, f"//a[@href='{ad_url[20:]}']")
            if href:
                print("Добавленное в Избранное обьявление совпадает с требуемым")
        except NoSuchElementException:
            print('Обьявление добавленное в Избранное не совпадает с выбранным пользователем обьявлением')
    except NoSuchElementException:
        print('Отсутствует возможность перейти на страницу Избранное')
    driver.quit()


if __name__ == '__main__':
    add_url = "https://www.avito.ru/nikel/knigi_i_zhurnaly/domain-driven_design_distilled_vaughn_vernon_2639542363"
    first_test(add_url)
