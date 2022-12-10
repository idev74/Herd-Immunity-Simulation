import random, sys
from person import Person
from logger import Logger
from virus import Virus

#log every itme step (alive, dead, infected, etc.), not interaction
class Simulation(object):
    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
        self.virus = virus
        self.pop_size = pop_size
        self.vacc_percentage = vacc_percentage
        self.initial_infected = initial_infected
        self.logger = Logger('logger-test.txt')
        self.newly_infected = []
        self.vaccine_saved = 0
        self.total_interactions = 0
        self.death_count = 0
        self.time_step_counter = 0
        self.people = self._create_population()
        self.num_immune = 0
        self.total_infected = 0
        # TODO: Create a Logger object and bind it to self.logger.
        # Remember to call the appropriate logger method in the corresponding parts of the simulation.
        
        # TODO: Store the virus in an attribute
        # TODO: Store pop_size in an attribute
        # TODO: Store the vacc_percentage in a variable
        # TODO: Store initial_infected in a variable
        # You need to store a list of people (Person instances)
        # Some of these people will be infected some will not. 
        # Use the _create_population() method to create the list and 
        # return it storing it in an attribute here. 
        # TODO: Call self._create_population() and pass in the correct parameters.
        

    def _create_population(self):
        # TODO: Create a list of people (Person instances). This list 
        # should have a total number of people equal to the pop_size. 
        # Some of these people will be uninfected and some will be infected.
        # The number of infected people should be equal to the the initial_infected
        # TODO: Return the list of people
        num_vaccinated = int(self.pop_size * self.vacc_percentage)
        num_unvaccinated = int(self.pop_size - num_vaccinated)
        people = []
        id = 0
        infected = self.initial_infected

        for i in range (num_vaccinated):
            people.append(Person((id + 1), True, None))

        for i in range (infected):
            people.append(Person((id + 1), False, self.virus))


        for i in range (num_unvaccinated):
            people.append(Person((id + 1), False, None))

        return people

    def _simulation_should_continue(self):
        # survivors = len(self.people) written by self
        # This method will return a boolean  indicating if the simulation 
        # should continue. 
        # The simulation should not continue if all of the people are dead, 
        # or if all of the living people have been vaccinated. 
        # TODO: Loop over the list of people in the popualation. Return True
        # if the simulation should continue or False if not.

        for person in self.people:
            if person.is_vaccinated == False and person.is_alive == True:
                return True
            return False

    def run(self):
        self.logger.write_metadata(self.pop_size, self.vacc_percentage, self.virus)
        # This method starts the simulation. It should track the number of 
        # steps the simulation has run and check if the simulation should 
        # continue at the end of each step. 
        self.time_step
        time_step_counter = 0
        should_continue = True

        while should_continue:
            # TODO: Increment the time_step_counter
            # TODO: for every iteration of this loop, call self.time_step() 
            # Call the _simulation_should_continue method to determine if 
            # the simulation should continue
            time_step_counter += 1
            print("time step counter", time_step_counter)
            should_continue = self._simulation_should_continue()
            self.time_step(time_step_counter)

        self.logger.log_interactions(time_step_counter, self.total_interactions, self.total_infected)
        print(f'Step {time_step_counter}:\nNumber Infected: {self.total_infected}')
        self.logger.log_final_data(len(self.people), self.death_count, self.num_immune + self.vaccine_saved, time_step_counter, self.total_infected) 

        # TODO: Write meta data to the logger. This should be starting 
        # statistics for the simulation. It should include the initial
        # population size and the virus. 

        # TODO: When the simulation completes you should conclude this with 
        # the logger. Send the final data to the logger. 

    def time_step(self, time_step_counter):
        # This method will simulate interactions between people, calulate 
        # new infections, and determine if vaccinations and fatalities from infections
        # The goal here is have each infected person interact with a number of other 
        # people in the population
        # TODO: Loop over your population
        # For each person if that person is infected
        # have that person interact with 100 other living people 
        # Run interactions by calling the interaction method below. That method
        # takes the infected person and a random person
        for person in self.people:
            if person.infection and person.is_alive:
                for i in range(100):
                    self.interaction(person, self.random_person(), time_step_counter)

                if person.did_survive_infection() == True:
                    person.is_vaccinated = True
                    self.num_immune += 1
                else:
                    person.is_alive = False
                    self.death_count += 1
    
    def random_person(self):
        rand_person = random.choice(self.people)
        while not rand_person.is_alive and not rand_person.is_vaccinated:
            rand_person = random.choice(self.people)
        return rand_person


    def interaction(self, infected_person, random_person, time_step_counter):
        # TODO: Finish this method.
        time_step_counter += 1
        assert infected_person.is_alive == True
        assert random_person.is_alive == True
        self.total_interactions += 1
        random_num = random.random()
        # The possible cases you'll need to cover are listed below:
            # random_person is vaccinated:
            #     nothing happens to random person.
            # random_person is already infected:
            #     nothing happens to random person.
            # random_person is healthy, but unvaccinated:
            #     generate a random number between 0.0 and 1.0.  If that number is smaller
            #     than repro_rate, add that person to the newly infected array
            #     Simulation object's newly_infected array, so that their infected
            #     attribute can be changed to True at the end of the time step.
        # TODO: Call logger method during this method.
        if random_person.is_vaccinated is True:
            self.vaccine_saved += 1
        elif random_person.is_vaccinated is False and random_person.infection is None:
            if random_num < repro_rate:
                self.newly_infected.append(random_person)
                self.people.remove(random_person)
                


    def _infect_newly_infected(self):
        # TODO: Call this method at the end of every time step and infect each Person.
        # TODO: Once you have iterated through the entire list of self.newly_infected, remember
        # to reset self.newly_infected back to an empty list.
        for infected in self.newly_infected:
            infected.infection is self.virus
            self.people.append(infected)
            self.total_infected += 1
        self.newly_infected = []


if __name__ == "__main__":
    # Test your simulation here
    virus_name = "Sniffles"
    repro_rate = 0.5
    mortality_rate = 0.12
    # virus = Virus(virus_name, repro_num, mortality_rate)

    # Set some values used by the simulation
    pop_size = 2000
    vacc_percentage = 0.1
    initial_infected = 20

    # Make a new instance of the simulation
    virus = Virus(virus_name, repro_rate, mortality_rate)
    sim = Simulation(virus, pop_size, vacc_percentage, initial_infected)

    sim.run()
