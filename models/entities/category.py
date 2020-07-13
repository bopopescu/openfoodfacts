
import unidecode
from models.manager import Manager


class Category():
    objects = Manager()
    table = "category"
    name = None

    def __init__(self, name):
        self.name = name.replace("'", " ")

    def __str__(self):
        return f"catégorie: {self.name}"

    def get_name(self):
        return self.name

    def save(self):
        from database import Database
        db = Database()
        db.save(self)