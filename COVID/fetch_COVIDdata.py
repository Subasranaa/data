import pandas as pd
from datetime import datetime
owid_df = pd.read_csv("owid-covid-data.csv")
us_df = owid_df[owid_df["iso_code"] == "USA"]
us_df.reset_index()
now = datetime.now()
dt_string = now.strftime("%Y-%m-%d-%H-%M-%S")
us_df = us_df.fillna(0)
us_df.to_csv(f"{dt_string}-OWID.csv")
