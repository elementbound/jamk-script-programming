# Exercise 5-4: Worker sorting
#
# Use Worker class from the exercise 5-2.
# Add Worker object into the list.
#
# Sort this list based on name and salary of the workers. 

from worker import Worker

def main():
    persons = list()
    persons.append(Worker("Bill","FullTime", 4500))
    persons.append(Worker("John","PartTime", 2900))
    persons.append(Worker("Calle","FullTime", 3900))
    persons.append(Worker("Mary","Hourly", 2600))
    persons.append(Worker("Jill","FullTime", 4100))
    persons.append(Worker("Ann","Hourly", 3300))

    name_sort = sorted(persons, key=lambda x: x.name)
    salary_sort = sorted(persons, key=lambda x: x.salary)

    print('Sorted by name: \n', '\n'.join([str(x) for x in name_sort]), '\n', sep='')
    print('Sorted by salary: \n', '\n'.join([str(x) for x in salary_sort]), '\n', sep='')

if __name__ == '__main__':
    main()
