#!/usr/bin/env python3

class Citizen:
    def __init__(self, name: str, party: str):
        self.name = name
        self.party = party

        self.known_parties = set([
            "democrat",
            "republican",
            "green"])

        self._validate_inputs()

    def _validate_inputs(self):
        """
        lets see if everything is up to snuff
        """
        if self.name is None:
            raise ValueError(
                "Gotta know your name, bud")

        if self.party not in self.known_parties:
            raise KeyError(
                "Gotta run with one of these two.. *checks notes* ..three parties?")

class Government:
    def __init__(self):
        self.potus = None

    def presidential_election(self, new_president: Citizen):
        self.potus = new_president

    def current_state(self):
        if self.potus is not None:
            return "Not Anarchy"
        else:
            return "Anarchy"

    def __repr__(self) -> str:
        """
        string representation of object
        (called when object is printed)
        """
        if not self.potus:
            return f"No President, we are in : {self.current_state()}"
        else:
            return f"{self.current_state()} : {self.potus.name} in charge"


def main():

    obama = Citizen("Barack Obama", "democrat")
#    noam = Citizen("Noam Teyssier", "communist")

    gov = Government()
    print(gov)

    gov.presidential_election(obama)
    print(gov)

    gov.presidential_election(None)
    print(gov)

if __name__ == "__main__":
    main()
