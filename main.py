"""
SendApp Automation Testing Framework
File: main.py

Copyright (c) 2023 SendApp. All Rights Reserved.

This program is free software: you can redistribute it and/or modify
it under the terms of the MIT License as published by
the Open Source Initiative.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
MIT License for more details.

You should have received a copy of the MIT License along with this program.
If not, see <https://opensource.org/licenses/MIT>.
"""

VERSION = "1.0.0"


from RunTestScenario import RunTestScenario
from api.botRoutes import BotRoutesAPI


def main():
    admin_token = "your-admin-token-here"  # Replace with your actual admin token
    # Create the API client
    api_client = BotRoutesAPI(admin_token)

    # Call create_bot and save the response
    create_bot_response = api_client.create_bot()
    if create_bot_response.get('error'):
        print(f"Failed to create bot: {create_bot_response.get('error')}")
        return
    bot_token = create_bot_response['token']

    # Define the list of numbers
    phone_numbers = ["972555555555", "972555555555"]  # Replace with actual numbers

    # Define the test scenario
    scenario = [
        lambda api: api.qr_interaction(bot_token),
        *[
            lambda api: api.send_message(bot_token, phone_numbers, "SendApp Saas API Test message")
        ],
        lambda api: api.close_bot(bot_token, True),
    ]

    # Run the test scenario
    test_runner = RunTestScenario(api_client, scenario)
    test_runner.start()

    # Print the results
    results = test_runner.get_results()
    for i, result in enumerate(results, 1):
        print(f"Step {i}: {result}")


if __name__ == "__main__":
    main()
