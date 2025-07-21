# Overriding parent class methods

class BaseModel:
    def train(self):
        print("Training base model")

class NeuralNet(BaseModel):
    def train(self):
        print("Training deep neural network")

model = NeuralNet()
model.train()

print('*' * 50)

class Bank:
    def roi(self):
        return "10% return"

class IcIcBank(Bank):
    def roi(self):
        return "7% return"

class UnionBank(Bank):
    def roi(self):
        return "9% return"

bankb1 = Bank()
bankb2 = IcIcBank()
bankb3 = UnionBank()

print("Bank Rate of interest:",bankb1.roi())
print("Bank Rate of interest:",bankb2.roi())
print("Bank Rate of interest:",bankb3.roi())
