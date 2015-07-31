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

class BlogContentSerializer(serializers.ModelSerializer):
    #Tell BlogContent that it has a relation on Annotations    
    annotation = serializers.SerializerMethodField()
    #annotation = SerializeAnnotationsField()
    
    class Meta:
        model = BlogContent
        fields =('id', 'title', 'create_date', 'data', 'url_path', 
                 'author_id', 'published_flag', 'section', 'content_type',
                 'annotation',)
     
    def get_annotation(self, obj):
        content_object = ContentType.objects.get_for_model(obj)
        print "In BlogContentSerializer"
        print obj
        """
        annotations =  Annotation.objects.filter(content_type=content_object.id, object_id=obj.id)
        if len(annotations) is not 0:
            print AnnotationSerializer(annotations, many=True).data
            return (AnnotationSerializer(annotations, many=True).data)
        else:
            return None
        """

class ReferenceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Reference
        fields = ('id', 'url', 'content', 'type', 'parent')
        
    def create(self, validated_data):
        pass
    
    def update(self, instance, validated_data):
        pass