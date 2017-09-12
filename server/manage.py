from app import app, sa, models
from app.console.commands import SeedCommand
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

migrate = Migrate(app=app, db=sa, directory='database/migrations')
manager = Manager(app)

# Add database seeder command line
@MigrateCommand.command
def seed():
    SeedCommand.run()

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
