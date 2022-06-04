from pathlib import Path
from typing import List

import joblib
import pandas as pd
from imblearn.pipeline import Pipeline

from fraud_detection_model import __version__ as _version
from fraud_detection_model.config.core import DATASET_DIR, TRAINED_MODEL_DIR, config


# 아래 함수 인자에 *는 함수를 사용할 떄, 뒤에 나오는 file_name= 을 꼭 쓰게 강제한다
def load_dataset(*, file_name: str) -> pd.DataFrame:
    """load dataset

    Parameters
    ----------
    file_name : str
        name of data to read_csv

    Returns
    -------
    pd.DataFrame
        dataset loaded with name 'file_name'
    """
    df = pd.read_csv(Path(f"{DATASET_DIR}/{file_name}"))
    # 간단하게 transform할 내용있으면 여기서 진행
    return df


def save_pipeline(*, pipeline_to_save: Pipeline) -> None:
    """save pipeline

    Parameters
    ----------
    pipeline_to_save : Pipeline
        pipeline to save
    """
    save_file_name = f"{config.app_config.pipeline_save_file}{_version}.pkl"
    save_path = TRAINED_MODEL_DIR / save_file_name

    remove_old_pipeline(files_to_keep=[save_file_name])
    joblib.dump(pipeline_to_save, save_path)


def load_pipeline(*, file_name: str) -> Pipeline:
    """load pipeline

    Parameters
    ----------
    file_name : str
        name of pipline to load

    Returns
    -------
    Pipeline
        _description_
    """
    file_path = TRAINED_MODEL_DIR / file_name
    trained_model = joblib.load(filename=file_path)
    return trained_model


def remove_old_pipeline(*, files_to_keep: List[str]) -> None:
    """remove old pipeline

    Parameters
    ----------
    files_to_keep : List[str]
        list of file name to keep
    """
    keep = files_to_keep + ["__init__.py"]
    for model_file in TRAINED_MODEL_DIR.iterdir():
        if model_file.name not in keep:
            model_file.unlink()  # pathlib 모듈을 사용하여 객체를 삭제
