from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^article/$', 'article.views.Article', name='Article'),
     url(r'^$', 'signups.views.home', name='home'),
     url(r'^orders$', 'orders.views.order'),
     url(r'^customers', 'customers.views.customer'),
     url(r'^categories', 'categories.views.category'),
     url(r'^employees$', 'employees.views.employee'),
     url(r'^regions', 'regions.views.region'),
     url(r'^lists', 'lists.views.lists'),
     url(r'^addOrder', 'orders.views.addOrder'),
     url(r'^addCategory', 'categories.views.addCategory'),
     url(r'^addCustomer', 'customers.views.addCustomer'),
     url(r'^addEmployee', 'employees.views.addEmployee'),
     url(r'^addRegion', 'regions.views.addRegion'),
     url(r'^ordersManager', 'orders.views.ordersManager'),
     url(r'^ordersPerEmployee', 'orders.views.ordersPerEmployee'),
     url(r'^employeesHireDate', 'orders.views.employeesHireDate'),
     url(r'^ordersFreightTop', 'orders.views.ordersFreightTop'),
     url(r'^seafoodSuppliers', 'suppliers.views.seafoodSuppliers'),
     url(r'^year1998Products', 'products.views.year1998OrderProducts'),
     url(r'^atomic', 'regions.views.atomicEmployeeAndOrder'),


    # url(r'^blog/', include('blog.urls')),

     url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
