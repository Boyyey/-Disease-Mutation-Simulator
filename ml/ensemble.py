import numpy as np
from ml.random_forest import RandomForestMutationModel
from ml.xgboost_model import XGBoostMutationModel
from ml.transformer import SequenceTransformer

class EnsembleMutationPredictor:
    """Combines multiple mutation prediction models for robust predictions."""
    def __init__(self, rf_path=None, xgb_path=None, transformer_path=None):
        self.rf = RandomForestMutationModel(rf_path)
        self.xgb = XGBoostMutationModel(xgb_path)
        self.transformer = SequenceTransformer(transformer_path)
        self.weights = [1/3, 1/3, 1/3]  # Default equal weights
    def predict(self, features, sequence):
        preds = []
        preds.append(self.rf.predict(features))
        preds.append(self.xgb.predict(features))
        preds.append(np.array(self.transformer.predict(sequence)))
        # Weighted average
        combined = sum(w*p for w, p in zip(self.weights, preds))
        return combined / sum(self.weights)
    def set_weights(self, weights):
        assert len(weights) == 3
        self.weights = weights
    def train(self, X, y):
        # TODO: Train all models and optimize weights
        pass 