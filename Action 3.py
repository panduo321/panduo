import pandas as pd

df = pd.read_csv("car_complain.csv")
df = df.drop("problem",axis=1).join(df.problem.str.get_dummies(","))
df["brand"] = df["brand"].apply(lambda x:x.replace("一汽-大众","一汽大众"))

result1 = df.groupby("brand")["id"].agg(["count"])
result2 = df.groupby("car_model")["id"].agg(["count"])
result2 = result2.sort_values("count",ascending=False)

#平均车型投诉：品牌总投诉数/车型数?
#result3 = df.groupby("brand")["car_model"].nunique()


print(result1,result2)



