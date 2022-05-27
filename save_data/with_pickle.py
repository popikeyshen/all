import pickle 

def save_vec(vec_X,vec_y, name):
	print('len ',len(vec_X), ', data save..')
	if len(vec_X)>0:
		with open(name+'.pickle', 'wb') as f_out:
			pickle.dump((vec_X,vec_y), f_out)

