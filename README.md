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
+ Unsupervised learning 
+ Reinforcement learning