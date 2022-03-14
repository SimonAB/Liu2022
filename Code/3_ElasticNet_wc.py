# ---
# title: "BBSRC_ARC ElasticNet"
# author: "Simon Babayan"
# ---

#%% Import packages
import numpy as np
import pandas as pd

from sklearn.model_selection import RepeatedKFold
from sklearn.metrics import mean_squared_error, r2_score

from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import ElasticNetCV

import seaborn as sns
sns.set(context="paper",
        style="whitegrid",
        palette="deep",
        font_scale=1.4,
        color_codes=True,
        rc=None)



#########################################################################
#%% Iterate over every week
# data prep
## Import response variable
df_wc = pd.read_excel('~/Dropbox/sheep_arc/data/read_in/Complete data set Tcirc AHRC 010617.xlsx', index_col="Animal_ID")

df_wc.rename(index=lambda x: 'sheep_'+str(x), inplace=True)
df_wc.head()

eigenweeks = {
    "Week1": "./eigengenes_clusters_g1g3_Week1.csv",
    "Week2": "./eigengenes_clusters_g1g3_Week2.csv",
    "Week3": "./eigengenes_clusters_g1g3_Week3.csv",
    "Week4": "./eigengenes_clusters_g1g3_Week4.csv",
    "Week5": "./eigengenes_clusters_g1g3_Week5.csv",
    "Week7": "./eigengenes_clusters_g1g3_Week7.csv"
    }

# cross validation
seed = 4 # to ensure reproducibility during setup
num_splits = 5
num_repeats = 4

# base algorithm settings
regressor = ElasticNetCV(l1_ratio=[.1, .5, .7, .9, .95, .99, 1],
                         eps=0.001,
                         n_alphas=100,
                         alphas=None,
                         fit_intercept=True,
                         normalize=False,
                         precompute="auto",
                         max_iter=10000,
                         tol=0.0001,
                         cv=num_splits,
                         copy_X=True,
                         verbose=1,
                         n_jobs=-1,
                         positive=False,
                         random_state=seed,
                         selection="cyclic")

# repeated random stratified splitting of dataset
rkf = RepeatedKFold(n_splits=num_splits,n_repeats=num_repeats, random_state=seed)

for week, file in eigenweeks.items():

    df_eigen = pd.read_csv(file, sep = ",", index_col = ["Unnamed: 0"])
    df_eigen.rename(index = lambda x: 'sheep_' + x.split('g')[0], inplace=True)
    df_eigen.index.names = ["Animal.ID"]

    # merge wc with culters on sample ID
    df_wc_eigen = df_wc[["Total_Worms"]].join(df_eigen, how='outer')
    print(df_wc_eigen.head())

    # data prep
    df = df_wc_eigen.copy()
    df = df.fillna(0)

    # define labels and features
    y = np.log10(1+df["Total_Worms"])
    X = df.iloc[:,1:-1]
    X[X.columns] = StandardScaler().fit_transform(X[X.columns].values)

    # prepare matrices of results
    rkf_coef = pd.DataFrame(columns=["cluster", "coef"]).set_index("cluster")
    rkf_coef.loc["r2"] = ""
    rkf_intercept = pd.DataFrame(columns=["cluster", "intercept"]).set_index("cluster")
    rkf_intercept.loc["r2"] = ""

    for train_index, test_index in rkf.split(X, y):
        X_train, X_test = X.values[train_index], X.values[test_index]
        y_train, y_test = y[train_index], y[test_index]
        #fit model
        regressor.fit(X_train, y_train);
        # test model
        y_pred = regressor.predict(X_test)
        r2 = r2_score(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        coef_table = pd.DataFrame(
            {"coef": regressor.coef_, "cluster": X.columns}).set_index("cluster")
        coef_table.loc["r2"] = r2
        coef_table.loc["mse"] = mse
        intercept_table = pd.DataFrame(
            {"intercept": regressor.intercept_, "cluster": X.columns}).set_index("cluster")
        intercept_table.loc["r2"] = r2
        intercept_table.loc["mse"] = mse
        # combine outputs
        rkf_coef = pd.merge(rkf_coef, coef_table, left_index=True,
                            right_index=True, how='outer')
        rkf_intercept = pd.merge(
            rkf_intercept, intercept_table, left_index=True, right_index=True, how='outer')

    # Results
    rkf_coef.dropna(axis=1, inplace=True)
    rkf_coef["coef mean"] = rkf_coef.mean(axis=1)
    rkf_coef["coef sem"] = rkf_coef.sem(axis=1)
    rkf_coef.to_csv("./enet_wc_repeatedCV_coef_{0}.csv".format(week))
    rkf_intercept.dropna(axis=1, inplace=True)
    rkf_intercept["intercept mean"] = rkf_intercept.mean(axis=1)
    rkf_intercept["intercept sem"] = rkf_intercept.sem(axis=1)
    rkf_intercept.to_csv("./enet_wc_repeatedCV_intercept_{0}.csv".format(week))
