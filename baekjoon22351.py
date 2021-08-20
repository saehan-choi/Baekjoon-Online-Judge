import torch



b1_x1 = torch.FloatTensor([-0.1])
b1_x2 = torch.FloatTensor([0.5])
b2_x1 = torch.FloatTensor([0.5])
b2_x2 = torch.FloatTensor([1.8])

# print(torch.min(b1_x2, b2_x2) - torch.max(b1_x1, b2_x1))

print(b1_x1.clamp(0))
print(b1_x2.clamp(0))
print(b2_x1.clamp(0))   
print(b2_x1.clamp(1))