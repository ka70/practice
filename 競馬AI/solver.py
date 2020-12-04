# from pulp
from pulp import *


# m = LpProblem(sense=LpMaximize)  # 数理モデル
# x[t] = LpVariable('x', lowBound=0, cat=LpInteger)  # 変数
# y = LpVariable('y', lowBound=0, cat=LpInteger)  # 変数
# z = LpVariable('z', lowBound=0, cat=LpInteger)  # 変数
# m += 70 * x + 100 * y + 20 * z  # 目的関数
# m += 3 * x + 5 * z <= 74  # 材料Aの上限の制約条件
# m += 2 * y + 8 * z <= 62  # 材料Bの上限の制約条件
# m += 8 * x + 12 * y <= 99  # 材料Cの上限の制約条件
# m += 5 * x + 10 * z <= 80  # 材料Dの上限の制約条件
# m.solve()  # ソルバーの実行
# print(value(x), value(y), value(z), value(m.objective))  # 3.0, 6.0,  6.0, 930
# 重さ
w = [2, 1, 3, 2, 1, 4]

# 価値
v = [3, 2, 6, 1, 3, 8]

# 限度：10kg
W = 10

r = range(len(w))

# 数理モデル
m = pulp.LpProblem(sense=LpMaximize)

# 変数
x = [pulp.LpVariable('x%d' % i, cat=LpBinary) for i in r]

# 目的関数
m += pulp.lpDot(v, x)

# 限度を設定し、問題を解く
m += pulp.lpDot(w, x) <= W
m.solve()
print('最大価値:{} / 組み合わせ:{}'.format(pulp.value(m.objective),
                                  [i for i in r if pulp.value(x[i]) > 0.5]))
