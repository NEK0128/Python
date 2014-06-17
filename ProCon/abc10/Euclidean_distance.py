import math

class Euclidean_distance:
	## コンストラクタ
	def __init__(self, st, go):
		self.st = st
		self.go = go

	## 距離計算メソッド
	def calc_dist(self):
		dist = math.sqrt((self.st[0] - self.go[0]) ** 2 + (self.st[1] - self.go[1]) ** 2)
		return dist
