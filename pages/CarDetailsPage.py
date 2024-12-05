from pages.InitPage import InitPage
from selenium.webdriver.common.by import By

class CarDetailsPage(InitPage):
    ELE_CarImage = (By.ID, "vehicleImage")
    BTN_BACK = (By.ID, "btn-back")
    TXT_car_RegNum = (By.XPATH, "(//div[@class=\"details-vrm ng-star-inserted\"])[2]")
    TXT_car_make = (By.XPATH, "(//div[@class=\"d-table-cell value\"])[8]")
    TXT_car_model = (By.XPATH, "(//div[@class=\"d-table-cell value\"])[9]")
    TXT_car_year = (By.XPATH, "(//div[@class=\"d-table-cell value\"])[10]")



    """Constructor of CarDetailsPage class"""

    def __init__(self, driver):
        super().__init__(driver)

    def verify_car_details_section(self):
        self.verify_element_displayed(self.ELE_CarImage)

    def click_back(self):
        self.click_element(self.BTN_BACK)

    def get_regNumber(self):
        regNumber = self.get_element_text(self.TXT_car_RegNum)
        print(regNumber)
        return regNumber

    def get_make(self):
        manufacture = self.get_element_text(self.TXT_car_make)
        return manufacture

    def get_model(self):
        model = self.get_element_text(self.TXT_car_model)
        return model

    def get_year(self):
        year = self.get_element_text(self.TXT_car_year)
        return year