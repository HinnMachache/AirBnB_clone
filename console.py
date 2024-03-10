#!/usr/bin/python3
"""The Console File"""

from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
import cmd


class HBNBCommand(cmd.Cmd):
    """Class that has logic of the console"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """The quit Function"""
        exit()

    def do_EOF(self, line):
        """Quit the Command by: Ctrl+D"""
        return True

    def emptyline(self):
        """Overwrite empty line"""
        pass

    def do_create(self, model):
        """Creates a new instance"""
        models = {"BaseModel": BaseModel, "Amenity": Amenity, "City": City,
                  "Place": Place, "Review": Review, "State": State,
                  "User": User}
        if not model:
            print("** class name missing **")
        elif model not in models:
            print("** class doesn't exist **")
        else:
            new_model = models[model]()
            new_model.save()
            print(f"{new_model.id}")

    def do_show(self, model):
        """Prints string representation of an instance"""
        model = model.split(" ")
        data = storage.all()
        models = {"BaseModel": BaseModel, "Amenity": Amenity, "City": City,
                  "Place": Place, "Review": Review, "State": State,
                  "User": User}

        if not model[0]:
            print("** class name missing **")
        elif model[0] not in models:
            print("** class doesn't exist **")
        elif len(model) < 2:
            print("** instance id missing **")
        else:
            for key, value in data.items():
                if model[1] == value.id:
                    print(value)
                    return
            print("** no instance found **")

    def do_destroy(self, model):
        """Delete an intance based on the id"""
        model = model.split(" ")
        data = storage.all()
        models = {"BaseModel": BaseModel, "Amenity": Amenity, "City": City,
                  "Place": Place, "Review": Review, "State": State,
                  "User": User}

        if not model[0]:
            print("** class name missing **")
        elif model[0] not in models:
            print("** class doesn't exist **")
        elif len(model) < 2:
            print("** instance id missing **")
        else:
            for key, value in data.items():
                if model[1] == value.id:
                    del value
                    del storage._FileStorage__objects[key]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, model):
        """Prints all string representation of all instances"""
        data = storage.all()
        obj = []

        if not model:
            for key, value in data.items():
                obj.append(value.__str__())
            print(obj)
        else:
            for key, value in data.items():
                key = key.split(".")
                if key[0] == model:
                    obj.append(value.__str__())
                if len(obj) == 0:
                    print("** class doesn't exist **")
                    return
                print(obj)

    def do_update(self, args):
        """
        This command updates a field in the object module
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """

        data = storage.all()
        models = ["BaseModel", "User", "State", "City",
                  "Amenity", "Place", "Review"]
        model = args.split()
        if len(model) == 0:
            print("** class name missing **")
        elif model[0] not in models:
            print("** class doesn't exist **")
        elif len(model) == 1:
            print("** instance id missing **")
        elif len(model) == 2:
            print("** attribute name missing **")
        elif len(model) == 3:
            print("** value missing **")
        else:
            for key, value in data.items():
                tag = key.split('.')
                if model[0] == tag[0]:
                    if model[1] == value.id:
                        setattr(value, model[2], model[3])
                        # storage.save()
                        return
            print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
