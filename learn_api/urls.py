from django.urls import  path,re_path
from learn_api import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    re_path(r'snippets/$',views.snippet_list),
    re_path(r'^snippets/(?P<pk>[0-9]+)/$',views.snippet_detail)

]

#给现有的URL后面添加一组format_suffix_patterns。

urlpatterns = format_suffix_patterns(urlpatterns)


