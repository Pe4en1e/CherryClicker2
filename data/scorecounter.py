import yaml
from yaml import Loader, Dumper


yaml_file = open('data/playerdata.yml', 'r')
data = yaml.load(yaml_file, Loader=Loader)


class cherryjam():
    count = int(data['cherryjam_count'])
    price = round(15*1.1**count)
    buff = 5

class autoscore():
    total = cherryjam.buff*cherryjam.count
