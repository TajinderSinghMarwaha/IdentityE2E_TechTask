import os

from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from configuration.config import TestData
from pages.CarDetailsPage import CarDetailsPage
from pages.HomePage import HomePage
from Utilities import ExtractRegNumber
from Utilities import CreateActualOutputFile
from Utilities import Compare_Results
from Utilities import Generate_Result_File


@given(u'User launch the browser and Open the URL')
def launch_browser(context):
    if TestData.BROWSER == 'chrome':
        """Initializes the Chrome WebDriver."""
        options = Options()
        #options.add_argument("--headless")  # Run browser in headless mode for automation
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")

        try:
            serviceChrome = Service(TestData.CHROME_EXECUTABLE_PATH)
            context.driver = webdriver.Chrome(service=serviceChrome, options=options)
            context.driver.get(TestData.URL)
            context.homePage = HomePage(context.driver)
        except Exception as e:
            print(f"Error initializing ChromeDriver: {e}")

    else:
        raise ValueError('Browser is not supported')

@when(u'User searches the details of the cars whose registration numbers present in the input file')
def search_car_reg(context):
    # Folder path containing input files
    folder_path = os.path.join(os.getcwd(), "resources", "Test_Input_Files")
    # Iterate through each file in the folder
    context.homePage.click_accept_all_cookies()
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        all_reg_numbers = ExtractRegNumber.read_file(file_path, filename)
        lines_of_text = []
        try:
            for regNumb in all_reg_numbers:
                print(regNumb)
                context.homePage.enter_car_reg(regNumb)
                context.homePage.click_search()
                # returnText = context.homePage.sorry_is_displayed()
                # print('search_car_reg', returnText)
                # if(returnText):
                #     context.driver.refresh()
                #     context.homePage = HomePage(context.driver)
                #     continue
                # else:
                context.CarDetailsPage = CarDetailsPage(context.driver)
                context.CarDetailsPage.verify_car_details_section()
                registration_number = context.CarDetailsPage.get_regNumber()
                car_make = context.CarDetailsPage.get_make()
                car_model = context.CarDetailsPage.get_model()
                car_year = context.CarDetailsPage.get_year()
                line_of_text = f"{registration_number} ,{car_make}, {car_model}, {car_year}"
                lines_of_text.append(line_of_text.strip())
                context.CarDetailsPage.click_back()
                context.driver.refresh()
                context.homePage = HomePage(context.driver)
            CreateActualOutputFile.create_or_replace_file(filename, lines_of_text)
        except:
            context.driver.close()
            assert False, "Test is failed in searching the reg"

@then(u'User should see the displayed car details matches the expected details from the output file')
def validate_actual_output(context):
    pass_list = []
    fail_list = []

    # Folder path containing input files
    folder_path = os.path.join(os.getcwd(), "resources", "Test_Input_Files")
    folder_result = os.path.join(os.getcwd(), "results")
    # Iterate through each file in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        all_reg_numbers = ExtractRegNumber.read_file(file_path, filename)
        try:
            for regNumb in all_reg_numbers:
                regNumb = regNumb.replace(" ", "")
                results = Compare_Results.compare_fetch_reg_compare(filename, regNumb)
                if results == "Match":
                    pass_row = filename + ":" + regNumb + "- MATCH"
                    pass_list.append(pass_row)
                else:
                    fail_row = filename + ":" + regNumb + "- MISMATCH"
                    fail_list.append(fail_row)
        except:
            context.driver.close()
            assert False, "Test is failed in validating the reg details"
    pass_list.extend(fail_list)
    Generate_Result_File.create_or_replace_results(pass_list)
    if fail_list:
        print("fail_list:", fail_list)
        print("pass_list:", pass_list)
        assert False, "Test is failed in validating the reg details"
    else:
        print("pass_list:", pass_list)
        assert True, "Test validation pass."



@then(u'Close the browser')
def step_impl(context):
    context.driver.close()