import yaml
from yaml import Loader, Dumper

yaml_file = open('playerdata.yml', 'r')
data = yaml.load(yaml_file, Loader=Loader)
total = data['playerscore']
print(total+1)
