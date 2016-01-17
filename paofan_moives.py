# -*- coding: utf-8 -*-

__author__ = 'wei.tang'
__date__ = '2016/01/17'

from BeautifulSoup import BeautifulSoup

from foodie import FOODIE


class PAOFAN(FOODIE):
    def __init__(self, kw):
        FOODIE.__init__(self, kw)

    def _get_href_dicts(self, food_links):
        href_list = []
        try:
            soup = BeautifulSoup(food_links)
            moive_contens = soup.find("div",id='sideleft').dt.text
            href_list.append(dict(title=moive_contens))
        except Exception,e:
            pass

        return href_list

if __name__ == "__main__":

    for i in range(1, 20167):
        chip_args = dict(href_attrs={"class": "s xst"}, food_share_url="http://www.chapaofan.com/", url_args=dict(p=i))
        #print u"{}p={}".format("http://www.chapaofan.com/",i)
        paofan = PAOFAN(chip_args)
        html_content =  paofan._get_html_content()
        href_dicts = paofan._get_href_dicts(html_content)

        for href_dict in href_dicts:

            if u'720' in href_dict.get("title"):
                print u"{}".format(href_dict.get("title"))
