import urllib as u
def trans(url):
    f = open('out.jpg', 'wb')
    f.write(u.request.urlopen(url).read())
    f.close