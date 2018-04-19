from django.db import models
import uuid
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Analysis(models.Model):
    """
    Model representing a specific copy of a book (i.e. that can be borrowed from the library).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique Id for the Analysis")
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    submission_date = models.DateField(null=True, blank=True)
    co_ord = models.TextField (max_length=50)
    depth = models.IntegerField()	
    n_els = models.TextField (max_length=20)
    n_el_l = models.TextField (max_length=20)
    El=models.IntegerField()
    nu=models.CharField(max_length=5)
    Fy=models.IntegerField()
    
    Boundary_Condition = (
        ('p', 'pin'),
        ('f', 'fix'),
    )
    BC = models.CharField(max_length=1, choices=Boundary_Condition, blank=True, default='p', help_text='Boundary Condition')	
	
    analysistype = (
        ('b', 'buckle'),
        ('s', 'static'),
    )
    Analysis_type = models.CharField(max_length=1, choices=analysistype, blank=True, default='s', help_text='Analysis Type')	
	
    testtype= (
        ('b', 'bend'),
        ('s', 'shear'),
        ('u', 'uniform'),
    )
    Test_type = models.CharField(max_length=1, choices=testtype, blank=True, default='s', help_text='Boundary Condition')	
	
    o_stress = models.CharField(max_length=200)
    o_strain = models.CharField(max_length=200)
    
	
	
    ANALYSIS_STATUS = (
        ('p', 'Pending'),
        ('c', 'Completed'),
    )

    status = models.CharField(max_length=1, choices=ANALYSIS_STATUS, blank=True, default='p', help_text='Analysis Status')

    class Meta:
        ordering = ["submission_date","status"]
      
    def __str__(self):
        """
        String for representing the Model object
        """
        return '{0} ({1}) // {2} // {3}'.format(self.owner,self.submission_date,self.status,self.id)
	
    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this Analysis.
        """
        return reverse('analysis-detail', args=[str(self.id)])
