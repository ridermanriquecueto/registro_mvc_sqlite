from model.model import UserModel
from view.view import UserView
from controller.controller import UserController

def main():
    db_name = "users.db"
    model = UserModel(db_name)
    view = UserView()
    controller = UserController(model, view)

    while True:
        print("\nOpciones:")
        print("1. Agregar usuario")
        print("2. Listar usuarios")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")
        print("5. Salir")
        choice = input("Seleccione una opción: ")

        if choice == '1':
            controller.add_user()
        elif choice == '2':
            controller.list_users()
        elif choice == '3':
            controller.update_user()
        elif choice == '4':
            controller.delete_user()
        elif choice == '5':
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
