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
        self.logger = Logger('logger.txt')
        self.people = self._create_population()
        self.newly_infected = []
        self.num_vaccinated = self.pop_size * self.vacc_percentage
        self.num_unvaccinated = self.pop_size - self.num_vaccinated
        self.vaccine_saved = 0
        self.total_interactions = 0
        self.death_count = 0
        self.time_step_counter = 0
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
        people = []
        infected = 0
        id = 0
        # id_num = id += 1
        infected = self.initial_infected
#  self._id = _id  # int
#         self.is_vaccinated = is_vaccinated
#         self.infection = infection
#         self.is_alive = True

        for i in range (self.num_vaccinated):
            people.append(Person((id + 1), True, None))

        for i in range (infected):
            people.append(Person((id + 1), False, self.virus))


        for i in range (self.num_unvaccinated):
            people.append(Person((id + 1), False, None))

        return people
        # vaxx, unvaxx, infected; append to people with statistics per person (infection = virus/None, vaxx = true, etc.)

        

    def _simulation_should_continue(self):
        # survivors = len(self.people) written by self
        # This method will return a boolean  indicating if the simulation 
        # should continue. 
        # The simulation should not continue if all of the people are dead, 
        # or if all of the living people have been vaccinated. 
        # TODO: Loop over the list of people in the popualation. Return True
        # if the simulation should continue or False if not.

        for person in self.population:
            if person.is_vaccinated == False and person.is_alive == True:
                return True
            return False # idk what this line does

    def run(self):
        # This method starts the simulation. It should track the number of 
        # steps the simulation has run and check if the simulation should 
        # continue at the end of each step. 
        self.time_step
        self.time_step_counter = 0
        should_continue = True

        while should_continue:
            # TODO: Increment the time_step_counter
            # TODO: for every iteration of this loop, call self.time_step() 
            # Call the _simulation_should_continue method to determine if 
            # the simulation should continue
            should_continue = self._simulation_should_continue()
            time_step_counter += 1
            self.time_step()
            print(f'Step {time_step_counter}:\nNumber Infected: {len(self.newly_infected)}')
            

        # TODO: Write meta data to the logger. This should be starting 
        # statistics for the simulation. It should include the initial
        # population size and the virus. 

        self.logger.write_metadata(self.pop_size, self.vacc_percentage, virus_name, mortality_rate, repro_num)
        # TODO: When the simulation completes you should conclude this with 
        # the logger. Send the final data to the logger. 

    def time_step(self):
        # This method will simulate interactions between people, calulate 
        # new infections, and determine if vaccinations and fatalities from infections
        # The goal here is have each infected person interact with a number of other 
        # people in the population
        # TODO: Loop over your population
        # For each person if that person is infected
        # have that person interact with 100 other living people 
        # Run interactions by calling the interaction method below. That method
        # takes the infected person and a random person
        self.logger.log_time_step(self.time_step_counter)

    def interaction(self, infected_person, random_person):
        # TODO: Finish this method.
        assert infected_person.is_alive == True
        assert random_person.is_alive == True
        self.total_interactions +=1
        random_num = random.randint(0.0, 1.0)
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
            if random_num > repro_num:
                if random_person not in self.newly_infected:
                    self.newly_infected.append(random_person)

        self.logger.log_interactions(self.time_step_counter, self.total_interactions, len(self.newly_infected))

    def _infect_newly_infected(self):
        # TODO: Call this method at the end of every time step and infect each Person.
        # TODO: Once you have iterated through the entire list of self.newly_infected, remember
        # to reset self.newly_infected back to an empty list.
        for infected in self.newly_infected:
            infected.infection is virus
            self.newly_infected.append(infected)
        self.newly_infected = []


if __name__ == "__main__":
    # Test your simulation here
    virus_name = "Sniffles"
    repro_num = 0.5
    mortality_rate = 0.12
    virus = Virus(virus_name, repro_num, mortality_rate)

    # Set some values used by the simulation
    pop_size = 1000
    vacc_percentage = 0.1
    initial_infected = 10

    # Make a new instance of the simulation
    virus = Virus(virus, pop_size, vacc_percentage, initial_infected)
    sim = Simulation(pop_size, vacc_percentage, initial_infected, virus)

    # sim.run()
