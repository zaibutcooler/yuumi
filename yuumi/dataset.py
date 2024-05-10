from datasets import Dataset as HFDataset

class Dataset(HFDataset):
    def __init__(self,url = ''):
        super().__init__()
        pass
    
    def load_dataset(self):
        pass
    
    def get_data(self):
        pass
    
    def build_dataset(self):
        pass


pretrainset = Dataset()

finetuneset = Dataset()