from mainapp.model.Header import Header
from mainapp.Common import DateTime
from datetime import datetime

def get_path_header():
    """
    Get path header active
    """
    header = Header.objects.filter(active=True).first()
    return header

def update_header_image(header_name, header_path):
    """
    Update header
    """
    header = Header.objects.filter(active=True).first()
    header.image_default_name = header_name
    header.image_default_path = header_path
    header.save()

def insert_header_image(header_name, header_path):
    """
    Insert header
    """
    create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    header = Header(image_default_name=header_name, image_default_path=header_path, created_at=create_at, active=True)
    header.save()

def count_header_image():
    """
    Count header image
    """
    count_header_image = Header.objects.filter(active=True).count()
    return count_header_image