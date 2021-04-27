import pandas as pd
import plotly.express as px

df=pd.read_csv("data.csv")
fig=px.bar(df,x="Country",y="InternetUsers",title="Internet Users Per Country",color="Country")
fig.show()