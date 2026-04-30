from django.db import models
from django.conf import settings

class Certificate(models.Model):

    CATEGORY_CHOICES = [
        ('Cloud','Cloud'),
        ('AI/ML','AI/ML'),
        ('Blockchain','Blockchain'),
        ('Programming','Programming'),
        ('Cybersecurity','Cybersecurity'),
        ('Database','Database'),
        ('Web Development','Web Development'),
    ]

    user=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    title=models.CharField(max_length=200)

    issuer=models.CharField(
        max_length=200
    )

    category=models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    issue_date=models.DateField()

    expiry_date=models.DateField()

    description=models.TextField(
        blank=True
    )

    certificate_file=models.FileField(
        upload_to='certificates/'
    )

    is_verified=models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.title