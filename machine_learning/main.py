import torch 
print(torch.__version__)
print(torch.get_default_dtype())

#set new dtype float32 -> float 64
torch.set_default_dtype(torch.float64)
print(torch.get_default_dtype())

#2d tensor array
tensor_arr = torch.Tensor([[1,2,3], [4,5,6]])
print(tensor_arr)

#check is var is tensor
print(torch.is_tensor(tensor_arr))

#print num of elements regardless of shape
print(torch.numel(tensor_arr))

#create a new uninitialized tensor in memory
t_unit = torch.Tensor(2,2)
print(t_unit)


#initialized random value tensor
t_init = torch.rand(2,2)
print(t_init)

#int tensor
torch_custom_dtype = torch.Tensor([5,2]).type(torch.IntTensor)
print(torch_custom_dtype)

#torch.half halves the float size to save memory

#eye creates a diagnol 1s matrix
tensor_eye = torch.eye(5)

i = torch.tensor([[0,1,1], [2,2,0]])
v = torch.tensor([3,4,5])
#creates a sparse tensor in coordinate format with non-zero elements at indices with the given values
sparce_tensor = torch.sparse_coo_tensor(i, v, [2, 5])

print(sparce_tensor.data)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
#_ modifies the operation in place
init_tensor = torch.rand(2,3)

init_tensor.fill_(10)
print(init_tensor)
init_tensor.add_(20)
print(init_tensor)

#gen even spaced numbers
x = torch.linspace(start=0.1, end=10, steps=15)
print(x)
chunkx = torch.chunk(x, 3,0)
print(chunkx)
print(x.size())
print(x.shape)
test = torch.rand(2,2)
print(test.shape)
torch_unsqueeze = torch.unsqueeze(test, 2)
print(torch_unsqueeze.shape)
torch_squeeze = torch.squeeze(torch_unsqueeze, 2)
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
print(torch.cuda.is_available())
torch.cuda.init()
print("Current device", torch.cuda.current_device())
print("Device count", torch.cuda.device_count())
print(torch.cuda.memory_allocated())
print(torch.cuda.memory_cached())

cuda = torch.device('cuda')
print(cuda)
cuda0 = torch.device('cuda:0')
print(cuda0)
x = torch.tensor([10,20], device='cuda:1')
print(x)