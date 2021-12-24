
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

class fcnet(nn.Module):
	def __init__(self):
		super(fcnet, self).__init__()
		
		self.lay1 = nn.Linear(2, 4)
		self.lay2 = nn.Linear(4, 4)
		self.lay3 = nn.Linear(4, 1)
	
	def forward(self, x):
		x = self.lay1(x)
		x = self.lay2(x)
		x = self.lay3(x)
		x = torch.sigmoid(x)*4
		return x


class torch_svr( ):

	def __init__(self, X,y):
		X = np.array(X)
		y = np.array(y)

		tx = torch.from_numpy(X).float()
		ty = torch.from_numpy(y).float()
		ty = np.transpose( ty, axes=(1, 0))

		print('\n tx shape, ty shape \n',tx.shape, ty.shape)

		net = fcnet()
		
		criterion = nn.MSELoss()
		learning_rate = 0.005
		optimizer = optim.SGD(net.parameters(),lr=learning_rate,momentum=0.9)

		for i in range(1000):
			
			
			res = net(tx)
			loss = criterion(res, ty)
			#print("loss and res",loss,res)
			

			optimizer.zero_grad()
			loss.backward()
			optimizer.step() 

		print(loss)
		self.net = net.eval()
		  
	def predict(self, X):
		X = np.array(X)
		X = torch.from_numpy(X).float()
		res = self.net.forward(X)
		return res
	
if __name__ == "__main__":

	

	X = [[0, 0], [1, 1], [2, 2], [3, 3]]
	y = [[0, 0, 2, 3]]
	
	clf = torch_svr(X,y)
	
	res = clf.predict(X)
	print(res) 


	X = [[0.3, 0.5], [0.7, 0.7], [1.1, 1.1], [3, 3]]
	res = clf.predict(X)
	print(res) 


