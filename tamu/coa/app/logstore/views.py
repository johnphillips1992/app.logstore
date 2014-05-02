from django.views.generic import View

from tamu.coa.app.logstore.models import Log



class LogView(View):
    def get(self, request, **kwargs):
        print request.POST
        log = Log.objects.create(log=str(request.POST))
        return

