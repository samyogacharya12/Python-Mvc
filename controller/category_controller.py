from model.category import Category

class CategoryController:
    @staticmethod
    def fetch_categories():
        return Category.get_all_categories()
