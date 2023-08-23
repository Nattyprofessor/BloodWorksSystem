import base64
import datetime
import json
import uuid

import requests
from django.contrib.auth.models import User, Group
import random

import config

from jinja2 import Environment, FileSystemLoader

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

def generate_donations_report(report_type, template_id, payload):
    current_date = datetime.datetime.now().strftime("%d-%m-%Y")

    environment = Environment(loader=FileSystemLoader("static/pdf_templates/"))
    template = environment.get_template(template_id)

    filename = "id.html"
    content = template.render(station_name=payload['station_name'],
                              station_id=payload['station_id'],
                              volunteer_id=payload['volunteer_id'],
                              document_number=payload['document_number'],
                              document_date=payload['document_date'],
                              donors=payload['donors']
                              )

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

        doc_id = uuid.uuid4()
        filename = f"static/reports/{report_type}-reports/{payload['volunteer_id']}-report-{current_date}-{doc_id}.pdf"
        with open(filename, 'wb') as f:
            f.write(pdf_content)

        return {"status": "success", "doc_path": filename, 'id': doc_id}
    else:
        return "Error:", response.status_code

def generate_donors_report(report_type, template_id, payload):
    current_date = datetime.datetime.now().strftime("%d-%m-%Y")

    environment = Environment(loader=FileSystemLoader("static/pdf_templates/"))
    template = environment.get_template(template_id)

    filename = "id.html"
    content = template.render(station_name=payload['station_name'],
                              station_id=payload['station_id'],
                              volunteer_id=payload['volunteer_id'],
                              document_number=payload['document_number'],
                              document_date=payload['document_date'],
                              donors=payload['donors']
                              )

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

        doc_id = uuid.uuid4()
        filename = f"static/reports/{report_type}-reports/{payload['volunteer_id']}-report-{current_date}-{doc_id}.pdf"
        with open(filename, 'wb') as f:
            f.write(pdf_content)

        return {"status": "success", "doc_path": filename, 'id': doc_id}
    else:
        return "Error:", response.status_code

def generate_exam_report(report_type, template_id, payload, exam):
    current_date = datetime.datetime.now().strftime("%d-%m-%Y")

    environment = Environment(loader=FileSystemLoader("static/pdf_templates/"))
    template = environment.get_template(template_id)

    filename = "id.html"
    content = template.render(volunteer_id=payload['volunteer_id'],
                              name=payload['name'],
                              donor_id=payload['donor_id'],
                              age=payload['age'],
                              blood_group=payload['blood_group'],
                              station_name=payload['station_name'],
                              donation_date=payload['donation_date'],
                              exam=exam
                              )

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

        filename = f"static/reports/pre-{report_type}-reports/{payload['volunteer_id']}-report-{current_date}.pdf"
        with open(filename, 'wb') as f:
            f.write(pdf_content)

        return {"status": "success", "doc_path": filename}
    else:
        return "Error:", response.status_code
def generate_my_report(report_type, template_id, payload):
    current_date = datetime.datetime.now().strftime("%d-%m-%Y")

    environment = Environment(loader=FileSystemLoader("static/pdf_templates/"))
    template = environment.get_template(template_id)

    filename = "id.html"
    content = template.render(station_name=payload['station_name'],
                              station_id=payload['station_id'],
                              volunteer_id=payload['volunteer_id'],
                              document_number=payload['document_number'],
                              document_date=payload['document_date'],
                              donors=payload['donors']
                              )

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

        filename = f"static/reports/{report_type}-reports/{donor_id}-report-{payload['donation_date']}.pdf"
        with open(filename, 'wb') as f:
            f.write(pdf_content)

        return {"status": "success", "doc_path": filename}
    else:
        return "Error:", response.status_code
    endpoint = 'https://api.pdfmonkey.io/api/v1/documents'
    header = {f'Authorization': f'Bearer {config.pdf_monkey_key}', 'Content-Type': 'application/json'}
    data = {
        "document": {
            "document_template_id": f"{template_id}",
            "status": "pending",
            "payload": payload,
            "meta": {
                "_filename": f" "
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


def generate_doc_path(report_id, meta, report_type):
    report_url = get_document_url(report_id)
    document_response = requests.get(report_url)
    if document_response.status_code == 200:
        # convert the meta data to json format
        report_dict = json.loads(meta)

        print(f'This is the document path: {report_dict["_filename"]}')

        # obtain the filename from the report_dict  and write the document to media files
        open(f'static/reports/{report_type}/{report_dict["_filename"]}', 'wb').write(document_response.content)
        doc_path = f'reports/{report_type}/{report_dict["_filename"]}'

        return doc_path
    else:
        return ''


def create_donor_id_card():
    data = {
        "qr_code": {"code": "000036", "name": "Mango"},
        "donor": {"photo": "https://t3.ftcdn.net/jpg/02/43/58/76/360_F_243587666_DXAiHEZwwbQBDWQRmu2KtfP1qofmEmrH.jpg",
                  "name": "Anthony Kabuthu", "email": "kabuthu@gmail.com", "phone": "0745765678", "blood_group": "O+"}
    }

    environment = Environment(loader=FileSystemLoader("static/pdf_templates/"))
    template = environment.get_template("donor_id.html")

    filename = "id.html"
    content = template.render(qr_code = data.get("qr_code"), donor = data.get("donor"))

    with open(filename, mode="w", encoding="utf-8") as new_card:
        new_card.write(content)

    html = ""
    encoded_html = base64.b64encode(html.encode('utf-8')).decode('utf-8')

    headers = {
        'Authorization': 'Bearer ',
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
        with open('output.pdf', 'wb') as f:
            f.write(pdf_content)
    else:
        print("Error:", response.status_code)
        print(response.text)


def create_station_report(payload):
    current_date = datetime.datetime.now().strftime("%d-%m-%Y")

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

    print("Download x", data)
    if response.status_code == 200:
        return data['document']['download_url']
    else:
        return 'error'


def generate_donor_statement(donor_id, template_id, payload):

    environment = Environment(loader=FileSystemLoader("static/pdf_templates/"))
    template = environment.get_template(template_id)

    filename = "id.html"
    content = template.render(name=payload['name'],
                              age=payload['age'],
                              blood_group=payload['blood_group'],
                              units=payload['units'],
                              type=payload['type'],
                              donation_date=payload['donation_date'],
                              station_name=payload['station_name'],
                              )

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
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        filename = f"static/reports/donor-statements/{donor_id}-report-{current_date}.pdf"
        with open(filename, 'wb') as f:
            f.write(pdf_content)

        return { "status":"success", "doc_path": filename}
    else:
        return "Error:", response.status_code

        """
        #print(response.text)
    current_date = datetime.datetime.now().strftime("%d/%m/%Y")
    endpoint = 'https://api.pdfmonkey.io/api/v1/documents'
    header = {f'Authorization': f'Bearer {config.pdf_monkey_key}', 'Content-Type': 'application/json'}
    data = {
        "document": {
            "document_template_id": f"{template_id}",
            "status": "pending",
            "payload": payload,
            "meta": {
                "_filename": f"{donor_id}-report-{payload['donation_date']}.pdf"
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
    """