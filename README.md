<<<<<<< HEAD
# API Automation Testing with Pytest

This project demonstrates API automation testing using Pytest. It includes structured test cases, reusable utility functions, configurations, and reporting to facilitate efficient API testing.

## 📁 Project Structure
Api-automation/
│
├── conftest.py # Pytest fixtures and hooks
├── pytest.ini # Pytest configuration settings
├── requirements.txt # Python dependencies
├── tests/ # Directory containing test cases
│ ├── test_example.py # Sample test file
│ └── ...
├── utils/ # Utility functions for API requests and validations
│ ├── api_utils.py
│ └── ...
├── data/ # Test data files
│ ├── test_data.json
│ └── ...
└── reports/ # Directory for test reports

##  Getting Started

### Prerequisites

- Python 3.6+
- Install required dependencies:

```bash
pip install -r requirements.txt

Running Tests
pytest tests

Run all tests in the tests/ folder:
pytest -v tests

 License

This project is licensed under the MIT License.
=======

## API Automation Testing with Pytest

This project demonstrates API automation testing using Pytest. It includes structured test cases, reusable utility functions, configurations, and reporting to facilitate efficient API testing.



## Technologies Used

**Languages:** Python

- **Libraries:** os ,JsonPath, Requests, Pytest
- **Tools:** Git, GitHub, VSCode

## Installation
Install the dependencies and start the testing.

1. **Clone the repository:**

```bash
git clone  https://github.com/Phabi95/Api-automation.git
  cd Api-automation
```
2. **Create a virtual environment**   
```bash
python -m venv .venv
source .venv/bin/activate
```

3. **Install dependencies:** 

```bash
pip install -r requirements.txt
```

4. **Libraries**   
```bash
-pip install  pytest
-pip install requests
-pip install jsonpath
-pip install pytest-html
```


 **Quality Assurance:** 

This project includes automated tests to ensure code correctness and reliability. You can run them using:

```bash
pytest
```

 **Testing** 

 Run all tests and view detailed results with the following command  
```bash
pytest -s 
```

 **Testing** 

 Run all tests and view detailed results with the following command  
```bash
pytest -s 
```

## Viewing Test Reports

After generating the HTML report, you can view it by following these steps:

1. Open the project folder in your file explorer or IDE.  
2. Navigate to the `reports` folder.  
3. **Refresh** the folder if needed (right-click → Refresh).  
4. Right-click on `StationReport.html` and select **Open with → Default Browser**.  

This will open the full test report in your default web browser.


>>>>>>> dcb85b4 (update README)
