# Supervised learning
- Supervised learning depends on datasets with labeled classes. 
- Tasks are well-defined and has more potential use cases. 
## Learning concepts

### Data
    - The driving force of any model in ML. Usually in the form of words and numbers stored in tables and dictionaries.
    - Datasets are made up of individual examples that contain features(input variable) and a label (output or result to feature).
    - A dataset is characterized by its size and diveristy where the size refers to the number of examples and diversity refers to the range of examples. 

### Model
    - A model is a complex collection of numbers that define the mathematical relationship from input variables to result an output. 

### Training
    - A model is trained before being deployed for use. To train a model, we provide a dataset with labeled examples. The model     then works out the best solution for predicting the labels from its features. 
    - The model finds the best solution by comparing its predicted value to the labels' actual value. The delta between the values is the loss. 

### Evaluating
    - Evaluate a trained model to determine how well it learned. During evaluation, we use a labeled dataset, but give the model only the datasets features. We then compare the model's predictions to the label's true values. 
 
### Inference
    -  Once we are satisfied with evaluating a model, we can use it to make predictions on unlabeled examples. 