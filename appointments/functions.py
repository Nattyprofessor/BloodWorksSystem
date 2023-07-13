import os


def handle_uploaded_file(drive_id, file):
    new_path = f'./static/hosted_blood_drives/{drive_id}'
    if not os.path.exists(new_path):
        os.mkdir(new_path)
    with open(new_path + '/' + file.name, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
