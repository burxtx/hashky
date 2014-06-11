from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('account.views',
    url(r'^accounts/$', 'account_page', name="account_page")
    url(r'^accounts/login/$', 'login_page', name="login_page"),
    url(r'^accounts/logout/$', 'logout_page', name="logout_page"),
    url(r'^register/$', 'register_page', name="register_page"),
    (r'^register/success/$', direct_to_template,
        { 'template': 'registration/register_success.html' }),
)