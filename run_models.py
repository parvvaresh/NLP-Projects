from models.train_models import train_models
import pandas as pd
from PreProcess import PreProcess

def main():
    df = pd.read_csv("./data/Snappfood.csv").head(10000)
    result = train_models(df, PreProcess)
    result.to_csv("./assets/result.csv")
    print(f"result saved in <<./assets/result.csv>>")
    

main()