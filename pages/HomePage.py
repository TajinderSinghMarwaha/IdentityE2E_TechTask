from pages.InitPage import InitPage
from selenium.webdriver.common.by import By

class HomePage(InitPage):
    TXT_CarRegNumber = (By.ID, "vehicleReg")
    TXT_Mileage = (By.ID, "Mileage")
    BTN_ACCEPTALLCOOKIES = (By.XPATH, "//*[contains(text(), 'Accept all cookies')]")
    BTN_AcceptAll = (By.ID, "onetrust-accept-btn-handler")
    H1_Sorry = (By.XPATH, "//*[@class = \"text-focus ng-star-inserted\"]")


    BTN_Search = (By.ID, "btn-go")

    """Constructor of HomePage class"""

    def __init__(self, driver):
        super().__init__(driver)

    def enter_car_reg(self, regNum):
        self.click_element(self.TXT_CarRegNumber)
        self.clear_input_element(self.TXT_CarRegNumber)
        self.input_element(self.TXT_CarRegNumber, regNum)
        self.input_element(self.TXT_Mileage, "50000")

    def click_search(self):
        self.click_element(self.BTN_Search)

    def click_input_car_reg(self):
        self.click_element(self.TXT_CarRegNumber)

    def click_accept_all_cookies(self):
        self.click_element_if_displayed(self.BTN_AcceptAll)

    def sorry_is_displayed(self):
        returnTest = self.verify_element_displayed(self.H1_Sorry)
        return returnTest

    def accept_cookies(self):
        try:
            # Wait for and accept cookies popup if present
            self.click_element(self.BTN_ACCEPTALLCOOKIES)
        except Exception as e:
            print("No cookie button found or error handling cookies:", e)
