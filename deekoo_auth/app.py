
import argparse
import os

from deekoo_auth import create_app

usage="""

Run the the app by giving a configuration file


"""


def run():

    parser = argparse.ArgumentParser(usage=usage)
    parser.add_argument('-c', '--config', metavar="/path/to/config.py", help="Path to config.py file to load at app start")
    args = parser.parse_args()

    if args.config:
        # run with the argument configuration file

        # relative paths will break stuff up
        config_full_path = os.path.abspath(args.config)

    else:
        # run with the defeult config
        config_full_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config', 'config.py')

    
    print(f"Deploying app with config {config_full_path}")

    app = create_app(config_full_path)
    
    app.run()

if __name__ == "__main__":
    run()