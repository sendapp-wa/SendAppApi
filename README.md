# SendAppApi

This project provides a framework for testing SendApp SaaS API. It provides a Python-based API client for a range of bot-related operations, as well as a test scenario runner that can call API functions in sequence and log their results. The project is built on Python3.

## Installation

1. Ensure that Python3 is installed on your system. If not, you can download it from [here](https://www.python.org/downloads/).
2. Clone this repository to your local machine.
3. Navigate to the project directory and run `pip install -r requirements.txt` to install the necessary dependencies.

## Configuration

Before you can run the testing framework, you need to rename example.env to .env and update the parameters in it.

1. you'll need to set the `admin_token` in the `.env` were given to you by SendApp. 
This token will be used to authenticate some of your requests.

```python - .env
ADMIN_TOKEN='your-admin-token'
```

2. Change the server-adress-given-by-sendapp with the server DNS given to you
```python - .env
SERVER_URL='server-url'
```

3. Change the dummy numbers to have a valid list of numbers you want to sent the message to
```python - main.py
phone_numbers = ["972555555555", "972555555555"]  # Replace with actual numbers
```
## Usage
This framework provides the following API functions:

```python - main.py
create_bot(): Initiates a new bot session.
qr_interaction(): Interacts with the server to receive a QR code for WhatsApp Web session.
send_message(): Sends a message to a specific phone number.
close_bot(): Closes an existing bot session.
The main.py script defines a test scenario as a list of steps, where each step is a dictionary containing an 'action' (the API function to call) and 'args' (a dictionary of arguments for that function). A test scenario might look like this:
```
```
scenario = [
    {"action": "create_bot", "args": {}},
    {"action": "qr_interaction", "args": {"bot_token": ""}},
    {"action": "send_message", "args": {"bot_token": "", "phone": "", "message": "Hello, world!"}},
    {"action": "close_bot", "args": {"bot_token": "", "deleteBot": True}},
]
```

After defining your scenario, you can start the test runner with the following code:

```
runner = RunTestScenario(scenario)
runner.start()
results = runner.get_results()
``` 
The results object will be a list of dictionaries, where each dictionary contains the 'action', 'args', and 'result' (the API response) for each step.

## Contribution
As this code is licensed under MIT, you're free to use it as you please, including making and distributing closed source versions. However, any modification to the codebase should be done in a separate branch or in your own copy of the project. We ask that you do not directly modify the code in the main branch.

```
This README explains the basic functionality of your project, but it may be worth expanding on some points or adding additional sections as needed.
```