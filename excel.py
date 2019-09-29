import pandas as pd
frame=pd.read_csv("MIDAS Site -  14276 at A3 southbound between A283 near Milford (south) and A333 (200094033).csv",names=["A","B","C","D","E","F","G","H","I","J","K","L"])
group=frame[["D","E","F","G","H","I"]].groupby(frame["A"]).sum()
group.to_csv("hello.csv")

