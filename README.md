![Playwright Tests](https://github.com/Samiksha-Ghimire/python-playwright-automation/actions/workflows/playwright-tests.yml/badge.svg) 

# Playwright Automation Framework (Python)
This repository contains UI automation tests implemented using Playwright, Python, and Pytest.
The framework uses a basic Page Object Model structure and includes login scenarios and a complete checkout process for the SauceDemo application.


## Framework Overview
Key components include:

- Page Object classes for different application screens
- Test modules grouped by feature
- HTML test reporting
- Automatic screenshot capture for failed runs
- GitHub Actions workflow to run tests in CI



## Project Structure 

```

pages/ Page Object classes
tests/ Test cases by feature
utils/ Configuration values
reports/ HTML reports
screenshots/ Failure screenshots
.github/workflows/ CI pipeline configuration
conftest.py Pytest setup and screenshot hook
requirements.txt Dependencies 

```


## Test Coverage
### Login Tests

- Valid login
- Invalid username
- Invalid password
- Empty fields
- Locked-out user

### Checkout Flow

- Login
- Add item to cart
- Open cart
- Proceed to checkout
- Enter personal information
- Complete order
- Verify confirmation message


## Running Tests Locally
Install dependencies: 

```
pip install -r requirements.txt 
```

Install Playwright browsers: 
```
playwright install 
```

Run all tests: 
```
pytest 
```

Run with browser visible: 
```
pytest --headed 
```

Generate an HTML report: 
```
pytest --html=reports/report.html --self-contained-html 
```


## Continuous Integration (GitHub Actions)
A GitHub Actions workflow is included to run tests on every push.
The pipeline:
1.	Installs Python and project dependencies
2.	Installs Playwright browsers
3.	Runs the full test suite
4.	Uploads the HTML test report as an artifact

## Notes
The framework structure is simple, readable, and easy to extend with additional tests or flows.

