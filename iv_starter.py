from __future__ import division
import pandas as pd
import numpy as np
import sys
from mfi_score_functions_v2 import *


data = pd.read_csv('input/data.csv')


data = data.loc[data[''] != , :] # exclude

data, ft_cols = prep_df_single(data, is_online = None)


# iv_table_full = pd.DataFrame(columns = ['', 'feature', 'min', 'x1', 'x2', 'max', 
                                        # 'good_qty_all', 'bad_qty_all',
                                        # 'bin0_bad_pcnt', 'bin0_good_pcnt',
                                        # 'bin1_bad_pcnt', 'bin1_good_pcnt',
                                        # 'bin2_bad_pcnt', 'bin2_good_pcnt',
                                        # 'bin0_woe', 'bin1_woe', 'bin2_woe',
                                        # 'bin0_iv', 'bin1_iv', 'bin2_iv',
                                        # 'iv_total', 'rank_by_iv'])


#num1 = int(sys.argv[1])
#num2= int(sys.argv[2])
dataset_list = ['train', 'valid', 'test']
n_combinations = len(dataset_list)*len(ft_cols)
while True:
    try:
        num1 = int(input('num1:'))
        num2 = int(input('num2:'))
        if num2 >= n_combinations:
            num2 = n_combinations - 1
        iii = 0        
        while (iii <= num2) and (0 <= num1 <= num2 < n_combinations):
            for dataset in dataset_list:
                for col in ft_cols:
                    if (iii >= num1) and (iii <= num2):
                        print('Iteration: {}'.format(iii))
                        iv_table = f_iv_v2(df = data, dataset = dataset, ft = col, y = 'target')
                        iv_table.to_csv('iv_table/iv_table_{}_{}.csv'.format(dataset, iii), index = None, sep = '\t')
                        iv_table.to_pickle('iv_table/iv_table_{}_{}.pkl'.format(dataset, iii))
                        iii += 1
                    else:
                        iii += 1
    except:
        pass    