# Exercise 5-2: Inheritance
#
# Create a Worker class which inherits a Person class.
# Worker has two own properties:
# * contractType: FullTime or PartTime
# * salary: amount of monthly salary
# + all properties from the Person base class (see Exercise I)

from person import Person

class ContractTypeError(Exception):
    pass

class Worker(Person):
    _allowedContractTypes = ['FullTime', 'PartTime', 'Hourly']

    def __init__(self, name, contract_type, salary):
        # Validate arguments
        if contract_type not in Worker._allowedContractTypes:
            raise ContractTypeError('Unknown contract type: ' + contract_type)

        super().__init__(name)
        self.contract_type = contract_type
        self.salary = salary

    def __repr__(self):
        return repr((self.name, self.contract_type, self.salary))

def main():
    persons = list()
    persons.append(Worker("Bill","FullTime", 4500))
    persons.append(Worker("John","PartTime", 2900))
    persons.append(Worker("Calle","FullTime", 3900))
    persons.append(Worker("Mary","Hourly", 2600))
    persons.append(Worker("Jill","FullTime", 4100))
    persons.append(Worker("Ann","Hourly", 3300))

    print(persons)

if __name__ == "__main__":
    main()
