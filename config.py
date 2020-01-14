import argparse

def get_args():

    argp = argparse.ArgumentParser()

    argp.add_argument('--transformer', action='store_true', default = False, help = 'transformer')
    argp.add_argument('--batch_size', type = int, default = 32, help = 'batch_size')

    return argp.parse_args()
