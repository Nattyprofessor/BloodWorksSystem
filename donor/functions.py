import requests
import config
from django.core.mail import send_mail
from django.conf import settings


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


def generate_id_document(name, donor, code):
    endpoint = 'https://api.pdfmonkey.io/api/v1/documents'
    header = {f'Authorization': f'Bearer {config.pdf_monkey_key}', 'Content-Type': 'application/json'}
    data = {
        "document": {
            "document_template_id": "BCBAD6C6-B324-47BC-A990-76457E7BEBFE",
            "status": "pending",
            "payload": {
                "qr_code": {"code": f"{donor.donor_id}", "name": f"#{donor.donor_id}"},
                "donor": {
                    "photo": f"{donor.profile_pic.url}",
                    "name": f"{name}", "email": f"{donor.email}", "blood_group": f"{donor.bloodgroup}"}
            },
            "meta": {
                "clientId": "ABC1234-DE",
                "_filename": f"donor-card-{donor.id}.pdf"
            }
        }
    }
    response = requests.post(endpoint, headers=header, json=data)
    data = response.json()
    print(f' >>>>>>>>>>>>>>>{response.status_code}')
    print(data)

    if response.status_code == 201:
        return data['document']['id']
    else:
        return 'error'


def get_document_url(card_id):
    endpoint = f'https://api.pdfmonkey.io/api/v1/documents/{card_id}'
    header = {f'Authorization': f'Bearer {config.pdf_monkey_key}', 'Content-Type': 'application/json'}
    response = requests.get(endpoint, headers=header)
    data = response.json()

    if response.status_code == 200:
        return data['document']['download_url']
    else:
        return 'error'
