import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
!pip install pandas-profiling==2.7.1
import pandas_profiling
from pandas_profiling import ProfileReport


dt = pd.read_csv(r"C:\Users\User\Desktop\Github Projects\Heart Disease\heart.csv")
dt.head(20)

dt.sum()


prof = ProfileReport(dt)
prof.to_file(output_file='output.html') #get an html file reporting the eda

dt.profile_report()
