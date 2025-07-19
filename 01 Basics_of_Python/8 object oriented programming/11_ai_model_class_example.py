# Simulated AI model with train and predict methods

class SimpleModel:
    def __init__(self, name):
        self.name = name

    def train(self):
        print(f"{self.name} is training...")

    def predict(self, x):
        print(f"{self.name} predicts: {x * 2}")

model = SimpleModel("LinearRegressor")
model.train()
model.predict(5)