from django.http import HttpResponse

class StripeWH_Handler:
    ''' handle webhooks from stripe'''

    def __init__(self, request):
        self.request = request
    
    def handler_event(self, event):
        '''handle webhook events'''
        return HttpResponse(
            content=f"webhook recieved {event['type']}",
            status=200
        )