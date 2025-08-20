========================= RESTART: C:/backup/TITANIC.py ========================
Initial Dataset Preview:
    Survived  Pclass  ... Parents/Children Aboard     Fare
0         0       3  ...                       0   7.2500
1         1       1  ...                       0  71.2833
2         1       3  ...                       0   7.9250
3         1       1  ...                       0  53.1000
4         0       3  ...                       0   8.0500

[5 rows x 8 columns]

Dataset Info:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 887 entries, 0 to 886
Data columns (total 8 columns):
 #   Column                   Non-Null Count  Dtype  
---  ------                   --------------  -----  
 0   Survived                 887 non-null    int64  
 1   Pclass                   887 non-null    int64  
 2   Name                     887 non-null    object 
 3   Sex                      887 non-null    object 
 4   Age                      887 non-null    float64
 5   Siblings/Spouses Aboard  887 non-null    int64  
 6   Parents/Children Aboard  887 non-null    int64  
 7   Fare                     887 non-null    float64
dtypes: float64(2), int64(4), object(2)
memory usage: 55.6+ KB
None

Statistical Summary:
         Survived      Pclass  ...  Parents/Children Aboard       Fare
count  887.000000  887.000000  ...               887.000000  887.00000
mean     0.385569    2.305524  ...                 0.383315   32.30542
std      0.487004    0.836662  ...                 0.807466   49.78204
min      0.000000    1.000000  ...                 0.000000    0.00000
25%      0.000000    2.000000  ...                 0.000000    7.92500
50%      0.000000    3.000000  ...                 0.000000   14.45420
75%      1.000000    3.000000  ...                 0.000000   31.13750
max      1.000000    3.000000  ...                 6.000000  512.32920

[8 rows x 6 columns]

Missing Values Count:
Survived                   0
Pclass                     0
Name                       0
Sex                        0
Age                        0
Siblings/Spouses Aboard    0
Parents/Children Aboard    0
Fare                       0
dtype: int64

Missing Values After Cleanup:
Survived                   0
Pclass                     0
Name                       0
Sex                        0
Age                        0
Siblings/Spouses Aboard    0
Parents/Children Aboard    0
Fare                       0
dtype: int64

Crosstab - Survival by Sex:
Survived         0         1
Sex                         
female    0.257962  0.742038
male      0.809773  0.190227

Crosstab - Survival by Pclass:
Survived         0         1
Pclass                      
1         0.370370  0.629630
2         0.527174  0.472826
3         0.755647  0.244353

EDA Completed.
