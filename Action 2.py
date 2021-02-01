import pandas as pd

df = pd.read_excel("action 2 data.xlsx")
df = df.drop("姓名",axis=1)
df.index = ["张飞","关羽","刘备","典韦","许楮"]
print(df)
print("平均成绩：","\n",df.mean())
print("最小成绩：","\n",df.min())
print("最大成绩：","\n",df.max())
print("成绩方差：","\n",df.var())
print("成绩标准差：","\n",df.std())

df["总成绩"] =df.apply(lambda x:x.sum(),axis = 1)
df = df.sort_values('总成绩', ascending=False)
print(df)