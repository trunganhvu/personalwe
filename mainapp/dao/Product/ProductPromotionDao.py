from mainapp.model.ProductPromotion import ProductPromotion
from datetime import datetime

def get_all_promotion_in_product(product_id):
    """
    Get all promotion in product
    """
    list_promotion = ProductPromotion.objects.filter(product_id=product_id)
    return list_promotion

def get_all_promotion_active_in_product(product_id):
    """
    Get all promotion in product
    """
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    list_promotion = ProductPromotion.objects.filter(product_id=product_id,
                                                    product_promotion_start__gte=now,
                                                    product_promotion_end__lte=now)
    return list_promotion

def insert_promotion(product_promotion):
    """
    Insert promotion
    """
    p_promotion = ProductPromotion(product_id=product_promotion.product_id,
                                    discount=product_promotion.discount,
                                    product_promotion_start=product_promotion.product_promotion_start,
                                    product_promotion_end=product_promotion.product_promotion_end,
                                    event_id=product_promotion.event_id,
                                    created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    p_promotion.save()
    return p_promotion

def update_promotion(product_promotion):
    """
    Update promotion
    """
    p_promotion = ProductPromotion.objects.get(pk=product_promotion.product_promotion_id)
    p_promotion.discount = product_promotion.discount
    p_promotion.product_promotion_start = product_promotion.product_promotion_start
    p_promotion.product_promotion_end = product_promotion.product_promotion_end
    p_promotion.event_id = product_promotion.event_id
    p_promotion.save()
    return p_promotion

def delete_promotion(product_promotion_id):
    """
    Delete promotion by id
    """
    p_promotion = ProductPromotion.objects.get(pk=product_promotion_id)
    p_promotion.delete()
