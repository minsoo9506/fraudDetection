# Fraud Detection model deployment project

- version
  - Ubuntu 20.04.4 LTS (Focal Fossa)
  - python 3.9.13

## Research

### model result metric

| 모델         | Baseline(Logit) | 설명    |
| ------------ | --------------- | ------- |
| train ROCAUC | 0.939           | 테스트3 |
| valid ROCAUC | 0.903           | 테스트3 |
| test ROCAUC  | 0.915           | 테스트3 |
| train PRAUC  | 0.612           | 테스트3 |
| valid PRAUC  | 0.585           | 테스트3 |
| test PRAUC   | 0.642           | 테스트3 |

## Deployment

## Reference

- serving
  - https://github.com/zzsza/Boostcamp-AI-Tech-Product-Serving
- sklearn.pipeline
  - https://jehyunlee.github.io/2022/05/24/Python-DS-101-kierlecture2/
- tox
  - https://christophergs.com/python/2020/04/12/python-tox-why-use-it-and-tutorial/
