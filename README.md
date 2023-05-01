# kavach_project
Citizen safety app for protection against cyber crimes



What is Malicious Website? A malicious website is a site that attempts to install malware (a general term for anything that will disrupt computer operation, gather your personal information or, in a worst-case scenario, gain total access to your machine) onto your device. This usually requires some action on your part, however, in the case of a drive-by download, the website will attempt to install software on your computer without asking for permission first.


# Introduction:
As the number of online users continues to increase, so does the number of malicious websites. These websites can contain harmful content, such as viruses and malware, and can pose a significant threat to users' privacy and security. 
The objective of this project is to develop an app to flag malicious/fraud indicators in real-time, including mobile numbers, SMS headers, URL links, UPI addresses and SMS templates. In this particular study, the focus was on detecting malicious websites using a 1D Convolutional Neural Network (CNN) algorithm.

# Dataset:
The dataset used in this study contains 420,464 website URLs and their corresponding labels (i.e., whether they are malicious or not). The dataset was split into training and testing sets using the holdout method, with 80% of the data used for training and the remaining 20% used for testing.

# Method:


The 1D CNN model used in this study consists of an input layer for the website URL, followed by an embedding layer, two convolutional layers with 64 filters each, and a concatenation layer.
 The model also has three input layers for the subdomain, domain, and domain suffix, respectively, each followed by an embedding layer. 
The output of the concatenation layer and the three embedding layers were then concatenated and fed into a dropout layer, followed by two dense layers.
Finally, the output layer with a sigmoid activation function was used to classify the website as malicious or not.
The model was trained on the training set using binary cross-entropy loss and Adam optimization with a learning rate of 0.001. The model was trained for 10 epochs with a batch size of 64.

# Results:
The model achieved an accuracy of 97.2% on the test set, indicating its effectiveness in detecting malicious websites. The model architecture had a total of 3,809,329 parameters, all of which were trainable.

# Conclusion:
The 1D CNN model used in this study is a promising approach for detecting malicious websites in real-time. The high accuracy achieved in this study indicates that the model can effectively identify malicious websites and can be used as a component of the larger app designed to flag various fraud indicators in real-time.
# View of app
## Home screen
<img width="152" alt="image" src="https://user-images.githubusercontent.com/93816049/233513163-e381ce23-e4dd-45d2-a1a4-70350e1bf354.png">

## URL check page
<img width="152" alt="image" src="https://user-images.githubusercontent.com/93816049/233512805-3fbf228f-85b5-4a68-911f-7fd26ba955a1.png">

## Live map page
<img width="151" alt="image" src="https://user-images.githubusercontent.com/93816049/233512921-e5356d48-888c-49ac-9395-3ed04bc2272b.png">

## Reporting page
<img width="148" alt="image" src="https://user-images.githubusercontent.com/93816049/233513618-79523bfd-05fc-44d4-83c4-5d57e8505560.png">

## Profile Page
<img width="146" alt="image" src="https://user-images.githubusercontent.com/93816049/233513311-533c06a9-7a34-4df5-ad11-88bf1a397ec9.png">

## Flask Website
![WhatsApp Image 2023-04-13 at 11 40 35 PM](https://user-images.githubusercontent.com/93816049/235405460-9a9577ba-a4dc-4ea9-968f-e0b193e0b3ce.jpeg)

## API Testing
Following api will be called in app. The respond the ULR class.(BAD CLASS)
![WhatsApp Image 2023-04-13 at 11 43 27 PM](https://user-images.githubusercontent.com/93816049/235405718-746a944e-c161-4037-83ad-e05489a29de2.jpeg)
(GOOD CLASS)
![WhatsApp Image 2023-04-13 at 11 41 10 PM](https://user-images.githubusercontent.com/93816049/235405764-e25afc27-b503-49c9-b71a-4526ec01ee75.jpeg)

