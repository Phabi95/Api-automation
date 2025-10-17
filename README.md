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
