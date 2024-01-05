from Ver3.model.da.person_da import PersonDa
from Ver3.model.entity.person import Person


class PersonController:
    def save(self, name, family):
        try:
            person = Person(name, family)
            da = PersonDa()
            da.save(person)
            return "Person Saved"
        except Exception as e:
            return e

    def find_all(self):
        try:
            da = PersonDa()
            return da.find_all()
        except Exception as e:
            return e
