# Simulated dataset class like in ML frameworks

class CustomDataset:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.data[index]

dataset = CustomDataset([10, 20, 30, 40])
print("Length:", len(dataset))
print("Item at 2:", dataset[2])