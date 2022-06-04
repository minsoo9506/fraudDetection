from typing import List, Optional, Tuple

import numpy as np
import pandas as pd
from pydantic import BaseModel, ValidationError

# from fraud_detection_model.config.core import config


def validate_inputs(*, input_data: pd.DataFrame) -> Tuple[pd.DataFrame, Optional[dict]]:
    """validate inputs

    Parameters
    ----------
    input_data : pd.DataFrame
        raw input data

    Returns
    -------
    Tuple[pd.DataFrame, Optional[dict]]
        after preprocessing, check input data with pydantic
    """

    # 여기서 필요한 preprocessing 을 하고 진행 ex) rename, fillna 등등

    errors = None

    try:
        # pydantic을 위해 np.nan을 None으로 바꿈
        MultipleInputs(
            inputs=input_data.replace({np.nan: None}).to_dict(orient="records")
        )
    except ValidationError as error:
        errors = error.json()

    return input_data, errors


class InputSchema(BaseModel):
    """input data schema config

    Parameters
    ----------
    BaseModel : _type_
        _description_
    """

    Time: Optional[float]
    V1: Optional[float]
    V2: Optional[float]
    V3: Optional[float]
    V4: Optional[float]
    V5: Optional[float]
    V6: Optional[float]
    V7: Optional[float]
    V8: Optional[float]
    V9: Optional[float]
    V10: Optional[float]
    V11: Optional[float]
    V12: Optional[float]
    V13: Optional[float]
    V14: Optional[float]
    V15: Optional[float]
    V16: Optional[float]
    V17: Optional[float]
    V18: Optional[float]
    V19: Optional[float]
    V20: Optional[float]
    V21: Optional[float]
    V22: Optional[float]
    V23: Optional[float]
    V24: Optional[float]
    V25: Optional[float]
    V26: Optional[float]
    V27: Optional[float]
    V28: Optional[float]
    Amount: Optional[float]


class MultipleInputs(BaseModel):
    """master input schema config

    Parameters
    ----------
    BaseModel : _type_
        _description_
    """

    inputs: List[InputSchema]
