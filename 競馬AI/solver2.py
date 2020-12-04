from pulp import *

Max_Money = 10000  # 持ち金
# 1位になる確率
w = [0.4, 0.3, 0.2]
# 3位以内になる確率
v = [0.5, 0.4, 0.5]

# 数理モデル
m = pulp.LpProblem(sense=LpMaximize)
# 変数
r = range(len(w))
# x = [pulp.LpVariable('x_{}'.format(i), cat=LpBinary) for i in r]
x = [pulp.LpVariable('x%d' % i, lowBound=100, cat=LpInteger) for i in r]
y = [pulp.LpVariable('y%d' % i, lowBound=100, cat=LpInteger) for i in r]

# 目的関数
m += pulp.lpDot(w, x) + pulp.lpDot(v, y)
# m += pulp.lpSum(w[i]*x[i]+v[i]*y[i] for i in r)
# m += pulp.lpSum([w[i], v[i]], [x[i], y[i]] for i in r)
# 制約条件
m += pulp.lpSum(x) + pulp.lpSum(y) <= Max_Money
# 最適化計算
m.solve()
# 出力
print("[単勝]")
for i in r:
    print('番号:{} 掛け金:{}'.format(i, value(x[i])))
print("[複勝]")
for i in r:
    print('番号:{} 掛け金:{}'.format(i, value(y[i])))
print('\n目的関数:{}'.format(value(m.objective)))
