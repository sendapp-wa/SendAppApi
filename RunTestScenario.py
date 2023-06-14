"""
SendApp Automation Testing Framework
File: RunTestScenario.py

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


class RunTestScenario:
    def __init__(self, api_client, scenario):
        self.api_client = api_client
        self.scenario = scenario
        self.results = []

    def start(self):
        for step in self.scenario:
            # Execute the function and store the result
            result = step(self.api_client)
            self.results.append(result)

    def get_results(self):
        return self.results
