from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, mean_squared_error, r2_score

class MutationModelMetrics:
    """Provides metrics for evaluating mutation prediction models."""
    @staticmethod
    def classification_metrics(y_true, y_pred, threshold=0.5):
        y_bin = (y_pred > threshold).astype(int)
        return {
            'accuracy': accuracy_score(y_true, y_bin),
            'precision': precision_score(y_true, y_bin),
            'recall': recall_score(y_true, y_bin),
            'f1': f1_score(y_true, y_bin),
            'roc_auc': roc_auc_score(y_true, y_pred)
        }
    @staticmethod
    def regression_metrics(y_true, y_pred):
        return {
            'mse': mean_squared_error(y_true, y_pred),
            'r2': r2_score(y_true, y_pred)
        } 