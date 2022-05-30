# Fraud Detection model deployment project

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

## Deployment

- fastapi
- CircleCI, git action
- docker

## Reference

- Lecture
  - https://www.udemy.com/course/deployment-of-machine-learning-models/
- serving
  - https://github.com/zzsza/Boostcamp-AI-Tech-Product-Serving
- sklearn.pipeline
  - https://jehyunlee.github.io/2022/05/24/Python-DS-101-kierlecture2/
- tox
  - https://christophergs.com/python/2020/04/12/python-tox-why-use-it-and-tutorial/
