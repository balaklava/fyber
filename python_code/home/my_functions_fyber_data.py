import pandas as pd

def max_values_per_feature(df_selectby_click, feature_name, length):
    df_selectby_click_featureHist = df_selectby_click.loc[:,feature_name].value_counts()
    df_selectby_click_featureHist_sort = df_selectby_click_featureHist.sort_values(ascending=False)
    df_selectby_click_featureHist_maxN = df_selectby_click_featureHist_sort.iloc[:length]      
    return df_selectby_click_featureHist_maxN
        

def regrouped_df(df_grouped):
    features_arr = []
    N_arr = []
    for feature in df_grouped.groups: 
        features_arr.append(feature)
        N_arr.append(len(df_grouped.groups[feature]))
    df_features_Hist = pd.DataFrame({'Feature':features_arr, 'N':N_arr})
    
    return df_features_Hist