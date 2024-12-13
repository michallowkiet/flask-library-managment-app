from configparser import ConfigParser


def load_config(filename="database.ini", section="postgresql"):
    # create a parser
    parser = ConfigParser()
    parser.read(f"./{filename}")

    # get section, default to postgresql
    config = {}

    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        raise Exception(f"Section {section} not found in the {filename} file")

    return config


if __name__ == "__main__":
    conf = load_config()
    print(conf)
