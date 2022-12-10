import random
from virus import Virus


class Person(object):
    def __init__(self, _id, is_vaccinated, infection = None):
        self._id = _id  # int
        self.is_vaccinated = is_vaccinated
        self.infection = infection
        self.is_alive = True
        # self.did_survive_infection() # died, didsurvive, etc

    def did_survive_infection(self):
        if self.infection:
            check_survival = random.random()
            if check_survival > self.infection.mortality_rate:
                self.is_alive = True
                return True
            else:
                self.is_alive = False
                self.is_vaccinated = False
                return False
        # return True


if __name__ == "__main__":
    # vaccinated person
    vaccinated_person = Person(1, True)
    assert vaccinated_person._id == 1
    assert vaccinated_person.is_alive is True
    assert vaccinated_person.is_vaccinated is True
    assert vaccinated_person.infection is None

    # unvaccinated person
    unvaccinated_person = Person(2, False)
    assert unvaccinated_person._id == 2
    assert unvaccinated_person.is_alive is True
    assert unvaccinated_person.is_vaccinated is False
    assert unvaccinated_person.infection is None
    
    virus = Virus("Dysentery", 0.7, 0.2)
    
    #infected person
    infected_person = Person(3, False, virus)
    assert infected_person._id == 3
    assert infected_person.is_alive is True
    assert infected_person.is_vaccinated is False
    assert infected_person.infection is virus

    #test infected person
    new_infected_person = Person(4, False, virus)
    assert new_infected_person._id == 4
    assert new_infected_person.is_alive is True
    assert new_infected_person.is_vaccinated is False
    assert new_infected_person.infection is virus

    survival_test = new_infected_person.did_survive_infection()
    if survival_test:
        assert new_infected_person.is_alive is True
        assert new_infected_person.is_vaccinated is True
        assert new_infected_person.infection is None
    else:
        assert new_infected_person.is_alive is False
        assert new_infected_person.is_vaccinated is False
   
    # Create a list to hold 100 people. Use the loop below to make 100 people
    people = []

    for i in range(1, 100):
        patient = Person(i, False, virus)
        people.append(patient)
        patient.did_survive_infection()
        # if infected_person:
        #     people.append(infected_person)
    did_survive = 0
    did_not_survive = 0

    for person in people:
        if patient.is_alive:
            did_survive += 1
        else:
            did_not_survive += 1
        

    # Count the people that survived and did not survive: 
    print(f'Survived: {did_survive} | Dead: {did_not_survive}')
    print(f'Mortality Rate: {virus.mortality_rate}')