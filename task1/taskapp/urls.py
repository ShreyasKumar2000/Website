from . import views
from django.urls import path

urlpatterns = [

    path('',views.demo,name='demo'),
    # path('arithmetic/',views.arithmetic,name='arithmetic'),
    # path('arithmetic/operation/',views.operation1,name='operation'),
    # path('contact/',views.contact,name='contact'),
    # path('details/',views.details,name='details'),
    # path('endpage/',views.endpage,name='endpage')
]