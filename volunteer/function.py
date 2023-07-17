import datetime

import requests
from django.contrib.auth.models import User, Group
import random

import config


def create_volunteer_account(volunteer):
    random_num = random.randrange(0, 100)
    # Create a new user
    user = User.objects.create_user(username=f'{volunteer.name}{random_num}',
                                    password=volunteer.volunteer_id)

    # Add the user to the "Volunteers" group
    group = Group.objects.get_or_create(name='VOLUNTEER')
    # user.groups.add(group)
    group[0].user_set.add(user)

    # Save the user
    user.save()
    print('user has been generated', user)

    return user


def generate_exam_id():
    current_time = datetime.datetime.now()
    random_num = random.randrange(0, 100)
    header = "EXAM"

    return f"EXAM-{random_num}-{current_time}"


def generate_my_report(report_type, template_id, data_array, volunteer_details, reports_count):
    current_date = datetime.datetime.now().strftime("%d/%m/%Y")

    endpoint = 'https://api.pdfmonkey.io/api/v1/documents'
    header = {f'Authorization': f'Bearer {config.pdf_monkey_key}', 'Content-Type': 'application/json'}
    data = {
        "document": {
            "document_template_id": f"{template_id}",
            "status": "pending",
            "payload": {
                "station_name": f"{volunteer_details.blood_drive.name}",
                "station_id": f"{volunteer_details.blood_drive.drive_id}",
                "volunteer_id": f"{volunteer_details.volunteer_id}",
                "document_number": f"000{reports_count}",
                "document_date": f"{current_date}",

                "donors": data_array
            }
            ,
            "meta": {
                "_filename": f"{report_type}-report-{volunteer_details.volunteer_id}.pdf"
            }
        }
    }
    print(data)
    response = requests.post(endpoint, headers=header, json=data)
    response_data = response.json()
    print(f' >>>>>>>>>>>>>>>{response.status_code}')
    print(response_data)

    if response.status_code == 201:
        return response_data
    else:
        return 'error'


def create_station_report(payload):
    current_date = datetime.datetime.now().strftime("%d/%m/%Y")

    endpoint = 'https://api.pdfmonkey.io/api/v1/documents'
    header = {f'Authorization': f'Bearer {config.pdf_monkey_key}', 'Content-Type': 'application/json'}
    data = {
        "document": {
            "document_template_id": "5AFF8357-2037-45C9-8B35-8A5B06CCD261",
            "status": "pending",
            "payload": payload,
            "meta": {
                "_filename": f"station-report-{payload['station_id']}-{current_date}.pdf"
            }
        }
    }
    print(data)
    response = requests.post(endpoint, headers=header, json=data)
    response_data = response.json()
    print(f' >>>>>>>>>>>>>>>{response.status_code}')
    print(response_data)

    if response.status_code == 201:
        return response_data
    else:
        return 'error'


def check_station_time():
    start = datetime.time(17, 30, 0)
    end = datetime.time(00, 55, 0)
    current = datetime.datetime.now().time()
    print(current)

    return start <= current <= end


def get_document_url(report_id):
    endpoint = f'https://api.pdfmonkey.io/api/v1/documents/{report_id}'
    header = {f'Authorization': f'Bearer {config.pdf_monkey_key}', 'Content-Type': 'application/json'}
    response = requests.get(endpoint, headers=header)
    data = response.json()

    print("Download x",data)
    if response.status_code == 200:
        return data['document']['download_url']
    else:
        return 'error'
