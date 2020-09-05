from celery import task

@task()
def send_notification(name="send_notification"):
    print('Notification Test')
