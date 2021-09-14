from mainapp.model.ProductImage import ProductImage
from datetime import datetime

def get_all_image_in_product(product_id):
    """
    Get all image in product
    """
    list_image = ProductImage.objects.filter(product_id=product_id)
    return list_image

def insert_image(product_image):
    """
    Insert image
    """
    p_image = ProductImage(product_image_name=product_image.product_image_name,
                            product_image_path=product_image.product_image_path,
                            product_id=product_image.product_id,
                            created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    p_image.save()
    return p_image

def update_image(product_image):
    """
    Update image
    """
    p_image = ProductImage.objects.get(pk=product_image.product_image_id)
    p_image.product_image_name=product_image.product_image_name
    p_image.product_image_path=product_image.product_image_path
    p_image.save()
    return p_image

def delete_image_by_id(product_image_id):
    """
    Delete image by id
    """
    p_image = ProductImage.objects.get(pk=product_image_id)
    p_image.delete()

def delete_all_product_image_by_product_id(product_id):
    """
    Delete product image by product id
    """
    p_image = ProductImage.objects.filter(product_id=product_id)
    p_image.delete()