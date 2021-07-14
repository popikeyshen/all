
import torch
import torch.nn as nn
import torch.nn.functional as F

import numpy as np
from matplotlib import pyplot as plt


def data():
	## data vatiants
	d1 = np.array([0,3,1,6,1,3,0])
	d2 = np.array([0,3,5,6,5,3,0])
	return d1




class G(nn.Module):
	def __init__(self, ):
		super(G, self).__init__()

		self.n1 = nn.Sequential(
			# in_channels, out_channels, kernel_size, stride=1, padding=0
			nn.ConvTranspose1d(     1, 1, 3, 1, 0, bias=False),
			nn.ConvTranspose1d(     1, 1, 3, 1, 0, bias=False),
			nn.ConvTranspose1d(     1, 1, 3, 1, 0, bias=False),
		)
		#self.apply(weights_init)

	def forward(self, input):
		output = self.n1(input)
		return output



if __name__ == '__main__':
	### init data
	label = data()
	label = torch.Tensor(label)

	### init network
	device = torch.device("cuda:0")
	net = G()#.to(device)

	## init optimizer
	optimizer = torch.optim.Adam(net.parameters(), lr=0.001)

	### init loss
	loss = nn.MSELoss()

	### generator input
	key = [[[1]]]
	key = torch.Tensor(key)

	output =0
	epoch = 1000
	for i in range(epoch):
		output = net(key)

		err = loss(output, label)
		print(output, "loss  ",err )

		optimizer.zero_grad()
		err.backward()
		optimizer.step()


	### resalts
	output = output.detach().numpy()[0][0]
	plt.plot(label)
	plt.plot(output)
	plt.show()


	### weight
	for param in net.parameters():
		print(param)





