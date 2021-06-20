import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def generate_r(df):
    df['R'] = round((df['A']*df['B']*df['C']*df['D']*df['E']) / df['S'], 2)
    return df

def generate_random_df(amin, amax, bmin, bmax, cmin, cmax, dmin, dmax, emin, emax, smin, smax):
    random_list_a = []
    random_list_b = []
    random_list_c = []
    random_list_d = []
    random_list_e = []
    random_list_s = []
    for i in range(1, 10001):
        np.random.seed(i)
        rand_a = round(np.random.uniform(amin, amax), 2)
        rand_b = round(np.random.uniform(bmin, bmax), 2)
        rand_c = round(np.random.uniform(cmin, cmax), 2)
        rand_d = round(np.random.uniform(dmin, dmax), 2)
        rand_e = round(np.random.uniform(emin, emax), 2)
        rand_s = round(np.random.uniform(smin, smax), 2)
        random_list_a.append(rand_a)
        random_list_b.append(rand_b)
        random_list_c.append(rand_c)
        random_list_d.append(rand_d)
        random_list_e.append(rand_e)
        random_list_s.append(rand_s)
    # df = pd.DataFrame(random_list_a, columns=['A'])
    # df = pd.DataFrame(list(zip(random_list_a, random_list_b, random_list_c, random_list_d, random_list_e, random_list_s)),
        # columns =['A', 'B', 'C', 'D', 'E', 'S'])
    df = pd.DataFrame({'A': random_list_a, 'B': random_list_b, 'C': random_list_c, 'D': random_list_d, 'E': random_list_e,'S': random_list_s})
    
    df.to_csv('/home/agus/Codigo/Django/Xoxo/statistics/montecarlo/data/df_random.csv')
    return df

def percentile_99(df):
    return round(df.quantile(0.99), 2)

def percentile_90(df):
    return round(df.quantile(0.9), 2)

def percentile_50(df):
    return round(df.quantile(0.5), 2)

def percentile_10(df):
    return round(df.quantile(0.1), 2)

def df_mode(df):
    return round(df.mode(), 2)

def df_mean(df):
    return round(df.mean(), 2)

def df_median(df):
    return round(df.median(), 2)

def plot_histogram(df):
    histogram = sns.histplot(data=df, bins=5, kde=False, legend=True)
    return histogram
