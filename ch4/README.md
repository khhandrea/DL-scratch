## Chapter 1. 헬로 파이썬

| File | Description | Page |
| :-- |:--   |:--      |
| gradient_descent.py | Numerical gradient, gradient descent | 127 |
| loss_function.py | MSE, CEE | 112 |
| train_neuralnet.py | Train 'two_layer_net.py' | 141 |
| two_layer_net.py | Two-layered NN class defined | 137 |

### Concept
- 손실 함수
  - Mini-batch : 훈련 데이터로부터 일부만 골라 학습
  - MSE(Mean Squared Error) :
    $$E = \frac{1}{2}\sum_k (y_k - t_k)^2$$
  - Cross Entropy :
    $$-\sum t_k log (y_k)$$
    - Mini-batched Cross Entropy :
      $$-\frac{1}{N}\sum_n \sum_k t_{nk} log(y_{nk})$$

- 경사 하강법 (Gradient Descent Method) :
  $$x_0 = x_0 - \eta\frac{\partial f}{\partial x_0}$$
  $$x_1 = x_1 - \eta\frac{\partial f}{\partial x_1}$$

- 확률적 경사 하강법 (Stochastic Gradient Descent, SGD) : 미니배치 데이터로 학습하는 경사 하강법
  1. Mini-batch
  2. 기울기 산출
  3. 매개변수 갱신
  4. 반복

- SGD의 계산 속도는 많이 많이 느리다. ch5의 오차역전파법을 사용할 것을 추천

- epoch : 학습에서 훈련 데이터를 모두 소진했을 떄의 횟수.
  - ((훈련 데이터 개수) / (배치 크기))회 = 1epoch