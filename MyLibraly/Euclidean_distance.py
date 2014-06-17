#
#更新日: 2014/06/16
#作成者: 松田　健司
#概要:  ユークリッド距離のクラス
#引数:  self コンストラクタ用
#         st  (int)始点の座標
#         go  (int)終点の座標
#
#メソッド： calc_dist ユークリッド距離計算
#返り値  ： dist (double)ユークリッド距離



import math

class Euclidean_distance:
    ## コンストラクタ
    def __init__(self, st, go):
        self.st = st
        self.go = go

    ## 距離計算メソッド
    def calc_dist(self):
        dist = math.sqrt((self.st[0] - self.go[0]) ** 2
        + (self.st[1] - self.go[1]) ** 2)
        return dist
