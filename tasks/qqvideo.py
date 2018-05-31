# coding=utf-8

import util

homepage = 'http://v.qq.com/vplus/a0e97f895a6978c918616f9785799de9'

class QQVideoData(object):

    def __init__(self,url=homepage):
        self.ulr = url
        self.check = True  #检查点，防止无法创建soup对象出现错误
        self.soup = util.get_soup(url)
        if self.soup is None:
            self.check = False

    #获得播放量
    def get_play_num(self):
        vnum = self.soup.select('.count_num')
        if vnum is not None:
            x = vnum[1]
            num = x.string
        else:
            num = '**找不到播放量**'
        return num

    #详细播放量
    def get_play_num_more(self):
        titles = self.soup.select('.figure_title')
        nums = self.soup.select('.info_inner')
        s = ' 腾讯视频-最新%d个视频：\n' % len(titles)
        for x in range(len(titles)):
            s += str(x+1) + '.'+titles[x].string+'\n 播放量：'+nums[x].string+'\n'
        return s
if __name__ == '__main__':
    v = QQVideoData()
    print(v.get_play_num())
    print(v.get_play_num_more())
