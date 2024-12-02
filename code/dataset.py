import json
import os
from torch.utils.data import Dataset

class MATH(Dataset):
    """
    Creates the Math Dataset from the JSON files and the base for the dataloader
    """

    def __init__(self, split='train', subject=None):
        parent_dir = os.path.join(os.getcwd(), os.pardir)
        data_dir = os.path.join(parent_dir, 'data/MATH')
        
        if subject:
            self.split_dir = os.path.join(data_dir, split, subject)
        else:
            self.split_dir = os.path.join(data_dir, split)

        if os.path.isdir(self.split_dir) == False:
            raise IOError(f"Invalid data directory: {self.split_dir}")
        
        print(self.split_dir)
        self.data = self.load_data()
    
    def load_data(self):
        
        data = []
        for root, _, files in os.walk(self.split_dir):
            for file_name in files:
                if file_name.endswith('.json'):
                    file_path = os.path.join(root, file_name)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = json.load(f)
                        content.pop('level')
                        content.pop('type')
                        data.append(content)
        return data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        
        item = self.data[idx]
                
        return item['problem'], item['solution']