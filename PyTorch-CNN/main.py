import torch
from PIL import Image
from torch import nn, save, load
from torch.optim import Adam
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor

train = datasets.MNIST(root = "/Users/yashvardhan/Desktop/Learnings/PyTorch-CNN/data", download = True, train = True, transform = ToTensor())
dataset = DataLoader(train, 32)

class ImageClassifier(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Conv2d(1, 32, (3, 3)),
            nn.ReLU(),
            nn.Conv2d(32, 64, (3, 3)),
            nn.ReLU(),
            nn.Conv2d(64, 64, (3, 3)),
            nn.ReLU(),
            nn.Flatten(),
            nn.Linear(64*22*22, 10)
        )
    def forward(self, x):
        return self.model(x)
    

clf = ImageClassifier().to('cpu')
optim = Adam(clf.parameters(), lr = 1e-3)
loss_fn = nn.CrossEntropyLoss()

if __name__ == "__main__":
    # for epoch in range(10):
    #     for batch in dataset:
    #         X, y = batch
    #         X, y = X.to('cpu'), y.to('cpu')
    #         yhat = clf(X)
    #         loss = loss_fn(yhat, y)

    #         optim.zero_grad()
    #         loss.backward()
    #         optim.step()
        
    #     print("Epoch : ", epoch, " | Loss : ", loss)

    # with open('Model.pt', 'rb') as f:
    #     save(clf.state_dict(), f)

    path = "<path to the image>"

    with open("Model.pt", 'rb') as f:
        clf.load_state_dict(load(f))

    img = Image.open(path)
    img_tensor = ToTensor(img).unsqueeze(0).to('cpu') # ToTensor returns shape in the format [channels, height, width],
                                                      # but as we have batches therefore we need batch dimension as well, 
                                                      # so unsqueeze(0) add 1 as the dimension at zeroth index : [1, channels, height, width]
    print(torch.argmax(clf(img_tensor)))

    


