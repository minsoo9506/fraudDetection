from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

from fraud_detection_model.config.core import config

fraud_detection_model_pipe = Pipeline(
    [
        (
            "SMOTE",
            SMOTE(
                sampling_strategy=config.model_config.sampling_strategy,
                random_state=config.model_config.random_state,
            ),
        ),
        ("model", LogisticRegression(random_state=config.model_config.random_state)),
    ]
)
