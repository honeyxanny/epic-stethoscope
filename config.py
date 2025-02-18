import yaml

class Config:
    sample_rates: list[int]
    bit_depths: list[int]
    
    def __init__(self, **kwargs):
        self.sample_rates = kwargs['sample_rates']
        self.bit_depths = kwargs['bit_depths']

with open('config.yml', 'r', encoding='utf-8') as stream:
    config = Config(**yaml.load(stream, Loader=yaml.FullLoader))