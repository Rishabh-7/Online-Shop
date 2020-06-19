from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]


# urlpatterns = [
#     # post views
#     #path(r'^$', views.post_list, name='post_list'),
#     path('', views.post_list, name='post_list'),
#     path('<int:year>/<int:month>/<int:day>/<slug:post>/',
#         views.post_detail,
#         name='post_detail'),
# ]