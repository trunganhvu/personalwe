from mainapp.model.Header import Header

def get_path_header():
    header = Header.objects.filter(active=True).first()
    return header
