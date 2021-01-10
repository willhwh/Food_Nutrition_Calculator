from function_folder.functions_file import static, back_to_menu, get_command
from class_folder.main_function_class import main_function

#program functions
def main():
    print('Welcome to Food Recorder Main Menu')
    cmd = get_command()
    static = main_function()
    static.__start__()
    if cmd == 'A':
        static.start_record()
        main()
    elif cmd == 'V':
        static.start_visualize()
        main()
    elif cmd == 'Q':   
        print('Thanks for using this software.')
        pass
    else:
        print("Unknown command: %s => try again." % cmd)


if __name__ == "__main__":
    main()