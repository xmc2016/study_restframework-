from django.urls import  path,re_path
from learn_api import views

urlpatterns = [
    re_path(r'snippets/$',views.snippet_list),
    re_path(r'^snippets/(?P<pk>[0-9]+)/$',views.snippet_detail)

]