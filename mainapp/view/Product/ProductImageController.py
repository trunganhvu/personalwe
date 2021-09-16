from datetime import datetime
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from mainapp.Common import Util
from mainapp.service.Product import ProductService, ProductDetailService, ProductImageService
from mainapp.Common import ConstValiable
from mainapp.model.ProductImage import ProductImage
from mainapp.service.Product import ProductImageService

@login_required(login_url='/login/')
def insert_product_image_in_product(request, product_id):
    """
    Insert product image - need auth
    """
    try:
        if request.method == 'POST':
            # Get data in form request
            if 'product-image' in request.FILES:
                product_image = request.FILES['product-image']
            else:
                raise Exception('Exception product image')

            # Get base info product       
            product = ProductService.get_product_detail_by_id(product_id)

            if product is not None:
                image_name = 'product-' +  str(product.product_code)
                # Create image
                image = ProductImage(product_image_name=image_name,
                                    product_image_path=product_image,
                                    product_id_id=product_id)

                # Save image 
                ProductImageService.insert_product_image(image)

                return redirect('/products/' + str(product_id) + '/images/')
            else:
                raise Exception('Product not exist')
    except Exception as error:
        print(error)
        messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
        return redirect('/products/' + str(product_id))

@login_required(login_url='/login/')
def delete_product_image_by_image_id(request, product_id):
    """
    Delete product image by image id
    """
    try:
        if request.method == 'POST':
            # Get data in form request
            product_image_id = request.POST.get('product-image-id')

            # Get base info product       
            product_image = ProductImageService.get_product_image_by_image_id(product_image_id)

            if product_image is not None:
                # Save image 
                ProductImageService.delete_product_image_by_image_id(product_id, product_image_id)

                return redirect('/products/' + str(product_id) + '/images/')
            else:
                raise Exception('Product not exist')
    except Exception as error:
        print(error)
        messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
        return redirect('/products/' + str(product_id))