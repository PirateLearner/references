from django.shortcuts import render
from reference.models import Reference

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import viewsets
from rest_framework import permissions
from utils import IsOwnerOrReadOnly, AnnotationIsOwnerOrReadOnly

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse

from django.contrib.auth.models import User
from blogging.models import BlogContent

from reference.serializers import *
# Create your views here.

'''
The Generic copy-paste type of views that are common to most of my code now
'''
@api_view(('GET',))
#If not set, the API root will assert for not having appropriate permissions.
@permission_classes((permissions.IsAuthenticatedOrReadOnly, ))
def api_root(request, format=None):
    return Response({
        'blogcontent': reverse('reference:blogcontent-list', request=request, format=format),
        'user': reverse('reference:user-list', request=request, format=format),
        'reference-list': reverse('reference:reference_list', request=request, format=format),
        'currentUser': reverse('reference:reference_detail', request=request, format=format),            
        })

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BlogContentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = BlogContent.objects.all()
    serializer_class = BlogContentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
       

class CurrentUserView(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def get(self, request, format=None):
        user_obj = self.request.user
        if(user_obj.id != None):
            serializer = UserSerializer(user_obj)
        else:
            serializer = AnonymousUserSerializer(user_obj)
            print(serializer.data)
             
        return Response(serializer.data)      

'''
The new 'relevant' views that drive this particular app
'''
class ReferenceList(APIView):
    def get(self, request, format=None):
        pass
    
    def post(self, request, format= None):
        pass
    
class ReferenceDetail(APIView):
    def get(self, request, pk, format=None):
        pass
    
    def put(self, request, pk, format=None):
        pass
    
    def delete(self, request, pk, format=None):
        pass

class BlogContentRefView(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def get(self, request, pk, format=None):
        #First, get the model instance of BlogContent
        obj = BlogContent.objects.get(pk=pk)
        #Then, get the content type instance
        content_type = ContentType.objects.get_for_model(obj)
        references = Reference.objects.filter(content_type= content_type.id, object_id=obj.id)
        print references
        
        #Now, put them into a serializer
        serializer = ReferenceSerializer(references, many=True)
        return Response(serializer.data)
         