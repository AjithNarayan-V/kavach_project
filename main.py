from flask import Flask,request,jsonify
import pickle
import numpy as np
import pandas as pd
import json
# !pip install tldextract -q
import tldextract
from tensorflow.keras.preprocessing.sequence import pad_sequences
import tensorflow as tf
model = tf.keras.models.load_model("model.h5")
app=Flask(__name__)
@app.route('/')
def home():
    return "hellow World"

@app.route('/predict',methods=['POST'])
def predict():  
    input_url=request.form.get('url')
    # input_url = ['ip-23-229-147-12.ip.secureserver.net/public/fi']
    url_data = pd.DataFrame([input_url], columns=['url'])
    url_data = extract_url(url_data)
    import pickle
    with open('tokenizer.pkl', 'rb') as f:
        tokenizer = pickle.load(f)
    input_seq = tokenizer.texts_to_sequences(url_data['url'])
    # print("After tokenizing URL:",input_seq)
    # print("typeAfterTOkennize_inputSeq:",type(input_seq))
    input_seq = pad_sequences(input_seq, maxlen=161, padding='post')
    # print("After Padding",input_seq)
    # print("typeAfterpadding_inputSeq:",type(input_seq))

    for feature in ['subdomain']:
        label_index = pd.read_csv("columns/label_index_subdomain.csv", index_col=0, header=None).squeeze("columns").to_dict()
        val=url_data.loc[:, feature]
        print("val",val)
        url_data.loc[:, feature] = [label_index[val] if val in label_index else label_index['<unknown>'] for val in url_data.loc[:, feature]]

    for feature in ['domain']:
        label_index = pd.read_csv("columns/label_index_domain.csv", index_col=0, header=None).squeeze("columns").to_dict()
        val=url_data.loc[:, feature]
        print("val",val)
        url_data.loc[:, feature] = [label_index[val] if val in label_index else label_index['<unknown>'] for val in url_data.loc[:, feature]]
    
    for feature in ['domain_suffix']:
        label_index = pd.read_csv("columns/label_index_domain_suffix.csv", index_col=0, header=None).squeeze("columns").to_dict()
        val=url_data.loc[:, feature]
        print("val",val)
        url_data.loc[:, feature] = [label_index[val] if val in label_index else label_index['<unknown>'] for val in url_data.loc[:, feature]]
    
    print("URL_DATA_AFTER_ALLPROCESS:",url_data)
    url_predict= [input_seq, url_data['subdomain'].astype('int64'), url_data['domain'].astype('int64'), url_data['domain_suffix'].astype('int64')]
    print("url_predict",[url_predict])
    from tensorflow.keras.models import load_model
    model = load_model('model.h5')
    val_pred = model.predict([url_predict])
    val_pred = np.where(val_pred[:, 0] >= 0.5, 1, 0)
    print("RESULT:",val_pred)
    if(val_pred==0):
         result="GOOD"
    elif(val_pred==1):
         result="BAD"
    else:
         result="error with input"
    # print("url_data:",url_data)
    # json_string = url_data.to_json(orient='records')
    # response = jsonify(json.loads(json_string))
    # response.headers.add('Access-Control-Allow-Origin', '*')
    dict={"result":result}
    return dict
   
def parsed_url(url):
        # extract subdomain, domain, and domain suffix from url
        # if item == '', fill with '<empty>'
        subdomain, domain, domain_suffix = ('<empty>' if extracted == '' else extracted for extracted in tldextract.extract(url))
        return [subdomain, domain, domain_suffix]

def extract_url(data):
        # pass the parsed_url(url) as a for loop and create new columns.  Create new df with results
        extract_url_data = [parsed_url(url) for url in data['url']]
        extract_url_data = pd.DataFrame(extract_url_data, columns=['subdomain', 'domain', 'domain_suffix'])
        
        # concat extracted feature with main data
        data = data.reset_index(drop=True)
        data = pd.concat([data, extract_url_data], axis=1)
        
        return data
if __name__=='__main__':  
    app.run(debug=True)  