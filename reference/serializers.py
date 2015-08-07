'''
Created on 24-Jul-2015

@author: anshul
'''
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField


from blogging.models import BlogContent
from django.contrib.auth.models import User

from django.contrib.contenttypes.models import ContentType

from reference.models import Reference

'''
The template copy-paste serializers
'''
class UserSerializer(serializers.ModelSerializer):
    
    gravatar = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'gravatar', 'url',)
        
    def get_gravatar(self, obj):
        return '#'
    
    def get_url(self, obj):
        return '#'
        
class AnonymousUserSerializer(serializers.Serializer):
    username = serializers.CharField();

class SerializeReadOnlyField(ReadOnlyField):
    
    def to_representation(self, value):
        if isinstance(value, BlogContent):
            return value.get_absolute_url()

'''
New/Modified code
'''
class BlogContentSerializer(serializers.ModelSerializer):
    references = serializers.PrimaryKeyRelatedField(many=True, 
                                                    queryset=Reference.objects.all())
    
    class Meta:
        model = BlogContent
        fields =('id', 'title', 'create_date', 'data', 'url_path', 
                 'author_id', 'published_flag', 'section', 'content_type',
                 'references',)
     
class ReferenceSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Reference
        fields = ('id', 'url', 'content', 'type', 'parent')
