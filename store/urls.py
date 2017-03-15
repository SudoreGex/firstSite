from django.conf.urls import url
from . import views

app_name='store'

urlpatterns=[
	url(r'^$',views.store_page,name='store_page'),
	url(r'^(?P<bijou_name>\w+)/$',views.bijou_details,name='bijou_details'),
	url(r'^(?P<bijou_name>\w+)/favorite/$',views.bijou_favorite,name='bijou_favorite'),
]
