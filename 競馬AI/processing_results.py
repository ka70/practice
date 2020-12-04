def processing_results(results):
    results = pd.read_pickle("results.pickle")
    df = results.copy()
    # 着順
    df = df[~(df["着順"].astype(str).str.contains("\D"))]
    df["着順"] = df["着順"].astype(int)
    # 性別
    df["性別"] = df["性齢"].map(lambda x: str(x)[0])
    df["性別"] = df["性別"].map({"牡": 1, "牝": 0, "セ": 1})  # 雄:1,牝:0
    # df["性別"]=df["性別"].astype(int)
    # df["性別"] = pd.get_dummies(df["性別"])
    # 年齢
    df["年齢"] = df["性齢"].map(lambda x: str(x)[1:])
    df["年齢"] = df["年齢"].astype(int)
    # 体重
    df["体重"] = df["馬体重"].str.split("(", expand=True)[0].astype(int)
    # 体重変化
    df["体重変化"] = df["馬体重"].str.split("(", expand=True)[1].str[:-1].astype(int)
    # 人気と単勝をint型に
    df["人気"] = df["人気"].astype(int)
    df["単勝"] = df["単勝"].astype(float)
    # いらない列の消去
    df.drop(["性齢", "タイム", "着差", "馬体重", "調教師"], axis=1, inplace=True)

    return df
