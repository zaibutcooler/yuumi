from datasets import Dataset as HFDataset

class Dataset(HFDataset):
    def __init__(self):
        super().__init__()
        pass


pretrainset = Dataset()

finetuneset = Dataset()