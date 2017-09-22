# Prevented from writing .pyc or .pyo files and __pycache__ folders
import sys; sys.dont_write_bytecode = True

from app import app, sa
from app.console.commands import SeedCommand
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

migrate = Migrate(app=app, db=sa, directory='database/migrations')
manager = Manager(app)

# Add database seeder command line
@MigrateCommand.command
def seed(drop=False):
    SeedCommand.run(drop)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
