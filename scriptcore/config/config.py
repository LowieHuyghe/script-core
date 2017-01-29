
try:
    import ConfigParser
except ImportError:
    import configparser as ConfigParser


class Config(object):

    def __init__(self):
        """
        Construct the config instance
        """

        self._config = {}

    def __call__(self, key, default=None):
        """
        Call instance
        :param key:     The key
        :param default: The default value
        :return:        The value
        """

        return self.get(key, default)

    def get(self, key, default=None):
        """
        Get a config value
        :param key:     The key
        :param default: The default value
        :return:        The value
        """

        parts = key.split('.')

        value = self._config
        for part in parts:
            if part in value:
                value = value[part]
            else:
                return default

        return value

    def load_from_ini(self, filename):
        """
        Load config from ini-file
        :param filename:    The file name
        :return:
        """

        config = ConfigParser.ConfigParser()
        config.read(filename)

        for section in config.sections():
            for option in config.options(section):
                if section.lower() not in self._config:
                    self._config[section.lower()] = {}

                try:
                    value = config.getint(section, option)
                except ValueError:
                    try:
                        value = config.getfloat(section, option)
                    except ValueError:
                        try:
                            value = config.getboolean(section, option)
                        except ValueError:
                            value = config.get(section, option)

                self._config[section.lower()][option.lower()] = value