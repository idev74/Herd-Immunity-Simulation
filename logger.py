class Logger(object):
    def __init__(self, file_name):
        self.file_name = file_name
        

   
    # What is important is that you log the following information from the simulation:
    # Meta data: This shows the starting situtation including:
    #   population, initial infected, the virus, and the initial vaccinated.
    # Log interactions. At each step there will be a number of interaction
    # You should log:
    #   The number of interactions, the number of new infections that occured
    # You should log the results of each step. This should inlcude: 
    #   The population size, the number of living, the number of dead, and the number 
    #   of vaccinated people at that step. 
    # When the simulation concludes you should log the results of the simulation. 
    # This should include: 
    #   The population size, the number of living, the number of dead, the number 
    #   of vaccinated, and the number of steps to reach the end of the simulation. 

    def write_metadata(self, pop_size, vacc_percentage, virus):

        f = open(self.file_name, 'w') # maybe 'w'?
        f.write(
            f'Population: {pop_size} people \t Percent Vaccinated {vacc_percentage} \t Virus Name: {virus.name} \t Mortality Rate: {virus.mortality_rate} \t Basic Reproduction Number {virus.repro_rate}\n'
        )
        f.close()

    def log_interactions(self, step_number, number_of_interactions, number_of_new_infections):
        f = open(self.file_name, 'a')
        f.write(
            f'Step No.: {step_number} \t Interactions: {number_of_interactions} \t New Infections: {number_of_new_infections}\n'
        )
        f.close()
        # TODO: Finish this method. Think about how the booleans passed (or not passed)
        # represent all the possible edge cases. Use the values passed along with each person,
        # along with whether they are sick or vaccinated when they interact to determine
        # exactly what happened in the interaction and create a String, and write to your logfile.

    def log_infection_survival(self, step_number, population_count, number_of_new_fatalities):
        deaths = 0
        for fatality in number_of_new_fatalities:
            if not fatality.is_alive:
                deaths += 1

        f = open(self.file_name, 'a')
        f.write(
            f'Step No.: {step_number} \t Population Count: {population_count} \t New Deaths: {number_of_new_fatalities}\n'
        )
        f.close()
        # TODO: Finish this method. If the person survives, did_die_from_infection
        # should be False.  Otherwise, did_die_from_infection should be True.
        # Append the results of the infection to the logfile
       

    def log_time_step(self, time_step_number):
        f = open(self.file_name, 'a')
        f.write(
            f'Time Step No.: {time_step_number}'
        )
        f.close()