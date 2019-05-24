from tastypie.resources import ModelResource
from tcapp.models import User
from tastypie.authorization import Authorization
class NoteResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'note'
