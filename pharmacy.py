
class Drug:
    def __init__(self, name, expires_in, benefit):
        self.name = name
        self.expires_in = expires_in
        self.benefit = benefit

class Pharmacy:
    def __init__(self, drugs=None):
        self.drugs = drugs if drugs is not None else []

    def update_benefit_value(self):
        for drug in self.drugs:
            if drug.name != "Herbal Tea" and drug.name != "Fervex":
                if drug.benefit > 0:
                    if drug.name != "Magic Pill":
                        drug.benefit -= 1
            else:
                if drug.benefit < 50:
                    drug.benefit += 1
                    if drug.name == "Fervex":
                        if drug.expires_in < 11:
                            if drug.benefit < 50:
                                drug.benefit += 1
                        if drug.expires_in < 6:
                            if drug.benefit < 50:
                                drug.benefit += 1
            if drug.name != "Magic Pill":
                drug.expires_in -= 1
            if drug.expires_in < 0:
                if drug.name != "Herbal Tea":
                    if drug.name != "Fervex":
                        if drug.benefit > 0:
                            if drug.name != "Magic Pill":
                                drug.benefit -= 1
                    else:
                        drug.benefit = drug.benefit - drug.benefit
                else:
                    if drug.benefit < 50:
                        drug.benefit += 1
        return self.drugs
