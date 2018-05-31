# coding=utf-8

import util

homepage = 'http://i.youku.com/i/UMzg0ODQyNDk4OA==/videos'

class YoukuData(object):

    def __init__(self,url=homepage):
        self.ulr = url
        self.check = True
        self.soup = util.get_soup(url)
        if self.soup is None:
            self.check = False

    #获得播放量
    def get_play_num(self):
        vnum = self.soup.select('.vnum')
        if vnum is not None:
            x = vnum[0]
            n = x.get('title')
            num = n
        else:
            num = '**找不到播放量**'
        return num

    #获得订阅数
    def get_sub_num(self):
        snum = self.soup.select('.snum')
        if snum is not None:
            x = snum[0]
            n = x.get('title')
            num = n
        else:
            num = '**找不到订阅数**'
        return num

    #详细播放量
    def get_play_num_more(self):
        titles = self.soup.select('.v-meta-title')
        nums = self.soup.select('.v-num')
        times = self.soup.select('.v-publishtime')

        s = ' 优酷视频-最新%d个视频：\n' % len(titles)
        for x in range(len(titles)):
            s += str(x+1) + '.'+titles[x].string+'\n 播放量：'+nums[x].string+'\n'
        return s

if __name__ == '__main__':
    v = YoukuData()
    print(v.get_play_num_more())