from django.http import HttpResponse


class StripeWH_Handler:
    ''' handle webhooks from stripe'''

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        '''handle webhook events'''
        return HttpResponse(
            content=f"Unhandled webhook recieved {event['type']}",
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        '''handle payment intent succeeded event'''
        return HttpResponse(
            content=f"webhook recieved {event['type']}",
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        '''handle payment intent failed event'''
        return HttpResponse(
            content=f"webhook recieved {event['type']}",
            status=200
        )
