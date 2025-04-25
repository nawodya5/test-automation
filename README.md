Here's your updated `README.md` file for the **OrangeHRM Automation** project, with your GitHub account link included:

---

# OrangeHRM Automation

This project is a test automation framework for the OrangeHRM application using Selenium and Pytest.

GitHub Repository: [https://github.com/nawodya5/test-automation](https://github.com/nawodya5/test-automation)

## Prerequisites

Before running the tests, make sure you have the following installed:

1. Python 3.7 or higher  
2. Google Chrome browser  
3. ChromeDriver (automatically handled by `chromedriver-autoinstaller`)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/nawodya5/test-automation.git
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Edit the `Config.py` file and update these variables as needed:

- `BASE_URL`: URL of the OrangeHRM app  
- `USERNAME`: Login username  
- `PASSWORD`: Login password  
- `WAIT_TIME`: Max wait time for elements to load  
- `SLEEP_TIME`: Sleep duration between actions  

## Running the Tests

1. Run all test cases:
   ```bash
   pytest TestCases/TestOrangeHRM.py
   ```

2. Generate an HTML report in the `Reports` folder with a timestamp:
   ```bash
   pytest TestCases/TestOrangeHRM.py --html=Reports/report_$(date +%Y%m%d_%H%M%S).html
   ```

3. Run tests and suppress warnings:
   ```bash
   pytest TestCases/TestOrangeHRM.py --html=Reports/report_$(date +%Y%m%d_%H%M%S).html --disable-warnings
   ```

## Logs and Screenshots

- Logs are saved in the `Logs` folder with timestamped filenames  
- Screenshots are saved inside `Screenshots`, organized by test run  

## Project Structure

```
OrangeHRMAutomation/
├── Config.py                # Configuration settings
├── requirements.txt         # Required packages
├── conftest.py              # Pytest fixtures
├── Utilities/               # Helpers and logging tools
├── PageObjects/             # Page Object classes
├── TestCases/               # All test cases
├── Logs/                    # Generated log files
├── Reports/                 # HTML reports (generated)
├── Screenshots/            # Screenshots (auto-saved)
└── README.md                # Documentation
```

## Notes

- Make sure Chrome browser version matches with the driver used by `chromedriver-autoinstaller`
- Use `--disable-warnings` to hide warnings when running tests:
  ```bash
  pytest --disable-warnings
  ```

## License

This project is licensed under the MIT License.

---

Let me know if you also want a short intro about yourself added to the README.
