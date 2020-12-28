# Heart-Disease-Prediction


![rd_cvm_hub_stage-2](https://user-images.githubusercontent.com/47864776/103246733-3090f000-496d-11eb-9cd4-f1b02400f99f.jpg)
https://www.roche.com/research_and_development/what_we_are_working_on/cardiovascular_and_metabolism.htm

<h3> Heart Disease</h3>

Heart disease describes a range of conditions that affect your heart. Diseases under the heart disease umbrella include blood vessel diseases, such as coronary artery disease; heart rhythm problems (arrhythmias); and heart defects you're born with (congenital heart defects), among others.

The term "heart disease" is often used interchangeably with the term "cardiovascular disease." Cardiovascular disease generally refers to conditions that involve narrowed or blocked blood vessels that can lead to a heart attack, chest pain (angina) or stroke. Other heart conditions, such as those that affect your heart's muscle, valves or rhythm, also are considered forms of heart disease.

Many forms of heart disease can be prevented or treated with healthy lifestyle choices.

Some key facts from the World Health Organization:

- CVDs are the number 1 cause of death globally: more people die annually from CVDs than from any other cause.
- An estimated 17.9 million people died from CVDs in 2016, representing 31% of all global deaths. Of these deaths, 85% are due to heart attack and stroke.
- Over three quarters of CVD deaths take place in low- and middle-income countries.
- Out of the 17 million premature deaths (under the age of 70) due to noncommunicable diseases in 2015, 82% are in low- and middle-income countries, and 37% are caused by CVDs.
- Most cardiovascular diseases can be prevented by addressing behavioural risk factors such as tobacco use, unhealthy diet and obesity, physical inactivity and harmful use of alcohol using population-wide strategies.
- People with cardiovascular disease or who are at high cardiovascular risk (due to the presence of one or more risk factors such as hypertension, diabetes, hyperlipidaemia or already established disease) need early detection and management using counselling and medicines, as appropriate.

<h4> Symptoms </h4>

Symptoms can include:

- Chest pain, chest tightness, chest pressure and chest discomfort (angina)
- Shortness of breath
- Pain, numbness, weakness or coldness in your legs or arms if the blood vessels in those parts of your body are narrowed
- Pain in the neck, jaw, throat, upper abdomen or back

Patients might not be diagnosed with cardiovascular disease until they have a heart attack, angina, stroke or heart failure. 
It's important to watch for cardiovascular symptoms.

https://www.mayoclinic.org/diseases-conditions/heart-disease/symptoms-causes/syc-20353118

https://www.who.int/news-room/fact-sheets/detail/cardiovascular-diseases-(cvds)





<h2> Heart Disease UCI Dataset </h2>

The database contains 76 attributes, but all published experiments refer to using a subset of 14 of them. In particular, the Cleveland database is the only one that has been used by ML researchers to this date. The "goal" field refers to the presence of heart disease in the patient. It is integer valued from 0 (no presence) to 4.

Attribute Information:

- age
- sex
- chest pain type (4 values)
- resting blood pressure
- serum cholestoral in mg/dl
- fasting blood sugar > 120 mg/dl
- resting electrocardiographic results (values 0,1,2)
- maximum heart rate achieved
- exercise induced angina
- oldpeak = ST depression induced by exercise relative to rest
- the slope of the peak exercise ST segment
- number of major vessels (0-3) colored by flourosopy
- thal: 3 = normal; 6 = fixed defect; 7 = reversable defect


Creators:

1. Hungarian Institute of Cardiology. Budapest: Andras Janosi, M.D.
2. University Hospital, Zurich, Switzerland: William Steinbrunn, M.D.
3. University Hospital, Basel, Switzerland: Matthias Pfisterer, M.D.
4. V.A. Medical Center, Long Beach and Cleveland Clinic Foundation: Robert Detrano, M.D., Ph.D.

Donor:
David W. Aha (

https://www.kaggle.com/ronitf/heart-disease-uci


<h2> Tasks </h2>

The tasks included :

- Visualization of the data
- Background Analysis
- Creation of Machine Learning Model (goal was to have >85% accuracy)


<h2> Evaluation </h2>

For the evaluation we used different metrics, such as :

- Accuracy


- Balanced Accuracy 



- f1 Score



- Sensitivity 



- Specificity




- ROC Curves & AUC Score







<html>
<head>


<body>

<h2>Machine Learning Models Results</h2>

The results of the ML models, can be seen in the detailed table below.

<table>
  <tr>
    <th>Model</th>
    <th>Accuracy</th>
    <th>Balanced Accuracy</th>
    <th>f1 Score</th>
    <th>Sensitivity</th>
    <th>Specificity</th>
    <th>AUC</th>
  </tr>
  <tr>
    <td>Logistic Regression</td>
    <td>0.9340</td>
    <td>0.9326</td>
    <td>0.9387</td>
    <td>0.9512</td>
    <td>0.9200</td>
    <td>0.9447</td>

  </tr>
  <tr>
    <td>Gradient Boost</td>
    <td>0.8460</td>
    <td>0.8481</td>
    <td>0.8478</td>
    <td>0.8051</td>
    <td>0.8863</td>
    <td>0.934</td>
  </tr>
  <tr>
    <td>AdaBoost</td>
    <td>0.8460</td>
    <td>0.8432</td>
    <td>0.8600</td>
    <td>0.8717</td>
    <td>0.8269</td>
    <td>0.9287</td>
  </tr>
  <tr>
 
  </tr>
</table>

</body>
</html>

Logistic Regression was by far the best model of the 3, with an accuracy of 93.40% and f1 score of 93.87%.
