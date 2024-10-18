from PreProcess import PreProcess
import pickle
import warnings
warnings.filterwarnings("ignore")

with open('./final_models/svc_model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('./final_models/tfidf_vectorizer.pkl', 'rb') as file:
    tfidf_vectorizer = pickle.load(file)

with open('./final_models/select_k_best_transformer.pkl', 'rb') as file:
    select_k_best_transformer = pickle.load(file)
    
    

def pipeline_predict(text : str) -> str:
    pre_process_model = PreProcess()
    text_preproces = pre_process_model.pipeline(text)
    text_preproces = [" ".join(tokens) for tokens in text_preproces]
    
    matrix = tfidf_vectorizer.transform(text_preproces)
    matrix = select_k_best_transformer.transform(matrix).toarray()
    lable = model.predict(matrix)[0]
    print(lable)
    return lable
    
