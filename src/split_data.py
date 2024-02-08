# split raw data
# save it in processed folder
import pandas as pd
import argparse
import os
from sklearn.model_selection import train_test_split
from get_data import read_params

def split_and_save_data(config_path):
    config=read_params(config_path)
    test_data_path=config["split_data"]["test_path"]
    train_data_path=config["split_data"]["train_path"]
    random_state=config["base"]["random_state"]
    split_ratio=config["split_data"]["test_size"]
    raw_data_path=config["load_data"]["raw_dataset_csv"]
    # print(config)
    df=pd.read_csv(raw_data_path,sep=",")
    train,test=train_test_split(df,test_size=split_ratio,random_state=random_state)
    train.to_csv(train_data_path,index=False)
    test.to_csv(test_data_path,index=False)
    # print(test.head())

if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args=args.parse_args()
    data = split_and_save_data(config_path=parsed_args.config)
