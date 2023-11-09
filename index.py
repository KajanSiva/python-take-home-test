from pharmacy import Drug, Pharmacy
import json

# Initialization of drugs and pharmacy
drugs = [
    Drug("Doliprane", 20, 30),
    Drug("Herbal Tea", 10, 5),
    Drug("Fervex", 5, 40),
    Drug("Magic Pill", 15, 40)
]
trial = Pharmacy(drugs)

# Collecting logs over 30 days
log = []
for elapsed_days in range(30):
    log.append(json.dumps([{"name": drug.name, "expiresIn": drug.expires_in, "benefit": drug.benefit} for drug in trial.update_benefit_value()]))

# Writing the log to a file
with open('output.txt', 'w') as file:
    for entry in log:
        file.write(entry + "\n")

print("success")