# -*- coding: utf-8 -*-

import urllib2
import sys

from bs4 import BeautifulSoup


sysCharType = sys.getfilesystemencoding()
my_blog_url = "http://yuanhuan.blog.51cto.com"
headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}


def div_has_class(html_div, html_attr_name, html_attr_value):
    div_attrs = html_div.attrs

    if len(div_attrs) == 0:
        return False

    try:
        real_html_attr_value = div_attrs[html_attr_name][0]
    except KeyError:
        return False

    # print real_html_attr_value, html_attr_name, html_attr_value
    if html_attr_value == real_html_attr_value:
        return True
    else:
        return False


def print_all_links(url):
    req = urllib2.Request(url=url, headers=headers)
    html = urllib2.urlopen(req).read()
    sys_html = html.decode(sysCharType).encode('utf-8')
    soup = BeautifulSoup(sys_html)
    all_div = soup.find_all("div")
    for each_div in all_div:
        if not div_has_class(each_div, 'class', 'artHead'):
            continue

        html_h3_a = each_div.find("h3").find("a")
        url_link = html_h3_a.get('href')
        title = html_h3_a.string
        sub_divs = each_div.find_all("div")
        time = ""
        for each_sub_div in sub_divs:
            if not div_has_class(each_sub_div, 'class', 'time'):
                continue

            time = each_sub_div.string
            break

        print time, my_blog_url + url_link, title


def print_each_page(url):
    req = urllib2.Request(url=url, headers=headers)
    html = urllib2.urlopen(req).read()
    sys_html = html.decode(sysCharType).encode('utf-8')
    soup = BeautifulSoup(sys_html)
    all_a = soup.find_all("a")
    each_link = ""
    for each_a in all_a:
        a_link = each_a.get('href')
        if a_link.startswith("/"):
            if a_link.find("p-") < 0:
                continue
            else:
                each_link = a_link

    total_pages_number = int(each_link[each_link.index("p-") + 2:])
    link_prefix = my_blog_url + each_link[0:each_link.index("p-") + 2]
    for i in range(1, total_pages_number + 1):
        link = link_prefix + str(i)
        print_all_links(link)


print_each_page(my_blog_url)

