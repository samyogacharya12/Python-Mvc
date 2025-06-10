from .database import get_db_connection

class Category:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

    @staticmethod
    def get_all_categories():
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("SELECT id, name, description FROM category;")
        categories = cursor.fetchall()
        db.close()

        # Convert results into Category objects
        return [Category(*row).__dict__ for row in categories]
