from mainapp.dao.Header import HeaderDao

def get_path_header():
    header = HeaderDao.get_path_header()
    context = {
        'name': header.image_default_name,
        'path': header.image_default_path
    }
    return context
