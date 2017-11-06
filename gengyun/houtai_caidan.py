#coding=utf-8
from __future__ import unicode_literals

"""
后台菜单列表
"""
def caidan():
    houtai_caidan = []
    grxx_admin = ['个人信息','/houtai_admin_grxx/']
    gy_lingdi = ['我的耕耘','/houtai_admin_wdgy/']
    gy_zhongzi = ['耕耘种子','/houtai_admin_gyzz/']
    houtai_caidan.append(grxx_admin)
    houtai_caidan.append(gy_lingdi)
    houtai_caidan.append(gy_zhongzi)
    return houtai_caidan



if __name__ == '__main__':
    caidan()