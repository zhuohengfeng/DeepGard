<p align="center">
  <img src="logo.png" width="200" alt="DeepGrad Logo"/>
</p>

<p align="center"><em>A lightweight and modular deep learning framework</em></p>

---

## 🚀 Features

- 🔁 **Automatic Differentiation** (autograd engine built from scratch)
- 🧱 **Modular Layers** (build models layer by layer)
- 🎯 **Optimizers** (SGD, Adam, RMSProp etc.)
- 📊 **Metrics & Losses** (MSE, CrossEntropy, etc.)
- 🧪 **Custom Training Loops** with flexibility
- 🧵 **Numpy-based** backend (no heavy dependencies)

---

## 🧠 Quick Start

```python
from deepgrad import Tensor, Linear, MSELoss, SGD

# Dummy training example
x = Tensor([[1.0], [2.0]])
y = Tensor([[2.0], [4.0]])

model = Linear(1, 1)
loss_fn = MSELoss()
optimizer = SGD(model.parameters(), lr=0.01)

for epoch in range(100):
    pred = model(x)
    loss = loss_fn(pred, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    print(f"Epoch {epoch}, Loss: {loss.data:.4f}")
