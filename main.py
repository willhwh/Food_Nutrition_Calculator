import functions as f


def main():
    print('Welcome to Food Recorder Main Menu')
    cmd = f.get_command()
    if cmd == 'A':
        f.start_record()
    elif cmd == 'V':
        f.start_visualize()
        f.back_to_menu()
    elif cmd == 'Q':   
        print('Thanks for using this software.')
        pass
    else:
        print("Unknown command: %s => try again." % cmd)


if __name__ == '__main__':
    main()  