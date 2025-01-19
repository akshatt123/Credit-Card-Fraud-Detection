# ***Credit-Card-Fraud-Detection***

A comprehensive system for detecting fraudulent credit card transactions leveraging machine learning models, advanced class imbalance handling techniques, and anomaly detection. This project demonstrates robust model performance on imbalanced datasets and incorporates modern machine learning pipelines for efficient processing.

## Features

* **Machine Learning Models:** Built and evaluated Random Forest, XGBoost, and SVM models.

* **Class Imbalance Handling:**

   * SMOTE (Synthetic Minority Over-sampling Technique).

   * Under-sampling techniques like NearMiss.

   * In-algorithm class weighting for Random Forest, XGBoost, and SVM.

* **Pipelining Concept:** Streamlined preprocessing and model training steps using Pipeline for modular and reusable workflows.

* **GridSearchCV for Hyperparameter Tuning:** (Commented in code) Provided flexibility for optimization though computationally intensive.

* **Stratified K-Fold Cross-Validation:** Ensured balanced splits of the dataset during training and evaluation.

* **Confusion Matrix Analysis:** Printed and analyzed confusion matrices to understand classification performance better.

* **Model Evaluation Metrics:** Used precision, recall, F1-score, and ROC-AUC for performance assessment.

## Class Imbalance Handling Approaches

**1. In-Algorithm Techniques**

 * Random Forest: Utilized class_weight='balanced' to assign higher weights to the minority class.

 * XGBoost: Adjusted scale_pos_weight to focus more on the fraudulent class.

 * SVM: Used class_weight='balanced' to make the model sensitive to the minority class.

**2. Under-Sampling Techniques**

 * NearMiss: Selected majority class samples close to the decision boundary.

 * Random Under-Sampling: Randomly removed majority class samples to achieve balance.


| Method | Description | Pros | Cons |
| ------ | ----------- | ---- | ---- |
| In-Algorithm Techniques. | Adjusts model weights for class imbalance. | Simple to implement. | May not work well on extreme imbalance. |
| Under-Sampling. | Reduces majority class samples. | Effective for large datasets. | Risk of losing important data.


## Dataset

The dataset used is the Credit Card Fraud Detection Dataset, containing anonymized features scaled for confidentiality. It includes highly imbalanced data with a small proportion of fraudulent transactions.

## Usage

**1. Preprocessing**

 * Split the dataset into training and test sets.

 * Scale features using StandardScaler.

 * Handle class imbalance using SMOTE, NearMiss, or in-algorithm techniques.

**2. Model Training**

 * Train the following models using pipelines:

    * Random Forest

    * XGBoost

    * SVM

**3. Model Evaluation**

 * Evaluate model performance using metrics such as:

    * ROC-AUC

    * Precision

    * Recall

    * F1-score

 * Analyze the Confusion Matrix to assess the classification accuracy for each class.

**4. Comparison: Stratified K-Fold vs Manual Holdout Evaluation**

 * Stratified K-Fold ensures that each fold maintains the same class distribution as the entire dataset, leading to more robust and consistent evaluation.

 * Manual Holdout Evaluation involves splitting the data into a single train-test set, which can result in performance variation depending on the split.

Stratified K-Fold is preferred when dealing with imbalanced datasets to reduce bias and variance in model evaluation.

**5. Hyperparameter Tuning (Optional)**

GridSearchCV can be applied for hyperparameter tuning, allowing for optimal parameter selection. While computationally intensive and too much time consuming, it can provide significant performance gains. 


## Results

* Achieved high detection accuracy and ROC-AUC scores with ensemble models like Random Forest,XGBoost and SVM.

* Imbalance handling techniques (e.g., SMOTE, class weighting) significantly improved model robustness.

* Confusion Matrix analysis revealed detailed insights into misclassification patterns.

## Future Work

* Experiment with deep learning models for fraud detection and try more optimizer to reduce time complexity.

* Optimize hyperparameters using advanced techniques like Bayesian Optimization.

* Deploy the model as a REST API for real-time fraud detection.

## Contribute

Feel free to contribute if you better and more optimized model, by creating a pull request or opening an issue for improvements or suggestions!

## License

This project is licensed under the MIT License. See the LICENSE file for details.


