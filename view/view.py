class UserView:
    @staticmethod
    def show_users(users):
        print("Lista de usuarios:")
        for user in users:
            print(f"ID: {user[0]}, Nombre: {user[1]}, Email: {user[2]}")

    @staticmethod
    def show_message(message):
        print(message)

    @staticmethod
    def get_user_input(prompt):
        return input(prompt)

    @staticmethod
    def get_user_id_input():
        return int(input("Ingrese el ID del usuario: "))
