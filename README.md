## **Python Behave BDD Framework**

This is a BDD automation framework developed on Selenium and Python Behave.

## **Problem Statement**

Task Description:  
Write a test automation suite that does the following.
1.
Reads given input file: car_input.txt
2.
Extracts vehicle registration numbers based on pattern(s).
3.
Each number extracted from the input file is fed to any car valuation website for e.g.
webuyanycar  
(Perform vehicle details search car valuation page with random mileage details)
4.
Compare the output returned by the car valuation website with the given car_output.txt
5.
Highlight/fail the test for any mismatches. Showcase your skills so it’s easier to add more  
input files in the future. Utilise Python for the language with browser automation tools. Use
design patterns where appropriate.

## **Pre-requisite**

1. install Python
2. Config IDE with installed python version
3. install behave
4. Set behave.exe file location in path variable I found my behave.exe at below location C:\Users\userid\AppData\Roaming\Python\Python37\Scripts

## **Initial Setup**
pip install -r requirements.txt


## **Description**

Page Object Model is followed in this framework

**pages** folder contains the elements and corresponding actions of the pages

**features** folder contains **steps** folder which has all the test files and also the feature files.

**configuration** directory contains the configuration files

**drivers** directory contains the chrome and firefox driver for mac

**requirements.txt** file contains all the python packages needed to run this framework

**reports** directory contains the json files generated with allure reports

**Utilities** folder contains the general non-selenium re-usable functions 

project/
├── features/
│   ├── car_valuation.feature  # Feature file
│   ├── steps/
│   │   └── car_valuation_steps.py  # Step definitions
├── resources/
│   ├── Test_Input_Files/  # Input files
│   │   ├── car_input1.txt
│   │   ├── car_input2.txt
│   ├── Test_Output_Files/ # Output files
│       ├── car_output1.txt
│       ├── car_output2.txt


### **Commands to run the tests**

**To run the test without allure report** 
`behave features/car_valuation.feature`

**To run the test with allure report**
`behave -f allure_behave.formatter:AllureFormatter -o reports/ features/car_valuation.feature`

### **Output of the tests**

**Having MisMatches**
car_input V4.txt:KT17DLX- MATCH
car_input V4.txt:GU14FMO- MATCH
car_input V4.txt:AD58 VNF- MISMATCH
car_input V4.txt:GU14 OFM- MISMATCH
car_input V5.txt:GU14 OFM- MISMATCH

**Not having MisMatches**
car_input V4.txt:AD58VNF- MATCH
car_input V4.txt:GU14OFM- MATCH
car_input V4.txt:KT17DLX- MATCH
car_input V4.txt:GU14FMO- MATCH
car_input V5.txt:GU14OFM- MATCH