from sklearn.metrics import roc_auc_score, precision_recall_curve, auc, roc_curve
from typing import Any
import matplotlib.pyplot as plt
import numpy as np

# model result anlaysis


def print_metrics(y_true: Any, pred_prob: Any) -> None:
    """print ROCAUC, PRAUC score

    Parameters
    ----------
    y_true : Any
        true label (0 or 1)
    pred_prob : Any
        should be 1D, prediction probability for label 1
    """
    roc_auc = roc_auc_score(y_true, pred_prob)
    precision, recall, _ = precision_recall_curve(y_true, pred_prob)
    pr_auc = auc(recall, precision)

    print(f"ROCAUC = {roc_auc:.3f}")
    print(f"PRAUC = {pr_auc:.3f}")


def plot_roc_curve(y_true: Any, pred_prob: Any, model_name: str = "your model") -> None:
    """plot roc curve

    Parameters
    ----------
    y_true : Any
        true label (0 or 1)
    pred_prob : Any
        should be 1D, prediction probability for label 1
    model_name : str, optional
        model name, by default 'your model'
    """
    # random classification
    plt.plot(np.arange(0, 1.1, 0.1), np.arange(0, 1.1, 0.1), linestyle="--", label="No Skill")
    # your prediction
    fpr, tpr, _ = roc_curve(y_true, pred_prob)
    plt.plot(fpr, tpr, marker=".", label=model_name)
    plt.xlabel("FPR")
    plt.ylabel("TPR")
    plt.legend()
    plt.title(f"{model_name} ROC CURVE")
    plt.show()


def plot_pr_curve(y_true: Any, pred_prob: Any, model_name: str = "your model") -> None:
    """plot pr curve

    Parameters
    ----------
    y_true : Any
        true label (0 or 1)
    pred_prob : Any
        should be 1D, prediction probability for label 1
    model_name : str, optional
        model name, by default 'your model'
    """
    # random classification
    random_clf = np.sum(y_true) / len(y_true)
    plt.plot([0, 1], [random_clf, random_clf], linestyle="--", label="No Skill")
    # your prediction
    precision, recall, _ = precision_recall_curve(y_true, pred_prob)
    plt.plot(recall, precision, marker=".", label=model_name)
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.legend()
    plt.title(f"{model_name} PR CURVE")
    plt.show()


def threshold_tuning_f1_score_plot(y_true: Any, pred_prob: Any) -> None:
    """show f1 score changing threshold

    Parameters
    ----------
    y_true : Any
        true label (0 or 1)
    pred_prob : Any
        should be 1D, prediction probability for label 1
    """
    precision, recall, threshold = precision_recall_curve(y_true, pred_prob)
    f1_score = 2 * precision * recall / (precision + recall)
    length = min(len(precision), len(recall), len(threshold))
    max_idx = np.where(f1_score == max(f1_score))
    plt.plot(threshold[:length], f1_score[:length])
    plt.scatter(threshold[max_idx], f1_score[max_idx], c="r")
    plt.xlabel("Threshold")
    plt.ylabel("F1 Score")
    plt.title("Threshold Tuning F1 Score Curve")
    plt.show()
