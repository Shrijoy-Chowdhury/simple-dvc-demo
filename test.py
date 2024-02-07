import pandas as pd
import argparse
from src.get_data import read_params
from sklearn.model_selection import train_test_split

def load(config_path):
    config=read_params(config_path)
    print(config) 
    train_path=config["split_data"]["train_path"]
    test_path=config["split_data"]["test_path"]
    raw_data=config["load_data"]["raw_dataset_csv"]
    random_state=config["base"]["random_state"]
    split_ratio=config["split_data"]["test_size"]
    df=pd.read_csv(raw_data,sep=",")
    train,test=train_test_split(df,test_size=split_ratio,random_state=random_state)
    train.to_csv(train_path,index=False)    
    test.to_csv(test_path,index=False)
    
if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args=args.parse_args()
    data=load(config_path=parsed_args.config)