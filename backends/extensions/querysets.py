from ramos.mixins import ThreadSafeCreateMixin
from rest_framework.exceptions import NotFound

from backends.generic_querysets import QuerysetsInterface


class QuerySetsBackend(ThreadSafeCreateMixin, QuerysetsInterface):
    id = 'querysets'

    def get_or_404(self, Model, key, value):
        try:
            return Model.objects.get(**{key: value})
        except Model.DoesNotExist:
            raise NotFound('Recurso não encontrado')

    def create_resource(self, Model, **data):
        return Model.objects.create(**data)
