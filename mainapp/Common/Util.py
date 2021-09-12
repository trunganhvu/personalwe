from django.core.files.storage import FileSystemStorage
import imghdr, os
from django.conf import settings


def save_image_to_media(image, image_name):
    """
    Save image to forder media
    """
    print('u1')
    # Set image name saved
    image_name_save = image_name + '.' + str(imghdr.what(image))
    # Dir save
    print('u2')

    fs = FileSystemStorage(location=settings.IMAGE_USER)
    # Save image
    print('u3')

    filename = fs.save(image_name_save, image)
    # Url dir save
    print('u4')
    uploaded_file_url = fs.url(filename)
    print('u5')
    full_path_image = settings.IMAGE_PATH_STATIC + uploaded_file_url
    return full_path_image

def delete_image_in_media(full_path_image):
    """
    Delete image
    """
    path1 = str(settings.BASE_DIR) + '/' + settings.APP_NAME1 + '/' + full_path_image
    path2 = str(settings.BASE_DIR) + '/' + full_path_image
    os.remove(path1)
    os.remove(path2)