from django.urls import  path,re_path
from learn_api import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include
# urlpatterns = [
#     re_path(r'snippets/$',views.SnippetList.as_view()),
#     re_path(r'^snippets/(?P<pk>[0-9]+)/$',views.SnippetDetail.as_view()), #基于类的视图。需要加as_view()
#     re_path(r'^users/$',views.UserList.as_view()),
#     re_path(r'^user/(<?P<pk>[0-9]+)/$',views.UserDetail.as_view()),
#     re_path(r'^api-auth',include('rest_framework.urls',namespace='rest_framework')),
#     re_path(r'^',views.api_root),
#     re_path(r'^snippets/(?P<pk>[0-9]+)/highlight/$',views.SnippetHighlight.as_view()),
# ]
urlpatterns = [
    re_path(r'^$',views.api_root),
    re_path(r'^snippets/$',views.SnippetList.as_view(),name='snippet-list'),
    re_path(r'^snippets/(?P<pk>[0-9]+)/$',views.SnippetDetail.as_view(),name='snippet-detail'),
    re_path(r'snippets/(?P<pk>[0-9]+)/highlight/$',views.SnippetHighlight.as_view(),name="snippet-highlight"),
    re_path(r'^users/$',views.UserList.as_view(),name='user-list'),
    re_path(r'^user/(?P<pk>[0-9]+)/$',views.UserDetail.as_view(),name='user-detail'),

]


#给现有的URL后面添加一组format_suffix_patterns。

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    re_path(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework'))

]
