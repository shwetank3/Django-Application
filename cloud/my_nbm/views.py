from django.shortcuts import render

# Create your views here.
from .models import Analysis
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.conf import settings
from .forms import CreateNewAnalysis
import datetime
#from django.contrib.auth.models import user

#login_required
def index(request):
    """
    View function for home page of site.
    """
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    # Generate counts of some of the main objects
    num_pending=Analysis.objects.filter(status__exact='p').filter(owner=request.user).count()
    num_completed=Analysis.objects.filter(status__exact='c').filter(owner=request.user).count()
	
    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_pending':num_pending,'num_completed':num_completed,'num_visits':num_visits},
		)
	
class AnalysisListView(LoginRequiredMixin,generic.ListView):
    model = Analysis
    def get_queryset(self):
        return Analysis.objects.filter(owner=self.request.user)


class AnalysisDetailView(LoginRequiredMixin,generic.DetailView):
    model = Analysis
    def get_queryset(self):
        return Analysis.objects.filter(owner=self.request.user)

def new_analysis(request):
    if request.method == 'POST':
        form  = CreateNewAnalysis(request.POST)
    else:
        form  = CreateNewAnalysis(initial={'nodes': '23',})
    return render(request,'my_nbm/create_new.html',{'form':form})

class AnalysisCreate(CreateView):
    model = Analysis
    fields = '__all__'
    initial={'submission_date':datetime.date.today(),'status':'p','co_ord':'[-2 4.5 0;-2 5 0;0 5 0;0 0 0;2 0 0;2 .5 0]','depth':10,'n_els':'[3 4 6 4 3]','n_el_l':20,'El':29500,'nu':0.3,'Fy':50}

class AnalysisUpdate(UpdateView):
    model = Analysis
    fields = ['submission_date','node','element','o_stress','o_strain','status']

class AnalysisDelete(DeleteView):
    model = Analysis
    success_url = reverse_lazy('index')
	
'''
    def analysis_detail_view(request,pk):
        try:
            analysis_id=Analysis.objects.get(pk=pk)
        except analysis.DoesNotExist:
            raise Http404("Analysis does not exist")

        #book_id=get_object_or_404(Book, pk=pk)
      
        return render(
            request,
            'my_nbm/analysis_detail.html',
            context={'analysis':analysis_id,}
    )
'''

	
	
	
	
