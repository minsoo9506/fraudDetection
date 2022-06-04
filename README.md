# Fraud Detection model python package project

- version
  - Ubuntu 20.04.4 LTS (Focal Fossa)
  - python 3.9.13

## Research

### model result metric

| 모델         | Baseline(Logit) | Baseline + SMOTE(0.1) | Baseline + RUS(0.1) | RUSBoost  |
| ------------ | --------------- | --------------------- | ------------------- | --------- |
| train ROCAUC | 0.939           | 0.989                 | 0.966               | 0.999     |
| valid ROCAUC | 0.903           | **0.930**             | 0.928               | 0.922     |
| test ROCAUC  | 0.915           | 0.945                 | 0.947               | **0.963** |
| train PRAUC  | 0.612           | 0.965                 | 0.921               | 0.798     |
| valid PRAUC  | 0.585           | **0.671**             | 0.639               | 0.668     |
| test PRAUC   | 0.642           | **0.745**             | 0.717               | 0.716     |

## summary

### tox를 통한 test

```bash
# 전체 test
tox
# 특정한 세션만 test, 예를 들어 lint를 한다고 하면 아래와 같이 진행
tox -e lint
```

### python package

- python package 를 만들기 위해 추가적으로 작성한 파일들은 아래와 같다.
  - `setup.py`, `MANIFEST.in`, `pyproject.toml`
  - 각 파일들이 하는 일은 내용을 보면 대략적으로 이해가 된다.
- https://packaging.python.org/en/latest/tutorials/packaging-projects/

```bash
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade build
python3 -m build

# 최종 log에 아래와 같이 나온다
Successfully built fraud_detection_model-0.0.1.tar.gz and fraud_detection_model-0.0.1-py3-none-any.whl
```

- 그러면 새로운 폴더, 파일들이 생성된다.

## Reference

- Lecture
  - https://www.udemy.com/course/deployment-of-machine-learning-models/
- serving
  - https://github.com/zzsza/Boostcamp-AI-Tech-Product-Serving
- sklearn.pipeline
  - https://jehyunlee.github.io/2022/05/24/Python-DS-101-kierlecture2/
- tox
  - https://christophergs.com/python/2020/04/12/python-tox-why-use-it-and-tutorial/
- pydantic
  - Data validation and settings management using python type annotations
  - https://pydantic-docs.helpmanual.io/
  - https://velog.io/@kjh03160/Type-Hinting
- strinctyaml
  - type-safe YAML parser that parses and validates a restricted subset of the YAML specification
  - https://github.com/crdoconnor/strictyaml
  - https://hitchdev.com/strictyaml/why-not/turing-complete-code/
