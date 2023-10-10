from django.db import models

# Create your models here.


class Document(models.Model):
    doc_id = models.BigAutoField(primary_key=True)
    CHOICES = (("I", "Certificate of Indigency"), ("B", "Baranggay Clearance"),
               ("R", "Certificate of Residency"), ("P", "Barangay Business Permit"),
               ("F", "Certificate of First-Time Job Seeker"), ("D", "PWD ID"))
    doc_type = models.CharField(max_length= 1, choices=CHOICES)
    fee = models.FloatField(default=0)

    class Meta:
        db_table = "Document"


class DocumentRequest(models.Model):
    doc_id = models.ForeignKey(Document, on_delete=models.CASCADE)
    resident_id = models.ForeignKey('CreateAccount.Resident', on_delete=models.CASCADE)
    dateOfApproval = models.DateField()
    requestStatus = models.CharField(max_length=10)


    class Meta:
        db_table = "Document_Request"
