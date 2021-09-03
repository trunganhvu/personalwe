from mainapp.model.Category import Category
from mainapp.model.CategoryPost import CategoryPost
from mainapp.Common import DateTime
from datetime import datetime

def get_all_category_post():
    """
    Get all post
    """
    list_post = CategoryPost.objects.all().order_by('-category_post_id')
    return list_post

def get_all_post_by_category_id(id):
    """
    Get all post in category
    """
    list_post = CategoryPost.objects.filter(category_id=id).order_by('category_post_id')
    return list_post

def get_post_detail_by_id(id):
    """
    Get detail by id
    """
    post = CategoryPost.objects.get(pk=id)
    return post

def insert_category_post(post):
    """
    Insert category post
    """
    category = Category.objects.get(pk=post.category_id)
    category_post = CategoryPost(category_id=post.category_id,
                    category_post_title=post.category_post_title,
                    category_post_url=post.category_post_url,
                    category_post_content=post.category_post_content,
                    category_post_description=post.category_post_description,
                    category_post_image_name=post.category_post_image_name,
                    category_post_image=post.category_post_image,
                    display=post.display,
                    display_order=post.display_order,
                    created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    )
    category_post.save()
    return category_post

def update_category_post(post):
    """
    Update category post
    """
    category_post = CategoryPost.objects.get(pk=post.category_post_id)
    category_post.category_id=post.category_id
    category_post.category_post_title=post.category_post_title
    category_post.category_post_url=post.category_post_url
    category_post.category_post_content=post.category_post_content
    category_post.category_post_description=post.category_post_description
    category_post.category_post_image_name=post.category_post_image_name
    category_post.category_post_image=post.category_post_image
    category_post.display=post.display
    category_post.display_order=post.display_order
    category_post.save()
    return category_post