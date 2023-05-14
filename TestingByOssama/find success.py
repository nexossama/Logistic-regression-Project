import pandas as pd

data = pd.read_csv('../student-mat.csv', sep=';')

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


