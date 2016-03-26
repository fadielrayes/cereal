
from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from main import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    #url(r'^cereal_detail/(?P<name>.+)/$', 'main.views.cereal_detail'),

    url(r'^cereal_list/$', 'main.views.cereal_list'),

    #url(r'^get_search/$', 'main.views.get_search'),

    #url(r'^get_post/$', 'main.views.get_post'),

  

] 
