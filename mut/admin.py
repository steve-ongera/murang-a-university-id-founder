from django.contrib import admin
from .models import Category, LostID, IDReplacement, Payment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(LostID)
class LostIDAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'registration_number', 'course', 'status', 'date_reported')
    list_filter = ('status', 'date_reported')
    search_fields = ('student_name', 'registration_number', 'course')
    readonly_fields = ('date_reported',)
    fieldsets = (
        ('Student Information', {
            'fields': ('student_name', 'registration_number', 'course', 'category')
        }),
        ('Lost ID Details', {
            'fields': ('last_seen_location', 'additional_details')
        }),
        ('Images', {
            'fields': ('id_front_image', 'id_back_image', 'additional_image1', 'additional_image2', 'additional_image3')
        }),
        ('Status', {
            'fields': ('status', 'found_location', 'found_date', 'finder_contact')
        }),
    )

@admin.register(IDReplacement)
class IDReplacementAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'registration_number', 'phone_number', 'status', 'application_date', 'amount')
    list_filter = ('status', 'application_date')
    search_fields = ('student_name', 'registration_number', 'phone_number')
    readonly_fields = ('application_date',)

    fieldsets = (
        ('Student Information', {
            'fields': ('student_name', 'registration_number', 'phone_number', 'course')
        }),
        ('Application Details', {
            'fields': ('reason', 'police_abstract')
        }),
        ('Status & Payment', {
            'fields': ('status', 'amount')
        }),
    )

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('replacement_application', 'amount_paid', 'payment_date', 'payment_method', 'payment_status')
    list_filter = ('payment_status', 'payment_method', 'payment_date')
    search_fields = ('replacement_application__student_name', 'transaction_reference')
    readonly_fields = ('payment_date',)

    fieldsets = (
        ('Payment Details', {
            'fields': ('replacement_application', 'amount_paid', 'payment_date', 'payment_method', 'transaction_reference', 'payment_status')
        }),
    )
