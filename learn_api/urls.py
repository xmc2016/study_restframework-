from django.urls import  path,re_path
from learn_api import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    re_path(r'snippets/$',views.SnippetList.as_view()),
    re_path(r'^snippets/(?P<pk>[0-9]+)/$',views.SnippetDetail.as_view())  #基于类的视图。需要加as_view()

]

#给现有的URL后面添加一组format_suffix_patterns。

urlpatterns = format_suffix_patterns(urlpatterns)


