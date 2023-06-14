# SendAppApi

This project provides a framework for testing SendApp SaaS API. It provides a Python-based API client for a range of bot-related operations, as well as a test scenario runner that can call API functions in sequence and log their results. The project is built on Python3.

## Installation

1. Ensure that Python3 is installed on your system. If not, you can download it from [here](https://www.python.org/downloads/).
2. Clone this repository to your local machine.
3. Navigate to the project directory and run `pip install -r requirements.txt` to install the necessary dependencies.

## Configuration

Before you can run the testing framework, you'll need to set the `admin_token` in the `main.py` script that were given to you by SendApp. 
This token will be used to authenticate some of your requests.

```python - main.py
admin_token = "your-admin-token-here"

```
Also change the server-adress-given-by-sendapp with the server DNS given to you
```python - api/botRoutes.py
server_url = 'https://server-adress-given-by-sendapp'
