from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


def test_text_visible(driver: Chrome):
    correct_text = "演唱會"

    driver.get("https://tixinn.com/index.php")
    xpath = "//ul[@class='center']/li[1]/a"
    question = driver.find_element(By.XPATH, xpath)
    print(question.text)

    assert question.text == correct_text
