import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures('driver')
class TestMain:

    def test_one(self, driver):
        """
        Verify click
        """
        driver.get("https://www.lambdatest.com/selenium-playground/")
        driver.maximize_window()
        driver.find_element(By.XPATH, "//a[normalize-space()='Input Form Submit']").click()
        result = driver.find_element(By.XPATH, "//input[@id='name']")
        driver.find_element(By.XPATH, "//button[normalize-space()='Submit']").click()
        res = result.get_attribute("validationMessage")
        assert "Please fill out this field." in res
        print(res)

    def test_two(self, driver):
        """
        Verify item submission
        : return: Pass
        """
        driver.get("https://www.lambdatest.com/selenium-playground/")
        driver.find_element(By.XPATH, "//a[normalize-space()='Drag & Drop Sliders']").click()
        slider = driver.find_element(By.XPATH, "//input[@value=15]").click()
        ActionChains(driver).drag_and_drop_by_offset(slider, 105, 0).perform()

    def test_three(self, driver):
        """
        Verify item submission
        : return: Pass
        """
        driver.get("https://www.lambdatest.com/selenium-playground/input-form-demo")
        driver.implicitly_wait(0)
        driver.find_element(By.XPATH, "//a[normalize-space()='Input Form Submit']").click()
        driver.find_element(By.ID, "name").send_keys("Srinivas")
        driver.find_element(By.ID, "inputEmail4").send_keys("Srinivasballa07@gmail.com")
        driver.find_element(By.ID, "inputPassword4").send_keys("Srinivasballa07")
        driver.find_element(By.CSS_SELECTOR, "#company").send_keys("Srinivasballa.com")
        driver.find_element(By.CSS_SELECTOR, "#websitename").send_keys("Srinivas.com")
        sel = Select(driver.find_element(By.XPATH, "//select[@name='country']"))
        sel.select_by_visible_text("United States")
        driver.find_element(By.CSS_SELECTOR, "#inputCity").send_keys("Hyderabad")
        driver.find_element(By.ID, "inputAddress1").send_keys("Hyderabad")
        driver.find_element(By.CSS_SELECTOR, "#inputAddress2").send_keys("Hyderabad")
        driver.find_element(By.ID, "inputState").send_keys("Telangana")
        driver.find_element(By.CSS_SELECTOR, "#inputZip").send_keys("500012")
        driver.find_element(By.XPATH, "//a[normalize-space()='Input Form Submit']").click()
        # successful = driver.find_element(By.XPATH, "//p[@class='success-msg hidden']").text
        # assert "Thanks for contacting us, we will get back to you shortly." in successful
        # print(successful)
