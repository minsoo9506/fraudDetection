# import math
import numpy as np

from fraud_detection_model.predict import make_prediction


def test_make_prediction(input_data):
    expected_first_prediction_value = 0
    expected_num_predictions = 71202

    result = make_prediction(input_data=input_data)

    predictions = result.get("predictions")
    assert isinstance(predictions, np.ndarray)
    assert isinstance(predictions[0], np.int64)

    assert result.get("errors") is None
    assert len(predictions) == expected_num_predictions
    assert predictions[0] == expected_first_prediction_value
    # assert math.isclose(predictions[0], expected_first_prediction_value, abs_tol=0.1)
