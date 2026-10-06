from django.http import JsonResponse
import json
from products.models import Product
from django.forms.models import model_to_dict


def api_home(request, *args, **kwargs):
    # body = request.body
    try:
        model_data = Product.objects.all().order_by("?").first()

        # data = {}
        # data["title"] = model_data.title
        # data["content"] = model_data.content
        data = model_to_dict(model_data, fields=["id", "title"])
    except:
        pass
    # data["content"] = request.content_type
    # data["headers"] = dict(request.headers)
    # data["params"] = dict(request.GET)

    return JsonResponse(data)
