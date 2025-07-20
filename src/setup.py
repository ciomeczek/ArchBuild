import os
import shutil

HOME = os.path.expanduser("~")

CONFIG = {
    "HYPRLAND": {
        'CONFIG_DIR': os.path.join(HOME, '.config', 'hypr'),
        'FILES': ['hyprland.conf', 'hyprpaper.conf'],
        'CHOICE_FILES': [
            {
                'OPTIONS': ['monitor-1.conf', 'monitors-2.conf'],
                'RESULT': 'monitors.conf'
            }
        ]
    },
    "KITTY": {
        'CONFIG_DIR': os.path.join(HOME, '.config', 'kitty'),
        'FILES': ['kitty.conf']
    },
    "NEOVIM": {
        'CONFIG_DIR': os.path.join(HOME, '.config', 'nvim'),
        'FILES': ['init.vim']
    },
    "WAYBAR": {
        'CONFIG_DIR': os.path.join(HOME, '.config', 'waybar'),
        'FILES': ['config.jsonc', 'style.css']
    },
    "WALLPAPER": {
        'CONFIG_DIR': os.path.join(HOME, 'Pictures'),
        'FILES': ['wallpaper.png']
    }
}


def ask_override(filename):
    resp = input(f"'{filename}' already exists. Override? (Y/N): ").strip().lower()
    return resp == 'y'


def ask_choice(options):
    print("Choose one of the following options:")
    
    for id, option in enumerate(options, 1):
        print(f"{id}) {option}")
        
    while True:
        choice = input(f"Enter choice number (1-{len(options)}): ").strip()
        
        if choice.isdigit():
            id = int(choice)
            
            if 1 <= id <= len(options):
                return options[id - 1]
            
        print("Invalid choice. Try again.")


def setup():
    override_all = input('Override all the files? (Y/N): ').strip().lower() == 'y'

    for config in CONFIG.values():
        os.makedirs(config['CONFIG_DIR'], exist_ok=True)

        for filename in config.get('FILES', []):
            destination = os.path.join(config['CONFIG_DIR'], filename)
            if override_all:
                shutil.copyfile(filename, destination)
                continue

            if os.path.exists(destination):
                if ask_override(filename):
                    shutil.copyfile(filename, destination)
            else:
                shutil.copyfile(filename, destination)

        for choice_group in config.get('CHOICE_FILES', []):
            chosen_file = ask_choice(choice_group['OPTIONS'])
            destination = os.path.join(config['CONFIG_DIR'], choice_group['RESULT'])

            if override_all:
                shutil.copyfile(chosen_file, destination)
                continue

            if os.path.exists(destination):
                if ask_override(choice_group['RESULT']):
                    shutil.copyfile(chosen_file, destination)
            else:
                shutil.copyfile(chosen_file, destination)


if __name__ == '__main__':
    setup()
