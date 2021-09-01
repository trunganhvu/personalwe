from mainapp.model.Header import Header
from mainapp.Common import DateTime
from datetime import datetime

def get_path_header():
    """
    Get path header active
    """
    header = Header.objects.filter(active=True).first()
    print('dao')
    return header

def insert_header_image(header_name, header_path):
    """
    Insert header
    """
    header = Header.objects.filter(active=True).first()
    header.image_default_name = header_name
    header.image_default_path = header_path
    # header.updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
    # print(DateTime.get_current_YmdHMS())
    # print(type(DateTime.get_current_YmdHMS()))
    header.save()