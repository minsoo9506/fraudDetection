from pathlib import Path
from typing import List

# pydantic을 통해 config.yml에 있는 config들의 type을 정해주자
# 저절로 type을 바꿔주고 바꿀수 없는 경우는 error return
from pydantic import BaseModel
from strictyaml import YAML, load

import fraud_detection_model

PACKAGE_ROOT = Path(fraud_detection_model.__file__).resolve().parent
ROOT = PACKAGE_ROOT.parent
CONFIG_FILE_PATH = PACKAGE_ROOT / "config.yml"
DATASET_DIR = PACKAGE_ROOT / "datasets"
TRAINED_MODEL_DIR = PACKAGE_ROOT / "trained_models"


class AppConfig(BaseModel):
    """Application config

    Parameters
    ----------
    BaseModel : _type_
        _description_
    """

    package_name: str
    train_data_file: str
    test_data_file: str
    pipeline_save_file: str


class ModelConfig(BaseModel):
    """Model config

    Parameters
    ----------
    BaseModel : _type_
        _description_
    """

    target: str
    features: List[str]
    test_size: float
    random_state: int
    sampling_strategy: float


class Config(BaseModel):
    """master config

    Parameters
    ----------
    BaseModel : _type_
        _description_
    """

    app_config: AppConfig
    model_config: ModelConfig


def find_config_file() -> Path:
    if CONFIG_FILE_PATH.is_file():
        return CONFIG_FILE_PATH
    raise Exception(f"Config not found at {CONFIG_FILE_PATH}")


def fetch_config_from_yaml(cfg_path: Path = None) -> YAML:
    if not cfg_path:
        cfg_path = find_config_file()

    if cfg_path:
        with open(cfg_path, "r") as conf_file:
            parsed_config = load(conf_file.read())
            return parsed_config
    raise OSError(f"Did not find config file at path: {cfg_path}")


def creat_and_validate_config(parsed_config: YAML = None) -> Config:
    if parsed_config is None:
        parsed_config = fetch_config_from_yaml()

    _config = Config(
        app_config=AppConfig(**parsed_config.data),
        model_config=ModelConfig(**parsed_config.data),
    )

    return _config


config = creat_and_validate_config()
