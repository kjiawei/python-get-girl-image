import requests
import re




def read_html_info(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    }
    res = requests.get(url, headers=headers)
    res.encoding = 'gb2312'
    html = res.text
    return html


def get_Class_list():
    url = 'http://www.mmonly.cc/mmtp/'
    html = read_html_info(url)
    pattern = re.compile(r'http://www.mmonly.cc/mmtp/\w+/')
    L = re.findall(pattern, html)
    LIS = []
    for i in L:
        if i not in LIS:
            LIS.append(i)
    print('get class list 被调用')
    return LIS


def write_to_file(url):
    html = read_html_info(url)
    pattern = re.compile(r'http://t1.mmonly.cc/uploads/tu/.+?jpg')
    src = re.findall(pattern, html)[0]
    name = src[-14:-5]
    headers = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'
    }
    image = requests.get(src, headers=headers)
    data = image.content
    with open('D:/beautiful/' + name + '.jpg', 'wb') as f:
        f.write(data)
    print(name + '.jpg' + '下载完毕')

def get_image(url):
    html = read_html_info(url)
    pattern = re.compile(r'<a>共(\d+?)页: </a>')
    pages = int(re.findall(pattern, html)[0])
    for page in range(1, pages + 1):
        try:
            if page == 1:
                write_to_file(url)
            else:
                url1 = (url[0:-5] + '_' + (str(page) + '.html'))
                write_to_file(url1)
        except Exception:
            continue


def get_inner_list(url):
    html = read_html_info(url)
    pattern = re.compile(url + r'\d+?.html')
    inner_list1 = re.findall(pattern, html)
    inner_list2 = []
    for i in inner_list1:
        if i not in inner_list2:
            inner_list2.append(i)
    for url_inner in inner_list2:
        try:
            get_image(url_inner)
        except Exception:
            continue


lis = get_Class_list()
for i in lis:
    get_inner_list(i)


# print(get_Class_list())
# get_inner_list('http://www.mmonly.cc/mmtp/qcmn/')
# get_image('http://www.mmonly.cc/mmtp/qcmn/238324.html')
# write_to_file('http://www.mmonly.cc/mmtp/qcmn/238324_2.html','nima')
