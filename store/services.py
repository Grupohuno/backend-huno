from store.models import Price

def build_obj_list(queryset):
    obj_list =[]
    for product in queryset:
            product_obj = {
                "id": product.id,
                "name": product.name,
                "store": product.store_id.name,
                "category": product.category_id.name,
                "brand": product.brand,
                "size": product.size,
                "image": product.image_url,
                "redirect_page": product.page_url,
                "price": Price.objects.filter(product_id=product).last().price,
                "is_promotion": product.is_promotion,
            }
            obj_list.append(product_obj)
    return obj_list

def build_obj(product):
    product_obj = {
            "id": product.id,
            "name": product.name,
            "store": product.store_id.name,
            "category": product.category_id.name,
            "brand": product.brand,
            "size": product.size,
            "image": product.image_url,
            "redirect_page": product.page_url,
            "price": Price.objects.filter(product_id=product).last().price,
            "is_promotion": product.is_promotion,
        }
    return product_obj