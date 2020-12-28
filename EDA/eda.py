import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


dt = pd.read_csv(r"C:\Users\User\Desktop\Github Projects\Heart Disease\heart.csv")
dt.head(20)

dt.sum()

dt.target.value_counts() #how many target(diseased patients) does the dataset contain?

#bar chart plot, to visualize the targets
sns.countplot(x="target", data=dt, palette="rocket")
plt.show()


HD = len(dt[dt.target == 1]) #Heart Disease
ND = len(dt[dt.target == 0]) #No Heart Disease

print("Percentage of Patients That Have Heart Disease: {:.2f}%".format((HD / (len(dt.target))*100)))
print("Percentage of Patients That Don't Have Heart Disease: {:.2f}%".format((ND / (len(dt.target))*100)))

#Now we want to see how many female/male patients does the dataset contain.
#This will help us to have a better understanding of the data and even find if there is higher correlation between the disease and sex.

Fem = len(dt[dt.sex == 0]) #Female patients
Mal = len(dt[dt.sex == 1]) #male patients
print("Percentage of Female Subjects On The Study: {:.2f}%".format((Fem / (len(dt.sex))*100)))
print("Percentage of Male Subjects On The Study: {:.2f}%".format((Mal / (len(dt.sex))*100)))


#bar chart plot, to visualize the sex
sns.countplot(x="sex", data=dt, palette="rocket")
plt.show()


#General Age Mean
dt.age.mean()

#Group data by the targets (0=No disease, 1= Disease), Max Results
dt.groupby("target").max()


dt.groupby("target").min() #Group data by the targets (0=No disease, 1= Disease), Min Results


dt.groupby("target").mean() #Group data by the targets (0=No disease, 1= Disease), Mean Results


#Boxplot of taget/age
#Is age an important factor for the disease?
sns.set_theme(style="whitegrid")
dt.head()
ax = sns.boxplot(x="target", y="age", hue="target", data=dt, palette="rocket")


#Detailed boxplot of sex/age - Orange = HD, Purple=ND, 0=Female Patients, 1=Male Patients

sns.set_theme(style="whitegrid")
dt.head()
ax = sns.boxplot(x="sex", y="age", hue="target", data=dt, palette="rocket")


#Detailed graph of frequency of disease & age
pd.crosstab(df.age,df.target).plot(kind="bar",figsize=(30,7))
plt.title('Heart Disease Frequency for Ages')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.savefig('heartDiseaseAndAges.png')
plt.show()


#Bar chart showing the frequency of disease between the sexes (0=female, 1=male)
pd.crosstab(df.sex,df.target).plot(kind="bar",figsize=(15,6),color=['#a5531c', '#a51c61' ])
plt.title('Heart Disease Frequency for Sex')
plt.xlabel('Sex ') #0=Female, 1=Male Patients
plt.xticks(rotation=0)
plt.legend(["No Disease", "Diseased"])
plt.ylabel('Frequency')
plt.show()



#Boxplot of chest pain/max heart rate

sns.set_theme(style="whitegrid")
#tips = sns.load_dataset("tips")
dt.head()
ax = sns.boxplot(x="cp", y="thalach", hue="cp", data=dt, palette="rocket")


#Boxplot of chest resting heart rate/max heart rate

sns.set_theme(style="whitegrid")
#tips = sns.load_dataset("tips")
dt.head()
ax = sns.boxplot(x="restecg", y="thalach",hue="restecg",
                 data=dt, palette="rocket")



#Scatter plot to see if there is a correlation between age & max heart rate
plt.scatter(x=df.age[df.target==1], y=df.thalach[(df.target==1)], c="red")
plt.scatter(x=df.age[df.target==0], y=df.thalach[(df.target==0)])
plt.legend(["Disease", "Not Disease"])
plt.xlabel("Age")
plt.ylabel("Maximum Heart Rate")
plt.show()

#Boxplot of target/cholesterol
#we want to see if chol is more noticable in diseased patients
sns.set_theme(style="whitegrid")
dt.head()
ax = sns.boxplot(x="target", y="chol",hue="target",
                 data=dt, palette="rocket")



#Scatter plot of age/chol
#Do older people have higher chol or other factor to consider?

plt.scatter(x=df.age[df.target==1], y=df.chol[(df.target==1)], c="red")
plt.scatter(x=df.age[df.target==0], y=df.chol[(df.target==0)])
plt.legend(["Disease", "Not Disease"])
plt.xlabel("Age")
plt.ylabel("Chol")
plt.show()

#How relevant is chest pain?
#Boxplot of chest pain / target
sns.set_theme(style="whitegrid")
#tips = sns.load_dataset("tips")
dt.head()
ax = sns.boxplot(x="target", y="cp",hue="target",
                 data=dt, palette="rocket")
                 

#Scatter plot of age/chest pain
plt.scatter(x=df.age[df.target==1], y=df.cp[(df.target==1)], c="red")
plt.scatter(x=df.age[df.target==0], y=df.cp[(df.target==0)])
plt.legend(["Disease", "Not Disease"])
plt.xlabel("Age")
plt.ylabel("cp")
plt.show()

#Bar chart, heart disease frequency /slope
pd.crosstab(df.slope,df.target).plot(kind="bar",figsize=(15,6),color=['#a5531c','#a51c61' ])
plt.title('Heart Disease Frequency for Slope')
plt.xlabel('The Slope of The Peak Exercise ST Segment ')
plt.xticks(rotation = 0)
plt.ylabel('Frequency')
plt.show()


#Cologram, to see the correlation between the variables 

# Plot
plt.figure(figsize=(15,15), dpi= 80)
sns.heatmap(dt.corr(), xticklabels=dt.corr().columns, yticklabels=dt.corr().columns, cmap='RdYlGn', center=0, annot=True)

# Decorations
plt.title('Correlation Between Variables', fontsize=22)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()
