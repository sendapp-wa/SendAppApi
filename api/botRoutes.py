"""
SendApp Automation Testing Framework
File: botRoutes.py

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

import requests
import json
import time

from matplotlib import pyplot as plt
import qrcode
import os

server_url = os.getenv("SERVER_URL")

# Get show QR flag
show_qr = os.getenv("SHOW_QR_IN_POPUP")
show_qr = show_qr.lower() in ['true', '1', 't', 'y', 'yes']

class BotRoutesAPI:
    BASE_URL = server_url + '/api/v1'  # Update this as needed

    def __init__(self, token):
        self.headers = {'Authorization': f'{token}'}

    def create_bot(self):
        url = f"{self.BASE_URL}/createBot"
        response = requests.post(url, headers=self.headers)
        return response.json()

    def qr_interaction(self, bot_token):
        url = f"{self.BASE_URL}/qrInteraction"
        payload = {'token': bot_token}

        while True:
            response = requests.post(url, json=payload)
            result = response.json()

            status = result.get('status')
            print(json.dumps(result, indent=4))

            if status == 'ready':
                print("Successfully connected to number: " + result['connected_number'])
                plt.close()
                break
            elif status == 'not ready':
                # Check if qr_code is available in response
                if 'qr_code' in result and result['qr_code']:
                    if show_qr:
                        qr_code_str = result['qr_code']
                        img = qrcode.make(qr_code_str)
                        plt.clf()  # clear the figure for next iteration
                        plt.imshow(img)
                        plt.show(block=False)
                        plt.pause(0.1)  # pause a bit so that the plot gets updated

            else:
                print("Error:", result.get('error'))
                break
            time.sleep(5)
        return result

    def send_message(self, bot_token, phone_numbers, message, file_url=None):
        url = f"{self.BASE_URL}/sendMessage"
        responses = []
        for phone in phone_numbers:
            data = {
                "token": bot_token,
                "phone": phone,
                "message": message,
                "fileUrl": file_url  # This can be None, as per the API schema
            }

            responses.append(requests.post(url, json=data).json())
            time.sleep(2)
        return responses

    def close_bot(self, bot_token, delete_bot):
        url = f"{self.BASE_URL}/closeBot"

        data = {
            "token": bot_token,
            "deleteBot": delete_bot
        }
        time.sleep(5)
        response = requests.post(url, headers=self.headers, json=data)
        return response.json()
