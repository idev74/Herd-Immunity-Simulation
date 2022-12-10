class Virus(object):
    def __init__(self, name, repro_rate, mortality_rate):
        self.name = name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate

# Test this class
if __name__ == "__main__":
    virus = Virus("HIV", 0.8, 0.3)
    assert virus.name == "HIV"
    assert virus.repro_rate == 0.8
    assert virus.mortality_rate == 0.3

    virus = Virus("Rabies", 0.6, 0.1)
    assert virus.name == "Rabies"
    assert virus.repro_rate == 0.6
    assert virus.mortality_rate == 0.1

    virus = Virus("Chicken Pox", 0.7, 0.2)
    assert virus.name == "Chicken Pox"
    assert virus.repro_rate == 0.7
    assert virus.mortality_rate == 0.2