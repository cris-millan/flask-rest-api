import click
import os
from sqlalchemyseed import load_entities_from_json
from sqlalchemyseed import Seeder

__json_path: str = 'seeds/json/'


def generate_seeder_list() -> dict:
    return {os.path.splitext(path)[0]: __json_path + path for path in os.listdir(__json_path)}


def register_commands(app, db):
    @app.cli.command("seed")
    @click.option('-n', '--name', 'name', default=None, show_default=True)
    @click.option('-l', '--list', 'list', is_flag=True, show_default=True, default=False)
    def seed(name, list):
        __seed_json_files = generate_seeder_list()
        if list:
            for name in __seed_json_files.keys():
                print(name)
            return 'finish'

        if name is not None:
            if __seed_json_files[name] is not None:
                try:
                    # load entities
                    entities = load_entities_from_json(__seed_json_files[name])
                    # Initializing Seeder
                    seeder = Seeder(db.session, ref_prefix='!')
                    # Seeding
                    seeder.seed(entities)
                    # Committing
                    seeder.session.commit()
                except Exception as ex:
                    print(str(ex))
                return "finish"

            else:
                print('invalid name try using -l to see the available names')
                return 'finish'

        if name is None:
            seeder = Seeder(db.session)
            for json_path in __seed_json_files.values():
                print(json_path)
                # load entities
                entities = load_entities_from_json(json_path)
                # Seeding
                seeder.seed(entities)
                seeder.session.commit()
                # Committing

            return "SUCCESS"

    @app.cli.command("command2")
    def another_command():
        print("another command")
