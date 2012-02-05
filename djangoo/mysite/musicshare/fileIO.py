def upload_Handler(f):
    destination = open('text.google', 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()

