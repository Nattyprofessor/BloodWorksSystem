import requests

from config import *


def send_email_campaign(emails, form):
    endpoint = email_campaign_api

    header = {f'Content-Type': 'application/json'}
    data = {
        "emails": emails,
        "subject": form.data['subject'],
        "message": form.data['message']
    }
    response = requests.post(endpoint, headers=header, json=data)
    response_data = response.json()
    print(f' >>>>>>>>>>>>>>>{response.status_code}')
    print(f' <<<<<<<<<<<<<<<{response_data}')

    if response.status_code == 200:
        return response_data
    else:
        return 'error'
