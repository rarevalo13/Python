import requests, bs4
res = requests.get('http://thearevalos.com/blog/2016/6/15/fynnlan-seeley-33-weeks')

try:
	res.raise_for_status()

except Exception as exc:
    print('There was a problem: %s' % (exc))
len(res.text)
blog = bs4.BeautifulSoup(res.text)
type(blog)
blogfile = open('blog.html')
blogfile2 = bs4.BeautifulSoup(blogfile)

