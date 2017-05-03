from django.conf.urls import url
from . import views

app_name='store'

urlpatterns=[
	url(r'^$',views.StoreView.as_view(),name='store_page'),
	url(r'^(?P<name>\w+)/$',views.DetailView.as_view(),name='bijou_details'),
	url(r'Bijou/Add/$',views.BijouCreat.as_view(),name='bijou_creat'),
	url(r'bijou/(?P<slug>\w+)/delete/$',views.BijouDelete.as_view(),name='bijou_delete'),
	url(r'Contact/1$',views.ContactUs,name='contact_us')


]
