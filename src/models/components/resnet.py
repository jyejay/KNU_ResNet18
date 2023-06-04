import torch
import torchvision.models as models

class ResNet(torch.nn.Module):
    def __init__(self, model_name: str, pretrained: bool = True, num_classes: int = 10) -> None:
        super().__init__()
        self.model = getattr(models, model_name)(pretrained=pretrained)
        
        if model_name == 'resnet18':
            num_ftrs = self.model.fc.in_features
            self.model.fc = torch.nn.Linear(num_ftrs, num_classes)  # Here we replace the last layer
        
    def forward(self, x):
        return self.model(x)