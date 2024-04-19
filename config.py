import configparser

def read_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    return config['DEFAULT']

def update_config(key, value, config_file='config.ini'):
    config = configparser.ConfigParser()
    config.read(config_file)
    config.set('DEFAULT', key, value)
    
    with open(config_file, 'w') as config_file:
        config.write(config_file)
