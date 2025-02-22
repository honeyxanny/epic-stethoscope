import yaml

class Config:
    sample_rates: list[int]
    
    def __init__(self, **kwargs):
        self.sample_rates = kwargs['sample_rates']

with open('config.yml', 'r', encoding='utf-8') as stream:
    config = Config(**yaml.load(stream, Loader=yaml.FullLoader))