# -*- coding: utf-8 -*-

__author__ = 'wei.tang'
__date__ = '2015/9/17'

import requests
from BeautifulSoup import BeautifulSoup
from BeautifulSoup import Tag


class FOODIE(object):
    def __init__(self, kw):
        self.url_args = kw.get('url_args')
        self.food_share_url = kw.get('food_share_url')
        self.href_attrs = kw.get('href_attrs')

    def _get_html_content(self):
        food_links = requests.get(self.food_share_url, params=self.url_args)

        if food_links.status_code != 200:
            return None
        else:
            return food_links.text

    def _get_href_dicts(self, food_links):
        soup = BeautifulSoup(food_links)

        href_list = []
        food_hrefs = soup.findAll('a', attrs=self.href_attrs)

        # for food_href in food_hrefs:
        #     print type(food_href)
        #     food_href = Tag()
        #     food_href.text
        #     print food_href.attrMap
        # print "*"*50

        for food_href in food_hrefs:
            # food_href = BeautifulSoup(food_href)
            # food_href_dicts = food_href.a.attrs
            # food_href_dict = self._transtuple2dict(food_href_tuples)
            href_list.append(dict(href=food_href.attrMap.get(u'href'), title=food_href.text))

        return href_list

    # def _transtuple2dict(self,tuples):
    #     href_dict = {}
    #     for tuple in tuples:
    #         if len(tuple) == 2:
    #             href_dict[tuple[0]] = tuple[1]
    #     return href_dict