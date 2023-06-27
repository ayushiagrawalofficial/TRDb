from django.views.static import serve
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view


@extend_schema(exclude=True)
@api_view(["GET"])
def media_locking_api(request, *args, **kwargs):
    """Media Locking API"""
    response = serve(request, kwargs["path"], document_root=kwargs["document_root"])
    return response
