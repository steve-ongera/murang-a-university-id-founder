# MUT STORE

MUT STORE is a comprehensive system for managing student ID cards at your institution, including lost ID reporting, ID replacement applications, and payment processing.

![Screenshot ](https://github.com/steve-ongera/murang-a-university-id-founder/blob/main/screenshot/screencapture-127-0-0-1-8000-2025-02-12-16_23_44.png)


## Features

### Lost ID Management
- Report lost student IDs with detailed information
- Upload multiple ID images (front, back, and additional photos)
- Track lost ID status (Pending, Found, Claimed)
- Record finder information and location details
- Support for both School of Computing (SC) and Education (ED) registration numbers

### ID Replacement System
- Submit ID replacement applications
- Upload police abstract documents
- Track application status through multiple stages
- Integrated payment processing
- Automated fee calculation (default: KES 500.00)

### Payment Processing
- Support for multiple payment methods (M-Pesa and Bank Transfer)
- Transaction tracking and reference number generation
- Payment status monitoring (Pending, Confirmed, Failed)
- Secure payment record keeping

## System Requirements

- Django framework
- Python 3.x
- Support for image and file uploads
- Database system (compatible with Django ORM)

## Models Overview

### Category
Manages categorization of lost IDs with the following fields:
- `name`: Unique category name

### LostID
Handles lost ID reports with these fields:
- `student_name`: Full name of the student
- `registration_number`: Student registration number (Format: SCXXX/YYYY/YYYY or EDXXX/YYYY/YYYY)
- `course`: Student's course of study
- `category`: Optional category classification
- `date_reported`: Timestamp of report submission
- `last_seen_location`: Last known location of the ID
- `additional_details`: Any extra information
- Multiple image fields for ID documentation
- Status tracking (Pending, Found, Claimed)
- Finder information when applicable

### IDReplacement
Manages ID replacement applications:
- `student_name`: Full name of the student
- `registration_number`: Student registration number (Format: MU/YY/XXXXX)
- `phone_number`: Contact number (Format: +254XXXXXXXXX)
- `course`: Student's course of study
- `application_date`: Timestamp of application
- `reason`: Explanation for replacement
- `police_abstract`: Uploaded police abstract file
- Status tracking (Pending Payment, Paid, Processing, Ready for Collection, Collected)
- `amount`: Replacement fee (Default: KES 500.00)

### Payment
Handles payment processing:
- One-to-one relationship with IDReplacement
- `amount_paid`: Payment amount
- `payment_date`: Transaction timestamp
- `payment_method`: M-Pesa or Bank Transfer
- `transaction_reference`: Unique payment identifier
- `payment_status`: Transaction status tracking

## Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/mut-store.git
cd mut-store
```

2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure your database settings in `settings.py`

5. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create a superuser
```bash
python manage.py createsuperuser
```

7. Start the development server
```bash
python manage.py runserver
```

## Usage

1. Access the admin interface at `/admin` to manage all records
2. Use the provided forms to submit lost ID reports or replacement applications
3. Track application and payment status through the user interface
4. Process payments and update status as needed

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to your branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and queries, please contact the MUT STORE team at support@mutstore.com