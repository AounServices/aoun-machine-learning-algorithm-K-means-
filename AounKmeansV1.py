{\rtf1\ansi\ansicpg1252\cocoartf1671
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww28600\viewh18000\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import numpy as np\
import pandas as panda\
import matplotlib.pyplot as plot\
%matplotlib inline\
from sklearn.preprocessing import normalize\
import json\
\
file = panda.read_excel('https://aoun-bucket.s3.eu-central-1.amazonaws.com/files/event_services_categories_annotated1.xlsx')\
\
\
df2= panda.DataFrame(\{\
    'x':np.array(file["user_id"]),\
    'y':np.array(file["annotated_value"])\
\})\
\
\
k=8\
# np.random.seed(200)\
\
\
centroids = \{\
    i+1:[np.random.randint(0,1000), np.random.randint(0,1000)]\
    for i in range(k)\
\}\
\
\
\
fig=plot.figure(figsize=(5,5))\
plot.scatter(df2['x'],df2['y'],color='k')\
plot.scatter(*centroids[1],color='r')\
plot.scatter(*centroids[2],color='g')\
plot.scatter(*centroids[3],color='b')\
plot.scatter(*centroids[4],color='y')\
plot.scatter(*centroids[5],color='m')\
plot.scatter(*centroids[6],color='c')\
plot.scatter(*centroids[7],color='r')\
plot.scatter(*centroids[8],color='k')\
\
\
\
plot.show()\
\
\
# loaded_model = joblib.load('saved_model.pkl') \
# predicted_y = model1.fit_predict(df2)\
\
# predictions_list= list(predicted_y)\
# print("labels =>  ",(predicted_y))\
# new_data=list()\
\
# for i in range(len(predictions_list)):\
#   new_data.append(\{'user_id':df2['x'][i],'cluster_id':predictions_list[i]\})\
  \
\
# print("annotated data  =>  ",(new_data))\
machineLearning()\
\
\
\
\
\
\
\
\
# ==============================================================================\
# machine learning part\
\
\
\
\
from sklearn.cluster import KMeans\
from sklearn.externals import joblib\
\
\
\
def machineLearning():\
  model1 = KMeans(n_clusters=k,verbose=False,max_iter=10000)\
  model1.fit(df2)  \
  labelsML=model1.predict(df2)\
  centroidsML=model1.cluster_centers_\
  predicted_y = model1.fit_predict(df2)\
\
  \
  fig=plot.figure(figsize=(5,5))\
  plot.scatter(*centroidsML[0],color='g')\
  plot.scatter(*centroidsML[1],color='b')\
  plot.scatter(*centroidsML[2],color='r')\
  plot.scatter(*centroidsML[3],color='y')\
  plot.scatter(*centroidsML[4],color='m')\
  plot.scatter(*centroidsML[5],color='c')\
  plot.scatter(*centroids[6],color='r')\
  plot.scatter(*centroids[7],color='k')\
\
\
  \
  colmap=\{1:'g',2:'b',3:'r',4:'y',5:'m',6:'c',7:'r',8:'k'\}\
  colors = map(lambda x: colmap[x+1],labelsML)\
  print(colors)\
  colors1=list(colors)\
  plot.scatter(df2['x'],df2['y'],color=colors1 , alpha=1, edgecolor='k')\
\
  plot.show()\
  print('fuck =',predicted_y)\
  print(len(predicted_y))\
\
  # saving the model\
  joblib.dump(model1, 'saved_model.pkl') \
\
  \
  #export json file\
  \
\
  predictions_list= list(predicted_y)\
  new_data=list()\
\
  for i in range(len(predictions_list)):\
    new_data.append(\{"user_id":np.int64(df2['x'][i]),"cluster_id":  (predictions_list[i])\})\
\
    \
  print("annotated data  =>  ",(new_data))\
  print("Saving ....")\
#   with open('annotatedData2.text', 'w') as json_file:\
#     json.dump(my_details, json_file)\
  with open('annotatedData6.text', 'w') as f:\
    f.write(str(new_data))\
\
\
\
\
\
\
\
\
\
\
\
}