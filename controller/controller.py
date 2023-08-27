from model.model import UserModel
from view.view import UserView

class UserController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_user(self):
        name = self.view.get_user_input("Ingrese el nombre del usuario: ")
        email = self.view.get_user_input("Ingrese el email del usuario: ")
        self.model.insert_user(name, email)
        self.view.show_message("Usuario agregado exitosamente.")

    def list_users(self):
        users = self.model.get_users()
        self.view.show_users(users)

    def update_user(self):
        user_id = self.view.get_user_id_input()
        new_name = self.view.get_user_input("Ingrese el nuevo nombre: ")
        self.model.update_user(user_id, new_name)
        self.view.show_message("Usuario actualizado exitosamente.")

    def delete_user(self):
        user_id = self.view.get_user_id_input()
        self.model.delete_user(user_id)
        self.view.show_message("Usuario eliminado exitosamente.")
