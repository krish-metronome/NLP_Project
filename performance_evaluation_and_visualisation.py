from sklearn import metrics
import matplotlib.pyplot as plt
import seaborn as sns

def evaluatePerformance(predictedLabels, manualLabels):
    print(metrics.classification_report(manualLabels, predictedLabels))

def visualisePerformanceUsingBarPlots(predictedLabels, manualLabels):
    report = metrics.classification_report(manualLabels, predictedLabels, output_dict=True)
    
    # Extract precision, recall, and F1-score values for each class
    precision_metrics = {label: report[label]['precision'] for label in report.keys() if label not in ['accuracy', 'macro avg', 'weighted avg']}
    recall_metrics = {label: report[label]['recall'] for label in report.keys() if label not in ['accuracy', 'macro avg', 'weighted avg']}
    f1_metrics = {label: report[label]['f1-score'] for label in report.keys() if label not in ['accuracy', 'macro avg', 'weighted avg']}
    
    # Plot bar plots for precision, recall, and F1-score
    fig, axes = plt.subplots(3, 1, figsize=(10, 18))
    
    # Precision bar plot
    sns.barplot(x=list(precision_metrics.keys()), y=list(precision_metrics.values()), palette='YlGnBu', ax=axes[0])
    axes[0].set_title('Precision for Each Class')
    axes[0].set_xlabel('Class')
    axes[0].set_ylabel('Precision')
    
    # Recall bar plot
    sns.barplot(x=list(recall_metrics.keys()), y=list(recall_metrics.values()), palette='YlGnBu', ax=axes[1])
    axes[1].set_title('Recall for Each Class')
    axes[1].set_xlabel('Class')
    axes[1].set_ylabel('Recall')
    
    # F1-score bar plot
    sns.barplot(x=list(f1_metrics.keys()), y=list(f1_metrics.values()), palette='YlGnBu', ax=axes[2])
    axes[2].set_title('F1-Score for Each Class')
    axes[2].set_xlabel('Class')
    axes[2].set_ylabel('F1-Score')
    
    plt.tight_layout()
    plt.show()

def visualisePerformanceUsingConfusionMatrix(predictedLabels, manualLabels):
    confusion_matrix = metrics.confusion_matrix(manualLabels, predictedLabels)
    plt.figure(figsize=(8, 6))
    sns.heatmap(confusion_matrix, annot=True, fmt='d', cmap='YlGnBu', xticklabels=sorted(set(manualLabels)), yticklabels=sorted(set(manualLabels)))
    plt.title('Confusion Matrix')
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.show()
