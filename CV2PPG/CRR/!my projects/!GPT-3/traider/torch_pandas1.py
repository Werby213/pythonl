import datapackage
import pandas as pd
import torch
import torch.nn as nn
import numpy as np

data_url = 'https://datahub.io/core/s-and-p-500-companies/datapackage.json'

# to load Data Package into storage
package = datapackage.Package(data_url)

# to load only tabular data
resources = package.resources
for resource in resources:
    if resource.tabular:
        df = pd.read_csv(resource.descriptor['path'])
        break

# Load the stock market data into a pandas DataFrame
# df = pd.read_csv("stock_market_data.csv")

# Preprocess the data to extract relevant features
df = df.dropna()
# Convert the pandas DataFrame to a numpy array
data = df.values

# Normalize the data to zero mean and unit variance
mean = np.mean(data, axis=0)
std = np.std(data, axis=0)
data = (data - mean) / std

# Split the data into training and testing sets
train_data = data[:int(0.8 * len(data))]
test_data = data[int(0.8 * len(data)):]

# Convert the data to PyTorch tensors
train_inputs = torch.tensor(train_data[:-1, :], dtype=torch.float32)
train_targets = torch.tensor(train_data[1:, -1], dtype=torch.float32)
test_inputs = torch.tensor(test_data[:-1, :], dtype=torch.float32)
test_targets = torch.tensor(test_data[1:, -1], dtype=torch.float32)


# Define the neural network architecture
class StockMarketNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(5, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x


# Initialize the neural network
model = StockMarketNet()

# Define the loss function and the optimizer
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

# Train the neural network
for epoch in range(1000):
    optimizer.zero_grad()
    outputs = model(train_inputs)
    loss = criterion(outputs, train_targets)
    loss.backward()
    optimizer.step()

# Evaluate the performance of the neural network on the test data
with torch.no_grad():
    test_outputs = model(test_inputs)
    test_loss = criterion(test_outputs, test_targets)
    print("Test Loss:", test_loss.item())
