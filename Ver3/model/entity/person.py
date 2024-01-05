from Ver3.model.tools.validation import name_validator

class Person:
    def __init__(self, name, family):
        self.name = name
        self.family = family

    def __repr__(self):
        return str(self.__dict__)

    def tuple(self):
        return tuple(self.__dict__.values())

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name_validator(name):
            self._name = name
        else:
            raise ValueError("Invalid Name")

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, family):
        if name_validator(family):
            self._family = family
        else:
            raise ValueError("Invalid family")
