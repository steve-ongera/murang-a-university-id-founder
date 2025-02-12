
from django.urls import path
from . import views


urlpatterns = [
    # Authentication URLs
    path('', views.home, name='homepage'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),

    # Lost ID Management
    path('lost-ids/', views.lost_id_list, name='lost_id_list'),
    path('lost-id/<int:pk>/', views.lost_id_detail, name='lost_id_detail'),
    path('lost-id/report/', views.report_lost_id, name='report_lost_id'),
    path('lost-id/<int:pk>/update/', views.update_lost_id, name='update_lost_id'),
    path('lost-id/<int:pk>/delete/', views.delete_lost_id, name='delete_lost_id'),

    # Found ID Management
    path('found-id/report/', views.report_found_id, name='report_found_id'),
    path('lost-id/<int:pk>/claim/', views.claim_id, name='claim_id'),

    # ID Replacement
    # path('replacement/apply/', views.replacement_apply, name='replacement_apply'),
    # path('replacement/<int:pk>/', views.replacement_detail, name='replacement_detail'),
    # path('replacement/list/', views.replacement_list, name='replacement_list'),

    # Payment
    # path('payment/<int:replacement_id>/initiate/', views.initiate_payment, name='initiate_payment'),
    # path('payment/callback/', views.payment_callback, name='payment_callback'),
    # path('payment/<int:pk>/status/', views.payment_status, name='payment_status'),

    # Category Views
    # path('category/<int:pk>/', views.category_detail, name='category_detail'),
    # path('category/list/', views.category_list, name='category_list'),

    # API endpoints for AJAX calls
    path('search-lost-ids/', views.search_lost_ids, name='search_lost_ids'),
    path('api/lost-ids/filter/', views.filter_lost_ids, name='filter_lost_ids'),

    # Profile Management
    # path('profile/', views.profile_view, name='profile'),
    # path('profile/edit/', views.edit_profile, name='edit_profile'),
    # path('profile/history/', views.user_history, name='user_history'),

    # Static Pages
    # path('about/', views.about_view, name='about'),
    # path('contact/', views.contact_view, name='contact'),
    # path('faq/', views.faq_view, name='faq'),
    # path('terms/', views.terms_view, name='terms'),
    # path('privacy/', views.privacy_view, name='privacy'),
]