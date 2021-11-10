import torch
import torch_rbf as rbf
import numpy as np

import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
import sys

class Network(nn.Module):
    
    def __init__(self, layer_widths, layer_centres, basis_func):
        super(Network, self).__init__()
        self.rbf_layers = nn.ModuleList()
        self.linear_layers = nn.ModuleList()
        for i in range(len(layer_widths) - 1):
            self.rbf_layers.append(rbf.RBF(layer_widths[i], layer_centres[i], basis_func))
            self.linear_layers.append(nn.Linear(layer_centres[i], layer_widths[i+1]))
    
    def forward(self, x):
        out = x
        for i in range(len(self.rbf_layers)):
            out = self.rbf_layers[i](out)
            out = self.linear_layers[i](out)
        return out
    
    def fit(self, x, y, epochs, batch_size, lr, loss_func):
        self.train()
        obs = x.size(0)
        trainset = MyDataset(x, y)
        trainloader = DataLoader(trainset, batch_size=batch_size, shuffle=True)
        optimiser = torch.optim.Adam(self.parameters(), lr=lr)
        epoch = 0
        loss =100
        while epoch < epochs:
            #if loss<0.001:
            #        epoch = epochs
            epoch += 1
            current_loss = 0
            batches = 0
            progress = 0
            for x_batch, y_batch in trainloader:
                batches += 1
                optimiser.zero_grad()
                y_hat = self.forward(x_batch)
                loss = loss_func(y_hat, y_batch)
                current_loss += (1/batches) * (loss.item() - current_loss)
                loss.backward()
                optimiser.step()
                progress += y_batch.size(0)
                sys.stdout.write('\rEpoch: %d, Progress: %d/%d, Loss: %f      ' % \
                                 (epoch, progress, obs, current_loss))
                sys.stdout.flush()
                
class MyDataset(Dataset):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __len__(self):
        return self.x.size(0)
    
    def __getitem__(self, idx):
        x = self.x[idx]
        y = self.y[idx]
        return (x, y)

class torch_svm( ):

	def __init__(self, X,y):
		X = np.array(X)
		y = np.array(y)
		y = np.swapaxes(y, 1,0)


		tx = torch.from_numpy(X).float()
		ty = torch.from_numpy(y).float()

		print('\n tx shape, ty shape \n',tx.shape, ty.shape)

		
		samples = 4
		layer_widths = [2,1]
		layer_centres = [4]
		basis_func = rbf.gaussian

		rbfnet = Network(layer_widths, layer_centres, basis_func)
		rbfnet.fit(tx, ty, 5000, samples, 0.01, nn.MSELoss())
		self.net = rbfnet.eval()
		  
	def predict(self, X):
		X = np.array(X)
		X = torch.from_numpy(X).float()
		res = self.net.forward(X)
		return res
	
if __name__ == "__main__":

	

	X = [[0, 0], [1, 1], [2, 2], [3, 3]]
	y = [[0, 1, 2, 3]]
	
	clf = torch_svm(X,y)
	
	res = clf.predict(X)
	print(res)
	
