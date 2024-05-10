# Declare model
from torch import nn
from huggingface_hub import PyTorchModelHubMixin

class LLM(nn.Module,PyTorchModelHubMixin):
    def __init__(self, ) -> None:
        super().__init__()
    