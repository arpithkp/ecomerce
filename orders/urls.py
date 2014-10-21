from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ecommerce.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^/(?P<order_id>\d+)/$', 'orders.views.details_order'),
    url(r'', 'orders.views.list_order'),
)
