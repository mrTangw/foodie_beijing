# -*- coding: utf-8 -*-

__author__ = 'wei.tang'
__date__ = '2015/9/17'

from foodie import FOODIE


class CHIPHELL(FOODIE):
    def __init__(self, kw):
        FOODIE.__init__(self, kw)


if __name__ == "__main__":

    for i in range(0, 19):
        chip_args = dict(href_attrs={"class": "s xst"}, food_share_url="http://www.chiphell.com/forum.php", url_args=dict(mod="forumdisplay", fid=233, typeid=382, filter="typeid", page=i))
        chiphell = CHIPHELL(chip_args)
        html_content =  chiphell._get_html_content()
        href_dicts = chiphell._get_href_dicts(html_content)

        for href_dict in href_dicts:

            if u'北京' in href_dict.get("title"):
                print u"{} {}".format(href_dict.get("title"), href_dict.get('href'))
