## Intro to Machine Learning
 
- ML is the process of *training* a piece of software, called a *model*, to make useful predictions from data.

+ **Training**: The process of determining the ideal parameters (weight and bias) comprising a model. DUring training, the system reads in examples and gradually adjusts parameters. 
+ **Model**: A mathematical contruct that processes input data and returns output. Or, a model is a set of parameters and structure needed for a system to make predictions. 
    + A linear regression model consists of a set of weights (A value that a model multiplies by another value) and biases
    + A neural network model consists of:
        * A set of hidden layers, each containing neurons
        * The W and B associated with each neuron.
    + A decision tree model 
        * The shape of the tree
        * The condition and leaves
> Example: Create an app to predict the rainfall

-> Physics approach: Create physics based representation of the earth's atmosphere and surface. Computing massive ammount of fluid dynamics equations. 

-> ML approach: Give a ML model enormous ammount of weather data until the data learns the mathematical relationship between weather patterns that produce different ammounts of rain. Then give current weather data and predict rain. 

### Types of ML systems

+ Supervised learning 
    - Training a model from features and their corresponding labels. Supervised ML is analogous to learning a subject by studying a set of questions and their answers. Master mapping between Q/A and provide answers to never-before-seen questions on the same topic. 
    - Models make prediction after going thru alot of data with correct answers. Then discover the connections b/w the elements in the data that produce the same answer. 
    - Two of the most common use cases of supervised learning are:
        #### Regression
        - A regression model predicts a numeric value. A model that takes an input and predicts a numerical output.
            - Input: information about a house such as square footage, zip code, num of bedrooms, lot size, mortage interest rate...etc.
            - Output: The price of a house.
        #### Classification 
        - A classification model predicts the probability of something belonging to a category. Example: food classification, input a picture of food item and get the category it belongs to. 
            ###### Binary classification
            - Outputs a value from a class that contains a binary output (True or False)
            ###### Multiclass classification 
            - Outputs a value from a class that contains multiple outputs (Blue, Red, Yellow, or Green)       

+ Unsupervised learning 
    - Unsupervised learning models make predictions from datasets with no correct answers. The goal of the models is to identify and predict meaningful patterns.
    - Unsupervised learning models employ a technique called clustering. 

+ Reinforcement learning
    - Reinforcement learning models make predictions by getting rewards or penalties based on actions performed. The models generate a policy that defines the best strategy to get the most rewards. 

### Training and loss

+ Training
    - A model means learning/determining the good values for all weights and the bias from labeled examples. 
    - A ML model algorithm builds a model by examining many examples and attempting to find a model minimized loss => **empirical risk minimization**
    
+ Loss
    - The penalty for bad prediction. It is a number indicating how bad the model's prediction was on a single example. 
    - If the model's prediction is perfect, the loss is zero, else the loss is greater. 
    - #### Squared loss
        - Squared loss or L<sub>2</sub> loss
        - The square of difference between label and prediction. 
    - #### Mean squared loss (MSE)
        - The average squared loss per example over the whole dataset. 
        - `MSE = 1/N * SUM(y-prediction(x)^2)`

### Reducing loss 
    - Hyperparamters: config settings used to tune how a model is trained.
    - Derivative of `(y-y')^2` with respect to weights and biases tells us how loss changes for a given example.
        
```
Notes of material taught by Google: https://developers.google.com/machine-learning/intro-to-ml
```
