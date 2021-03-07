The following project placed 2nd place at the annual 24 hour UMW Hackathon 2021 
[code formatting is reflective of time constraints]

Collected the data and trained the model for the following models;

1) Eagle: NonEagle(other birds) classifier
  -Reached a reported accuracy of roughly 91%
2) Head CT Scan(control:necrosis:tumor) classifier
  -Reached a reported accuracy of 32% using a data set of roughly 80 images curated from the internet
  -Includes a data upload and relabeling functionality that then generates a new model for continued model training
  
The Goal Of The Project:

The Eagle classifier is a proof of concept of how good a classifier can be generated from a personal data set and trainined over just a few layers

The Head CT Scan notebook is meant to function as a tool for radiologist and researchers who have a limited amount of data and will be manually labeling their data as they progress through their research.

Main libraries:
Tensorflow
Keras 
Numpy
fastai
pickle

References:
1)https://www.youtube.com/watch?v=j-3vuBynnOE&list=LL&index=3
2)https://www.youtube.com/watch?v=WvoLTXIjBYU&list=LL&index=4&t=937s
3)https://www.youtube.com/watch?v=iGWbqhdjf2s
4)https://keras.io/examples/vision/image_classification_from_scratch/
