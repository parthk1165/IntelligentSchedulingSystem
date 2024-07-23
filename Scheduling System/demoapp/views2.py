from django.shortcuts import render
import random
from tabulate import tabulate


DAYS_IN_WEEK_TE = 4
LECTURES_PER_DAY_TE = 4  # 3 theory sessions and 1 practical/tutorial
TOTAL_SUBJECTS_TE = 5

SUBJECTS_TE = ["CNW", "PDC", "PM", "AJP",]
PRACTICAL_SUBJECTS_TE = ["CNWp", "PDCp", "AJPp", "MPp"]

DAYS_IN_WEEK_BE = 4
LECTURES_PER_DAY_BE = 3  # 3 theory sessions and 1 practical
TOTAL_SUBJECTS_BE = 3

SUBJECTS_BE = ["FOC", "AD", "DM"]
PRACTICAL_SUBJECTS_BE = ["FOCp", "ADp", "DBMp", "IAEp"]

DAYS_IN_WEEK_SE = 5
LECTURES_PER_DAY_SE = 4  # 3 theory sessions and 1 practical/tutorial
TOTAL_SUBJECTS_SE = 5

SUBJECTS_SE = ["SS", "CS", "PCS", "OOP","EMPSKD"]
PRACTICAL_SUBJECTS_SE = ["OOPp", "PCSp", "PBLp", "DAp","SCSp"]
TUTORIALS_SE = ["SSt"]

DIVISIONS = ["SE1","SE2","TE1","TE2","BE1","BE2"]
MAX_MUTATION_ATTEMPTS = 5
PRACTICALS_PER_WEEK = 1  # 1 practical per week

TEACHERS = {
      "SE1": {
        "SS": "PGS",
        "CS": "MPP",
        "PCS": "SRL",
        "OOP":"VUG",
        "EMPSKD":"HPK",
        "OOPp": "VUG",
        "PCSp": "SRL",
        "PBLp": "RKP",
        "DAp": "TTK",
        "SCSp":"PGS",
        "SSt":"PGS"
    },
    "SE2": {
        "SS": "MHB",
        "CS": "SRJ",
        "PCS": "SRL",
        "OOP":"NDC",
        "EMPSKD":"HPK",
        "OOPp": "NDC",
        "PCSp": "ASN",
        "PBLp": "GAK",
        "DAp": "SRL",
        "SCSp":"MHB",
        "SSt":"MHB"
    },
     "TE1": {
        "CNW": "KJK",
        "PDC": "SKB",
        "AJP": "NDC",
        "PM":"HPK",
        "CNWp": "KJK",
        "PDCp": "SKB",
        "AJPp": "NDC",
        "MPp": "GAK",
    },
    "TE2": {
        "CNW": "MHB",
        "PDC": "YBT",
        "AJP": "VVS",
        "PM":"HPK",
        "CNWp": "MHB",
        "PDCp": "YBT",
        "AJPp": "VVS",
        "MPp": "RKP",
    },
    "BE1": {
        "FOC": "TSK",
        "AD": "NDC",
        "DM": "GAK",
        "FOCp": "TSK",
        "ADp": "NDC",
        "DBMp": "RKP",
        "IAEp": "MHB",
    },
    "BE2": {
         "FOC": "PSD",
        "AD": "VVS",
        "DM": "GAK",
        "FOCp": "PSD",
        "ADp": "VVS",
        "DBMp": "NDK",
        "IAEp": "PGS",
    }
}

index_names_BE = ["Mon", "Tue", "Wed", "Thu"]
index_names_TE = [ "Tue", "Wed", "Thu","fri"]
index_names_SE = [ "mon","Tue", "Wed", "Thu","fri"]

headers_TE = ["10-11", "11-12", "12-1", "1-2","2-3","3-5"]
headers_BE = ["","10-11", "11-12", "12-1", "1-3"]
headers_SE = ["10-11", "11-12", "12-1", "1-3","3-4","4-5"]

def max_lectures_SE(subject):
  if subject == "EMPSKD":
     return 2
  elif subject == "SSt":
    return 1
  return 3

def generate_timetable_population(population_size):
    population = []
    for _ in range(population_size):
        timetable = {division: [] for division in DIVISIONS}
        #practicals_assigned = {division: {subject: 0 for subject in PRACTICAL_SUBJECTS} for division in DIVISIONS}
        #subjects_assigned = {division: {subject: 0 for subject in SUBJECTS} for division in DIVISIONS}

        for division in DIVISIONS:
          if division in ["TE1","TE2"]:
            PRACTICAL_SUBJECTS = PRACTICAL_SUBJECTS_TE
            SUBJECTS = SUBJECTS_TE
            DAYS_IN_WEEK = DAYS_IN_WEEK_TE
            practicals_assigned = {division: {subject: 0 for subject in PRACTICAL_SUBJECTS} for division in DIVISIONS}
            subjects_assigned = {division: {subject: 0 for subject in SUBJECTS} for division in DIVISIONS}
            for day in range(DAYS_IN_WEEK):
                    daily_schedule = []
                    time_slot = 0
                # Monday, Tuesday, and Thursday
                    if day in [2, 3] and time_slot==0:
                       daily_schedule.append(("", ""))
                       time_slot+=1
                       # 10-11 slot is blank

                    # 2 theory sessions and 1 practical
                    #subject = random.choice(SUBJECTS)
                    while time_slot<5:
                        if time_slot == 2:
                          daily_schedule.append(("Lunch", "-"))
                          time_slot+=1
                          continue
                        if day==0 and time_slot in [3, 4]:
                          daily_schedule.append(("MPp", TEACHERS[division]["MPp"]))
                          time_slot+=1
                          continue
                        subject = random.choice(SUBJECTS)
                        while subjects_assigned[division][subject] >= 3:
                           # print(division,day,time_slot,subject)
                            subject = random.choice(SUBJECTS)
                        subjects_assigned[division][subject] += 1
                        daily_schedule.append((subject, TEACHERS[division][subject]))
                        time_slot+=1


                    # Generate practical (ensuring only 1 practical per week)
                    practicals = [subject for subject in PRACTICAL_SUBJECTS if practicals_assigned[division][subject] < PRACTICALS_PER_WEEK]
                    if len(practicals) > 0:
                        practical = random.choice(practicals)
                        practicals_assigned[division][practical] += 1
                        daily_schedule.append((practical, TEACHERS[division][practical]))
                    else:
                        daily_schedule.append(("Rest"))  # If all practicals for the week are assigned
                    #print(daily_schedule
                    timetable[division].append(daily_schedule)

          if division in ["BE1","BE2"]:
            PRACTICAL_SUBJECTS = PRACTICAL_SUBJECTS_BE
            SUBJECTS = SUBJECTS_BE
            DAYS_IN_WEEK = DAYS_IN_WEEK_BE
            practicals_assigned = {division: {subject: 0 for subject in PRACTICAL_SUBJECTS} for division in DIVISIONS}
            subjects_assigned = {division: {subject: 0 for subject in SUBJECTS} for division in DIVISIONS}
            for day in range(DAYS_IN_WEEK):
                daily_schedule = []

                # Monday, Tuesday, and Thursday
                if day in [0, 1, 3]:
                    # 10-11 slot is blank
                    daily_schedule.append(("", ""))

                    # 2 theory sessions and 1 practical
                    theory_subjects = random.sample(SUBJECTS, k=2)
                    for subject in theory_subjects:
                        while subjects_assigned[division][subject] >= 3:
                            subject = random.choice(SUBJECTS)
                        subjects_assigned[division][subject] += 1
                        daily_schedule.append((subject, TEACHERS[division][subject]))

                    # Generate practical (ensuring only 1 practical per week)
                    practicals = [subject for subject in PRACTICAL_SUBJECTS if practicals_assigned[division][subject] < PRACTICALS_PER_WEEK]
                    if len(practicals) > 0:
                        practical = random.choice(practicals)
                        practicals_assigned[division][practical] += 1
                        daily_schedule.append((practical, TEACHERS[division][practical]))
                    else:
                        daily_schedule.append(("Rest"))  # If all practicals for the week are assigned

                # Wednesday
                elif day == 2:
                    # 3 theory sessions from 10-1 and 1 practical
                    theory_subjects = random.sample(SUBJECTS, k=3)
                    for subject in theory_subjects:
                        while subjects_assigned[division][subject] >= 3:
                            subject = random.choice(SUBJECTS)
                        subjects_assigned[division][subject] += 1
                        daily_schedule.append((subject, TEACHERS[division][subject]))

                    # Generate practical (ensuring only 1 practical per week)
                    practicals = [subject for subject in PRACTICAL_SUBJECTS if practicals_assigned[division][subject] < PRACTICALS_PER_WEEK]
                    if len(practicals) > 0:
                        practical = random.choice(practicals)
                        practicals_assigned[division][practical] += 1
                        daily_schedule.append((practical, TEACHERS[division][practical]))
                    else:
                        daily_schedule.append(("Rest"))  # If all practicals for the week are assigned



                timetable[division].append(daily_schedule)

          if division in ["SE1","SE2"]:
            PRACTICAL_SUBJECTS = PRACTICAL_SUBJECTS_SE
            SUBJECTS = SUBJECTS_SE
            DAYS_IN_WEEK = DAYS_IN_WEEK_SE
            practicals_assigned = {division: {subject: 0 for subject in PRACTICAL_SUBJECTS} for division in DIVISIONS}
            subjects_assigned = {division: {subject: 0 for subject in SUBJECTS} for division in DIVISIONS}

            for day in range(DAYS_IN_WEEK):
                    daily_schedule = []
                    time_slot = 0
                # Monday, Tuesday, and Thursday
                    #if day in [2, 3] and time_slot==0:
                     #  daily_schedule.append(("", ""))
                      # time_slot+=1
                       # 10-11 slot is blank

                    # 2 theory sessions and 1 practical
                    #subject = random.choice(SUBJECTS)
                    while time_slot<6:
                        if time_slot == 2:
                          daily_schedule.append(("Lunch", "-"))
                          time_slot+=1
                          continue
                        if time_slot == 3:
                          practicals = [subject for subject in PRACTICAL_SUBJECTS if practicals_assigned[division][subject] < PRACTICALS_PER_WEEK]
                          if len(practicals) > 0:
                             practical = random.choice(practicals)
                             practicals_assigned[division][practical] += 1
                             daily_schedule.append((practical, TEACHERS[division][practical]))
                          time_slot+=1
                          continue
                        if time_slot == 5 and day == 0:
                          daily_schedule.append(("SSt", TEACHERS[division]["SSt"]))
                          time_slot+=1
                          continue

                        if day == 4 and time_slot in [4,5]:
                          daily_schedule.append(("PBLp",TEACHERS[division]["PBLp"]))
                          time_slot+=1
                          continue

                        if time_slot == 5:
                          daily_schedule.append(("Rest", "-"))
                          time_slot+=1
                          continue
                        if day == 4 and time_slot in [4,5]:
                          daily_schedule.append(("PBLp",TEACHERS[division]["PBLp"]))
                          time_slot+=1

                        subject = random.choice(SUBJECTS)
                        while subjects_assigned[division][subject] >= max_lectures_SE(subject):
                           # print(division,day,time_slot,subject)
                            subject = random.choice(SUBJECTS)
                        subjects_assigned[division][subject] += 1
                        daily_schedule.append((subject, TEACHERS[division][subject]))
                        time_slot+=1


                    # Generate practical (ensuring only 1 practical per week)

                    #print(daily_schedule
                    timetable[division].append(daily_schedule)



        population.append(timetable)
    return population


# Calculate fitness of a timetable (implement your own fitness function)
def calculate_fitness(timetable):
    fitness = 1000  # Initialize fitness value

    SUBJECTS = SUBJECTS_SE + SUBJECTS_TE + SUBJECTS_BE
    PRACTICAL_SUBJECTS = PRACTICAL_SUBJECTS_SE + PRACTICAL_SUBJECTS_TE + PRACTICAL_SUBJECTS_BE

    # Constraint: Avoid clashes in the timetable
    '''for division, days in timetable.items():
        for day_idx, day_schedule in enumerate(days):
            for hour_idx, schedule in enumerate(day_schedule):
                for other_div, other_days in timetable.items():
                    if other_div != division:
                        other_schedule = other_days[day_idx][hour_idx]
                        if schedule[0] == other_schedule[0] and schedule[1] == other_schedule[1]:
                            fitness -= 1000  # Penalize clashes heavily'''

    # Constraint: Ensure each subject lectures three times per week
    lectures_per_subject = {division: {subject: 0 for subject in SUBJECTS} for division in DIVISIONS}
    for division, days in timetable.items():
        for day_schedule in days:
            for schedule in day_schedule:
                if schedule[0] in SUBJECTS:
                    lectures_per_subject[division][schedule[0]] += 1

    for division, subjects in lectures_per_subject.items():
        for count in subjects.values():
            if count != 3:  # Penalize any deviations from three lectures
                fitness -= 50  # Adjust penalty value based on deviation

    # Constraint: Ensure practical sessions are at the end
    for division, days in timetable.items():
        for day_schedule in days:
            practical_present = any(schedule[0] in PRACTICAL_SUBJECTS for schedule in day_schedule)
            if practical_present and day_schedule[-1][0] not in PRACTICAL_SUBJECTS:
                fitness -= 50  # Penalize if practical sessions are not at the end

    # Constraint: Allocate a rest day
    '''rest_day = random.choice(index_names)
    for division, days in timetable.items():
        if rest_day not in index_names:
            fitness += 20  # Encourage having a rest day'''

    return fitness

# Select parents based on fitness
def select_parents(population, num_parents):
    parents = []
    population_size = len(population)
    for _ in range(num_parents):
        selected = random.choice(population)
        parents.append(selected)
    return parents

# Crossover to create a child timetable
def crossover(parent1, parent2,crossover_division):
    offspring = {division: [] for division in DIVISIONS}
    for division in DIVISIONS:
        offspring_schedule = []
        if division in ["SE1", "SE2"]:
          DAYS_IN_WEEK = DAYS_IN_WEEK_SE
        elif division in ["TE1", "TE2"]:
          DAYS_IN_WEEK = DAYS_IN_WEEK_TE
        else:
          DAYS_IN_WEEK = DAYS_IN_WEEK_BE
        for day in range(DAYS_IN_WEEK):
            daily_schedule = []

            if division == crossover_division:
                for idx, subject in enumerate(parent1[division][day]):
                        daily_schedule.append(subject)
            else:
                for idx, subject in enumerate(parent2[division][day]):
                        daily_schedule.append(subject)

            offspring_schedule.append(daily_schedule)

        offspring[division] = offspring_schedule

    return offspring

# Mutate a timetable to introduce variation
def mutate(timetable):
    for _ in range(MAX_MUTATION_ATTEMPTS):
        mutation_division = random.choice(DIVISIONS)
        if mutation_division in ["SE1", "SE2"]:
            DAYS_IN_WEEK = DAYS_IN_WEEK_SE
            LECTURES_PER_DAY = LECTURES_PER_DAY_SE
            SUBJECTS = SUBJECTS_SE
        elif mutation_division in ["TE1", "TE2"]:
            DAYS_IN_WEEK = DAYS_IN_WEEK_TE
            LECTURES_PER_DAY = LECTURES_PER_DAY_TE
            SUBJECTS = SUBJECTS_TE
        else:
            DAYS_IN_WEEK = DAYS_IN_WEEK_BE
            LECTURES_PER_DAY = LECTURES_PER_DAY_BE
            SUBJECTS = SUBJECTS_BE
        mutation_day = random.choice(range(DAYS_IN_WEEK))
        mutation_hour = random.choice(range(LECTURES_PER_DAY - 1))
        mutation_subject = random.choice(SUBJECTS)


        ''''replacement_day = random.choice(range(DAYS_IN_WEEK))
        replacement_hour = random.choice(range(LECTURES_PER_DAY-1))
        while(timetable[mutation_division][replacement_day][replacement_hour] != mutation_subject):
          replacement_day = random.choice(range(DAYS_IN_WEEK))
          replacement_hour = random.choice(range(LECTURES_PER_DAY-1))'''

        swap = timetable[mutation_division][mutation_day][mutation_hour]
        timetable[mutation_division][mutation_day][mutation_hour] = mutation_subject
        timetable[mutation_division][mutation_day][mutation_hour] = swap

    # Implement your mutation logic here
        return timetable  # Replace with your own logic

# Main genetic algorithm loop
def genetic_algorithm(population_size, num_generations, num_parents):
    population = generate_timetable_population(population_size)
    for generation in range(num_generations):
        # Evaluate fitness
        fitness_scores = [calculate_fitness(timetable) for timetable in population]

        # Select parents
        parents = select_parents(population, num_parents)

        new_population = []
        while len(new_population) < population_size:
            parent1, parent2 = random.sample(parents, 2)
            crossover_division = random.choice(DIVISIONS)
            child = crossover(parent1, parent2,crossover_division)
            child = mutate(child)
            new_population.append(child)

        population = new_population

    # Find the best timetable in the final population
    best_timetable = min(population, key=calculate_fitness)
    return best_timetable

if __name__ == "__main__":
    population_size = 50
    num_generations = 100
    num_parents = population_size // 10  # Use 10% of the population size as the number of parents
    best_timetable = genetic_algorithm(population_size, num_generations, num_parents)

    # Display timetable for Monday to Thursday
    print("Best Timetable:")
    for division, timetable in best_timetable.items():
        print(f"Division: {division}")
        # Headers for the table
        if division in ["SE1","SE2"]:
          headers = headers_SE
          index_names = index_names_SE
        elif division in ["TE1","TE2"]:
          headers = headers_TE
          index_names = index_names_TE
        else:
          headers = headers_BE
          index_names = index_names_BE
        #headers = ["10-11", "11-12", "12-1", "1-2","2-3","3-5"]
        # Print the table using tabulate function
        print(tabulate(timetable, headers=headers, tablefmt="pretty", showindex=index_names))

def timetable_view2(request):
    # Assuming these values are coming from user input or some other source
    population_size = 50
    num_generations = 100
    num_parents = population_size // 10  # Use 10% of the population size as the number of parents
    best_timetable = genetic_algorithm(population_size, num_generations, num_parents)

    # Prepare timetable data for rendering in HTML template
    timetable_data = []
    for division, timetable in best_timetable.items():
        division_data = {'division': division, 'table_html': ''}

        # Headers for the table
        if division in ["SE1", "SE2"]:
            headers = ["10-11", "11-12", "12-1", "1-2", "2-3", "3-5"]
            index_names = ["Mon", "Tue", "Wed", "Thu", "Fri"]
        elif division in ["TE1", "TE2"]:
            headers = ["10-11", "11-12", "12-1", "1-2", "2-3"]
            index_names = ["Tue", "Wed", "Thu", "Fri"]
        else:
            headers = ["10-11", "11-12", "12-1", "1-2", "2-3"]
            index_names = ["Mon", "Tue", "Wed", "Thu"]

        # Generate HTML table using tabulate function
        division_data['table_html'] = tabulate(timetable, headers=headers, tablefmt="html", showindex=index_names)
        timetable_data.append(division_data)

    # Render the HTML template with the timetable data
    return render(request, 'demoapp/home2.html', {'timetable_data': timetable_data})
