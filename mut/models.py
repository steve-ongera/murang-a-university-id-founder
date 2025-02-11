from django.db import models
from django.core.validators import RegexValidator
from decimal import Decimal

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"



class LostID(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('FOUND', 'Found'),
        ('CLAIMED', 'Claimed'),
    ]
    
    student_name = models.CharField(max_length=100)
    registration_number = models.CharField(
    max_length=20,
    validators=[
            RegexValidator(
                regex=r'^(SC|ED)\d{3}/\d{4}/\d{4}$',
                message='Registration number must be in format SCXXX/YYYY/YYYY or EDXXX/YYYY/YYYY (e.g., SC211/0530/2022 or ED511/0920/2022)'
            )
        ]
    )

    course = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='lost_ids',blank=True,null=True)
    date_reported = models.DateTimeField(auto_now_add=True)
    last_seen_location = models.CharField(max_length=200)
    additional_details = models.TextField(blank=True)

    # ID Images
    id_front_image = models.ImageField( upload_to='students_ids/front/',blank=True,null=True )     
    id_back_image = models.ImageField(upload_to='students_ids/back/',blank=True,null=True ) 
    additional_image1 = models.ImageField(upload_to='students_ids/additional/',blank=True,null=True)
    additional_image2 = models.ImageField(upload_to='students_ids/additional/',blank=True,null=True)
    additional_image3 = models.ImageField(upload_to='students_ids/additional/',blank=True,null=True)

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='PENDING'
    )
    found_location = models.CharField(max_length=200, blank=True, null=True)
    found_date = models.DateTimeField(blank=True, null=True)
    finder_contact = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return f"Lost ID - {self.registration_number} ({self.student_name})"

class IDReplacement(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending Payment'),
        ('PAID', 'Payment Received'),
        ('PROCESSING', 'Processing'),
        ('READY', 'Ready for Collection'),
        ('COLLECTED', 'Collected'),
    ]
    
    student_name = models.CharField(max_length=100)
    registration_number = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^MU/\d{2}/\d{5}$',
                message='Registration number must be in format MU/YY/XXXXX'
            )
        ]
    )
    phone_number = models.CharField(
        max_length=13,
        validators=[
            RegexValidator(
                regex=r'^\+254\d{9}$',
                message='Phone number must be in format +254XXXXXXXXX'
            )
        ]
    )
    course = models.CharField(max_length=100)
    application_date = models.DateTimeField(auto_now_add=True)
    reason = models.TextField()
    police_abstract = models.FileField(
        upload_to='abstracts/',
        help_text='Upload police abstract for lost ID'
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING'
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('500.00')
    )
    
    def __str__(self):
        return f"ID Replacement - {self.registration_number} ({self.student_name})"

class Payment(models.Model):
    PAYMENT_METHODS = [
        ('MPESA', 'M-Pesa'),
        ('BANK', 'Bank Transfer'),
    ]
    
    replacement_application = models.OneToOneField(IDReplacement, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(
        max_length=10,
        choices=PAYMENT_METHODS,
        default='MPESA'
    )
    transaction_reference = models.CharField(max_length=50, unique=True)
    payment_status = models.CharField(
        max_length=20,
        choices=[
            ('PENDING', 'Pending'),
            ('CONFIRMED', 'Confirmed'),
            ('FAILED', 'Failed'),
        ],
        default='PENDING'
    )
    
    def __str__(self):
        return f"Payment - {self.transaction_reference}"