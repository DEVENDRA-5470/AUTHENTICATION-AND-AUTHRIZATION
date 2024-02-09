
import subprocess

def main():
    while True:
        # Display menu options
        print("Menu:")
        print("1. Make Migrations (mk)")
        print("2. Migrate (mg)")
        print("3. Run Server (run)")
        print("4. Start App (s)")
        print("5. Quit (b)")

        # User input for menu choice
        choice = input("Enter your choice: ")

        if choice == "mk":
            subprocess.run(["python", "manage.py", "makemigrations"])
        elif choice == "mg":
            subprocess.run(["python", "manage.py", "migrate"])
        elif choice == "run":
            subprocess.run(["python", "manage.py", "runserver"])
        elif choice == "s":
            app_name = input("Enter the app name: ")
            subprocess.run(["python", "manage.py", "startapp", app_name])
        elif choice == "b":
            print("Exiting the menu.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()