from django.http import Http404
from django.core.exceptions import PermissionDenied


class IsAuthorMixin:
    def dispatch(self, request, *args, **kwargs):
        try:
            if self.get_object().author != request.user.profile:
                raise PermissionDenied()
            return super().dispatch(request, *args, *kwargs)
        except:
            raise PermissionDenied()
