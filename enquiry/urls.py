from django.conf.urls import url,patterns
from enquiry import views

urlpatterns = patterns('',
        url('^$',views.index,name="index"),
        url(r'^enquire/?$',views.store),
	url(r'^zohoverify/verifyforzoho.html/?$',views.verify),
        )
