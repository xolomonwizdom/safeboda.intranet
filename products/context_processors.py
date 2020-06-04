from products.models import Notification

def get_notification(request):
    """return notification on everypage"""
    notification = Notification.objects.first()
    return {
        'notification': notification
    }