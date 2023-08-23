import base64
import os.path
import time
from datetime import datetime

import requests
from pytz import utc

import config
from django.core.mail import send_mail
from django.conf import settings

from jinja2 import Environment, FileSystemLoader


def notify_admin_about_new_donor(donor, name):
    subject = 'New Donor Registration'
    message = f'A new donor has registered.\n\nName: {name}\nEmail: {donor.email}\nPhone: {donor.mobile}'
    sender = settings.DEFAULT_FROM_EMAIL
    recipient = 'mwangisimone007@gmail.com'

    send_mail(subject, message, sender, [recipient])


def notify_volunteer_of_assignment(volunteer):
    subject = 'New Blood Drive Assignment'
    message = f'Hi there {volunteer.name}, you have been assigned to a new blood drive at {volunteer.blood_drive}. \n ' \
              f'Please carry your documents on the day before the blood drive'
    sender = settings.DEFAULT_FROM_EMAIL
    recipient = f'{volunteer.email}'

    send_mail(subject, message, sender, [recipient])


def check_my_account():
    endpoint = 'https://api.pdfmonkey.io/api/v1/current_user'
    header = {f'Authorization': 'Bearer {config.pdf_monkey_key}'}
    response = requests.get(endpoint, headers=header)
    data = response.json()
    print(data)


def generate_id_document(name, donor):
    data = {
        "qr_code": {"code": "000036", "name": "Mango"},
        "donor": {"photo": "https://t3.ftcdn.net/jpg/02/43/58/76/360_F_243587666_DXAiHEZwwbQBDWQRmu2KtfP1qofmEmrH.jpg",
                  "name": "Anthony Kabuthu", "email": "kabuthu@gmail.com", "phone": "0745765678", "blood_group": "O+"}
    }
    data2 = {
        "qr_code": {"code": f"{donor.donor_id}", "name": f"#{donor.user.username}"},
        "donor": {
            "photo": f"{donor.profile_pic.url}",
            "name": f"{name}", "email": f"{donor.email}", "phone": f"{donor.mobile}",
            "blood_group": f"{donor.bloodgroup}"}}

    environment = Environment(loader=FileSystemLoader("static/pdf_templates/"))
    template = environment.get_template("donor_id.html")

    filename = "id.html"
    content = template.render(qr_code=data2.get("qr_code"), donor=data2.get("donor"))

    with open(filename, mode="w", encoding="utf-8") as new_card:
        new_card.write(content)

    html = open("id.html", "r").read()

    encoded_html = base64.b64encode(html.encode('utf-8')).decode('utf-8')

    headers = {
        'Authorization': 'Bearer af11ffcd3c4b1212dada2d2b',
        'Content-Type': 'application/json'
    }

    data = {
        "page": {
            "pdf": {
                "printBackground": True
            },
            "setContent": {
                "html": encoded_html
            }
        }
    }

    url = 'https://api.doppio.sh/v1/render/pdf/direct'

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        pdf_content = response.content

        filename = f"static/reports/donor-cards/donor-card-{donor.donor_id}.pdf"
        with open(filename, 'wb') as f:
            f.write(pdf_content)

        return "success"
    else:
        return "Error:", response.status_code
        #print(response.text)
        """
    endpoint = 'https://api.pdfmonkey.io/api/v1/documents'
    header = {f'Authorization': f'Bearer {config.pdf_monkey_key}', 'Content-Type': 'application/json'}
    data = {
        "document": {
            "document_template_id": "BCBAD6C6-B324-47BC-A990-76457E7BEBFE",
            "status": "pending",
            "payload": {

            "meta": {
                "clientId": "ABC1234-DE",
                "_filename": f"donor-card-{donor.donor_id}.pdf"
            }
        }
    }
    response = requests.post(endpoint, headers=header, json=data)
    data = response.json()
    print(f' >>>>>>>>>>>>>>>{response.status_code}')
    #print(data)

    if response.status_code == 201:
        return data['document']['id']
    else:
        return 'error'
"""


def get_document_url(donor, card_id):

    path = f"static/reports/donor-cards/donor-card-{donor.donor_id}.pdf"
    if os.path.exists(path):
        return path
    else:
       return "None"

    """
    endpoint = f'https://api.pdfmonkey.io/api/v1/documents/{card_id}'
    header = {f'Authorization': f'Bearer {config.pdf_monkey_key}', 'Content-Type': 'application/json'}
    response = requests.get(endpoint, headers=header)
    data = response.json()

    # print(data)

    if response.status_code == 200:
        print('user has a card id')
        return data['document']['download_url']
    elif response.status_code == 404:
        print("user's id is not present or has been deleted")
        new_response = generate_id_document(donor.get_name, donor, "")

        if new_response != 'error':
            time.sleep(5)

            # Add the new card id to the donor model
            donor.donor_card_code = new_response
            donor.save(update_fields=['donor_card_code'])

            endpoint = f'https://api.pdfmonkey.io/api/v1/documents/{new_response}'
            header = {f'Authorization': f'Bearer {config.pdf_monkey_key}', 'Content-Type': 'application/json'}
            response = requests.get(endpoint, headers=header)
            data = response.json()

            # print(data)
            return data['document']['download_url']
        else:
            return 'error'
    else:
        return 'error'
    """

def find_most_recent_datetime(datetime_dict):
    if not datetime_dict:
        return None

    most_recent_key = None
    most_recent_datetime = utc.localize(datetime.min)

    for item in datetime_dict:
        if item['created_date'] > most_recent_datetime:
            most_recent_datetime = item['created_date']

    return str(most_recent_datetime)
