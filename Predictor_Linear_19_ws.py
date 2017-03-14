X_value=input('Input a qury sequence: ')
window_size=19
feature_list='ACDEFGHIKLMNPQRSTVWY'
features_dict=dict() 
binary_list=[0]*38
binary_list.insert(19,1)
i=0
for amino_acids in feature_list:
    features_dict[amino_acids]=binary_list[i:i+20]
    i=i+1
features_dict['Z']=[0]*20

X_list1=[]
for i in range(0,int(window_size/2),1):
    X_list1.append([0]*20)
for i in X_value:
    for key, value in features_dict.items():
        if key==i:
            X_list1.append(value)
for i in range(0,int(window_size/2),1):
    X_list1.append([0]*20)
X_test=[]
for i in range(int(window_size/2),len(X_list1)-int(window_size/2),1):
    list_every_window=[]
    for k in range(i-int(window_size/2),i+int(window_size/2)+1,1):
        list_every_window.extend(X_list1[k])
    X_test.append(list_every_window)
labels_dict={'G':0,'M':1,'STOP':2}
features=list()
labels=list()
f=open('membrane-alpha_2state.3line.txt','r')
m=0
for line in f:
    if m%3==0:
        features.extend(['Z']*(int(window_size/2)))
        labels.extend(['STOP']*(int(window_size/2)))
    if m%3==1:
        for i in line.strip():
            features.append(i)
    if m%3==2:
        for i in line.strip():
            l1=labels.append(i)
    m=m+1
features.extend(['Z']*(int(window_size/2)))
labels.extend(['STOP']*(int(window_size/2)))
f=open('membrane-alpha_2state.3line.txt')
o1=open('s1.txt','w')
o2=open('s2.txt','w')
for i in range(int(window_size/2),int(len(labels)-window_size/2)):
    o1.write(labels[i])
    o1.write('\n')
    for window_member in range(i-int(window_size/2),i+int(window_size/2)+1):
       o2.write(features[window_member])
    o2.write('\n')
f.close()
o1.close()
o2.close()
o1=open('s1.txt')
list_of_label_code=list()
for label_contents in o1:
    label_contents=label_contents.strip('\n').split(' ')
    for n,i in enumerate(label_contents):
        if i in labels_dict:
            label_contents[n]=labels_dict[i]
            list_of_label_code.append(label_contents[n])
o2=open('s2.txt')
list_of_feature=list()
for feature_contents in o2:
    list_of_window=list()
    feature_contents=feature_contents.strip('\n').split(' ')
    feature_contents=list(feature_contents[0])
    for n, i in enumerate(feature_contents):
        if i in features_dict:
            feature_contents[n]=features_dict[i]
            list_of_window.extend(feature_contents[n])
    list_of_feature.append(list_of_window)
list_label_final=list()
list_feature_window_final=list()
for i in list_of_label_code:
    if i!=2:
        list_label_final.append(i)

for i in list_of_feature:
    if i[(20*(int(window_size/2))):(20*int((window_size/2+1)))]!=[0]*20:
        list_feature_window_final.append(i)
import numpy as np
from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier
clf = OneVsRestClassifier(SVC(kernel='linear', C=1))
clf.fit(list_feature_window_final, list_label_final)
y_test=clf.predict(X_test)
result=[]
label_dict={0:'G',1:'M'}
for n,i in enumerate(y_test):
        if i in label_dict:
            y=label_dict[i]
            result.append(y)
result_string=''.join(result)
print (result_string)
