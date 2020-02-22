import sys
import argparse

from flask_script import Manager
from flask_migrate import init, migrate, upgrade, Migrate, MigrateCommand

from deekoo_auth import create_app, db, DEFAULT_CONFIG_PATH
from deekoo_auth.models import User
from deekoo_auth.database import check_database_available

usage = """
A command line tool for adding users to the database

Available tools are 

add_user [OPTIONS]      
            Add a new user to database
list_users 
            Lists current database accounts
db  [OPTIONS]
            Interact with the database. (init, migrate, upgrade)
"""

commands = ('add_user', 'list_users', 'db')

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
        check_database_available(app)
        with app.app_context():
            user = User.add_user(args.username, args.password, args.email)
            if user:
                db.session.add(user)
                db.session.commit()
                print(f"created user: {user}")


    def list_users(self):

        app = create_app(DEFAULT_CONFIG_PATH)
        check_database_available(app)
        with app.app_context():            
            users = User.query.all()

        if len(users) == 0:
            print(f"No users in the database at {app.config['SQLALCHEMY_DATABASE_URI']}")
            return
        
        print(f"\nFound {len(users)} user{'s' if len(users) > 1 else ''} in database at {app.config['SQLALCHEMY_DATABASE_URI']}\n")
        for user in users:
            print(user)


    def db(self):
        """
            Small wrapper for flask-migrate
        """        
        database_commands = ('init', 'migrate', 'upgrade' )

        app = create_app(DEFAULT_CONFIG_PATH)

        # add database migration tools
        migrate = Migrate(app, db)
        
        # init the command line tool
        manager = Manager(app)
        manager.add_command('db', MigrateCommand)

        # parse command line arguments
        manager.run()

        
        



def main():
    ServerCli()


if __name__ == "__main__":
    main()