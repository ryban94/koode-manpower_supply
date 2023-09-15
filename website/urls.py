from django.urls import path
from website import views



urlpatterns = [
        path('',views.home1,name="home1"),
        path('mainlog/',views.mainlog,name="mainlog"),
        path('loginclient/',views.loginclient,name="loginclient"),
        path('loginpartner/',views.loginpartner,name="loginpartner"),
        path('signupclient/',views.signupclient,name="signupclient"),
        path('signuppartner/',views.signuppartner,name="signuppartner"),
        path('add_partner/',views.add_partner,name="add_partner"),
        path('add_client/',views.add_client,name="add_client"),
        path('client_log/',views.client_log,name="client_log"),
        path('partner_log/',views.partner_log,name="partner_log"),
        path('partner_logout/',views.partner_logout,name="partner_logout"),
        path('client_logout/',views.client_logout,name="client_logout"),
        path('clienthome/',views.clienthome,name="clienthome"),
        path('demopage/',views.demopage,name="demopage"),
        path('postclient/',views.postclient,name="postclient"),
        path('save_post/',views.save_post,name="save_post"),
        path('view_post/',views.view_post,name="view_post"),
        path('edit_post/<int:dataid>/',views.edit_post,name="edit_post"),
        path('update_post/<int:postid>/', views.update_post, name="update_post"),
        path('delete_add/<int:dataid>/', views.delete_add, name="delete_add"),
        path('view_daily/<cat_name>', views.view_daily, name="view_daily"),
        path('view_perminent/<cat_name>', views.view_perminent, name="view_perminent"),
        path('view_contract/<cat_name>', views.view_contract, name="view_contract"),
        path('about/', views.about, name="about"),
        path('career/', views.career, name="career"),
        path('contactus/', views.contactus, name="contactus"),
        path('search_results/', views.search_results, name="search_results"),
        # path('invoicef/', views.invoicef, name="invoicef"),

    ]