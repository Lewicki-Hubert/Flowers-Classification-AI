# K-Nearest Neighbors Classifier
This project implements a simple K-Nearest Neighbors (KNN) classifier in Python. The KNN algorithm is a type of instance-based learning, or lazy learning, where the function is only approximated locally and all computation is deferred until function evaluation. It can be used for classification and regression problems, but this project focuses on classification, specifically designed to work with datasets formatted similarly to the Iris dataset.

# Features
Data Loading: Load your dataset from a file. The expected format is space-separated values, with the last column being the class label.
<br />Euclidean Distance Calculation: Compute the Euclidean distance between two data points.
<br />Neighbor Identification: For a given test instance, identify the k nearest neighbors in the training dataset.
<br />Majority Vote Classification: Classify the test instance based on the majority class among its k nearest neighbors. In the event of a tie, the nearest neighbor among the tied groups is chosen.
<br />Accuracy Evaluation: Evaluate the classification accuracy of the model on a test dataset.
<br />Interactive User Interface: Allows the user to either classify a test dataset or input individual data points for classification.

# Technologies
Python 3
<br />Math module for mathematical operations

# Running the Classifier
Ensure you have Python 3.x installed on your system. To run the classifier, follow these steps:
<br />Clone the repository or download the source code.
<br />Navigate to the directory containing the source code.
<br />Execute the script using the command: python knn_classifier.py (replace knn_classifier.py with the actual script name).

For classifying individual data points, enter the attribute values separated by spaces.
# Using the Classifier
The interactive user interface prompts you for:
<br />The path to the training dataset.
<br />The value of k (the number of neighbors to consider).
<br />The choice between classifying a test set or entering an individual data point.
<br />For classifying individual data points, enter the attribute values separated by spaces.

# Dataset Format
The dataset should be in a plain text file with each instance on a new line. Attributes should be space-separated, with the last attribute being the class label. This format is similar to the Iris dataset but can be adapted for use with other datasets.
