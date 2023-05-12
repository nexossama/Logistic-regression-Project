import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from LogisticRegression import myLogisticRegression,accuracy
from helpers import ConvertData,ConvertClass


data = pd.read_csv('student-mat.csv',sep=';')
X = data[['school', 'sex', 'age', 'address', 'famsize', 'Pstatus', 'Medu', 'Fedu',
       'Mjob', 'Fjob', 'reason', 'guardian', 'traveltime', 'studytime',
       'failures', 'schoolsup', 'famsup', 'paid', 'activities', 'nursery',
       'higher', 'internet', 'romantic', 'famrel', 'freetime', 'goout', 'Dalc',
       'Walc', 'health', 'absences']]


#codage des donnees nominale
df31 = X.replace({'Mjob': {'at_home': 0, 'teacher': 1, 'services': 2, 'health': 3, 'other': 4}})
df32 = df31.replace({'Fjob':{'at_home': 0, 'teacher': 1, 'services': 2, 'health': 3, 'other': 4}})
df33 = df32.replace({'school':{'GP': 0, 'MS': 1}})
df34 = df33.replace({'sex':{'M': 1, 'F': 0}})
df34 = df34.replace({'address':{'U': 1, 'R': 0}})
df35 = df34.replace({'famsize':{'GT3': 0, 'LE3': 1}})
df36 = df35.replace({'Pstatus':{'A': 1, 'T': 0}})
df37 = df36.replace({'higher':{'yes': 1, 'no': 0}})
df38 = df37.replace({'internet':{'yes': 1, 'no': 0}})
df39 = df38.replace({'romantic':{'yes': 1, 'no': 0}})
df41 = df39.replace({'reason':{'course':0,'home':1,'reputation':2,'other':3}})
df42 = df41.replace({'guardian':{'mother':0,'father':1,'other':2}})
df43 = df42.replace({'schoolsup':{'yes': 1, 'no': 0}})
df44 = df43.replace({'famsup':{'yes': 1, 'no': 0}})
df45 = df44.replace({'paid':{'yes': 1, 'no': 0}})
df46 = df45.replace({'activities':{'yes': 1, 'no': 0}})
df47 = df46.replace({'nursery':{'yes': 1, 'no': 0}})


# la definition et le codage de la variable cible
y = data['G3'].values
def encode_data(y):
    encoded_data=[]
    for i in y:
        if i>=10:
            encoded_data.append(1)
        if i <10:
            encoded_data.append(0)
    return encoded_data
y=encode_data(y)

def Std(x):
    return (x -x.mean(axis=0,numeric_only=True)) / x.std(axis=0)

# Standardisation des donnees
X_std = Std(df47)

#L'application de l'ACP
pca = PCA(n_components=X_std.shape[1])
pca.fit(X_std)
components = pca.components_
explained_variances = pca.explained_variance_ratio_
variances = explained_variances
for i, col in enumerate(X_std.columns):
    print(f"{col}: {variances[i]}")

print("===================================")

#========================================== Accuracy =============================
# la reduction de dimension

X = X_std[['school','sex','age','address','famsize','Pstatus','Medu','Fedu','Mjob','Fjob']].values

#Spliting the data
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2, random_state=3)



# l'application de la regression logistique
model = myLogisticRegression()
print(model.fit(X_train, Y_train))


# calcul de la precision
y_pred = model.predict(X_test)
acc = accuracy(y_pred,Y_test)
print("la precision est :",acc*100)


print("===================================")

#========================================== Prediction =============================
liste1=['Gabriel Pereira','Female',18,'urban',7,'living together','higher education','5th to 9th grade','health : care related','services (e.g. administrative or police)']

xx = ConvertData(liste1)
print(xx)
data_converted =  (xx - np.mean(xx)) / np.std(xx)
final_Data = np.array(data_converted)
final = final_Data.reshape((1, 10))
print(final)

#prediction de la classe des donnees
class_pred = model.predict(final)

print("the class is ",class_pred[0])
print("the result is  : ",ConvertClass(class_pred[0]))

