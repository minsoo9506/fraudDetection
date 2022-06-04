from config.core import config
from pipeline import fraud_detection_model_pipe
from processing.data_manager import load_dataset, save_pipeline
from sklearn.model_selection import train_test_split


def run_traning() -> None:
    """run train pipeline"""
    data = load_dataset(file_name=config.app_config.train_data_file)

    X_train, X_test, y_train, y_test = train_test_split(
        data[config.model_config.features],
        data[config.model_config.target],
        test_size=config.model_config.test_size,
        random_state=config.model_config.random_state,
    )

    fraud_detection_model_pipe.fit(X_train, y_train)

    save_pipeline(pipeline_to_save=fraud_detection_model_pipe)


if __name__ == "__main__":
    run_traning()
