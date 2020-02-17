import sys
import argparse

from deekoo_auth import create_app, db, DEFAULT_CONFIG_PATH
from deekoo_auth.models import User


usage = """
A command line tool for adding users to the database

Available tools are 

add_user [OPTIONS]      
            Add a new user to database
list_users 
            Lists current database accounts
"""

commands = ('add_user', 'list_users')

class ServerCli:

    def __init__(self):

        parser = argparse.ArgumentParser(usage=usage)
        parser.add_argument('command',
                            metavar=f"One of {commands}",
                            help=f"Entry point for other cli tools, you can select from following actions: {commands}")
        args = parser.parse_args(sys.argv[1:2])

        if not hasattr(self, args.command):
            print(f"The first argument has to be one of {commands}")
            parser.print_usage()
            sys.exit(1)

        getattr(self, args.command)()



    def add_user(self):

        parser = argparse.ArgumentParser()
        parser.add_argument('--username', required=True, metavar="Anon", help="The user name to be added.")
        parser.add_argument('--password', required=True, metavar="Secret", help="The password for the new user.")
        parser.add_argument('--email', required=False, metavar="anon@temp.net", help="The email for the new user.")
        parser.add_argument('--role', required=False, default='regular', metavar="admin", help="Either basic dude (regular) or admin (admin)")
        args = parser.parse_args(sys.argv[2:])

        app = create_app(DEFAULT_CONFIG_PATH)
        with app.app_context():
            user = User.add_user(args.username, args.password, args.email)
            if user:
                db.session.add(user)
                db.session.commit()
                print(f"created user: {user}")


    def list_users(self):

        app = create_app(DEFAULT_CONFIG_PATH)
        with app.app_context():            
            users = User.query.all()
        
        print(f"Got following users: {users}")
        for user in users:
            print(user)



def main():
    ServerCli()


if __name__ == "__main__":
    main()