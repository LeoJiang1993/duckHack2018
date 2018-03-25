import os, time, random

from duck_hacks_2018.settings import MEDIA_ROOT, MEDIA_URL, BASE_DIR


def save_news_picture(file):
    name = file.name
    ext = os.path.splitext(name)[1]
    d = os.path.join(MEDIA_ROOT, 'ideas', 'img')
    fn = time.strftime('%Y%m%d%H%M%S')
    fn = fn + '_%d' % random.randint(0, 100)
    file_name = fn + ext
    file_path = os.path.join(d, file_name)
    url = MEDIA_URL + "ideas/img/" + file_name
    destination = open(file_path, 'wb+')
    for chunk in file.chunks():
        destination.write(chunk)
    destination.close()
    return dict(url=url, fileName=file_name)
