# SimplyHired Website Testing

This repository contains automated tests for the SimplyHired website using Selenium and Pytest.

## Project Structure

SimplyHired_Website_Testing/
├── .venv/
├── pages/
│ ├── init.py
│ ├── BasePage.py
│ ├── pages_job_apply.py
│ ├── pages_job_search.py
│ ├── pages_signin.py
├── TestData/
│ ├── init.py
│ ├── Datasheet.xlsx
├── tests/
│ └── tests/
│ ├── init.py
│ ├── test_job_apply.py
│ ├── test_job_search.py
│ ├── test_Signin.py
├── tests_report/
│ ├── assets/
│ └── screenshots/
├── utils/
│ ├── init.py
│ ├── locators.py
│ ├── report_generator.py
│ ├── screenshot.py
├── conftest.py
├── jobs.csv
├── main.py
├── pytest.ini
└── run_test.py


### Directory Descriptions

- `pages/`: Contains the Page Object Model (POM) classes that abstract the interactions with web pages.
  - `BasePage.py`: Base class for all page objects.
  - `pages_job_apply.py`: Page object for the job application page.
  - `pages_job_search.py`: Page object for the job search page.
  - `pages_signin.py`: Page object for the sign-in page.

- `TestData/`: Contains test data files.
  - `Datasheet.xlsx`: Excel sheet with test data.

- `tests/`: Contains the test cases.
  - `test_job_apply.py`: Test cases for job application functionality.
  - `test_job_search.py`: Test cases for job search functionality.
  - `test_Signin.py`: Test cases for sign-in functionality.

- `tests_report/`: Contains test report files and screenshots of failed tests.
  - `assets/`: Assets for the report.
  - `screenshots/`: Screenshots of passed/failed test cases.

- `utils/`: Contains utility scripts.
  - `locators.py`: Contains locator definitions for the web elements.
  - `report_generator.py`: Script for generating test reports.
  - `screenshot.py`: Script for taking screenshots.

- `conftest.py`: Configuration file for Pytest.
- `jobs.csv`: CSV file with job data.
- `main.py`: Main script to run the tests.
- `pytest.ini`: Configuration file for Pytest.
- `run_test.py`: Script to run tests and generate reports.

## Prerequisites
Python 3.x
Selenium
Pytest

## Running the Tests

To run the tests, use the following command:

```bash
python run_test.py
