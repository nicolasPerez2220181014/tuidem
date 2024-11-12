from rest_framework import viewsets

class BaseViewSet(viewsets.ModelViewSet):
    """
    Clase base genérica para reducir duplicidad en ViewSets.
    """
    lookup_field = 'id'
