from django.shortcuts import render
import random
from tabulate import tabulate

# Paste all the functions and constants from your provided code here


# Constants for SE Division
SUBJECTS_SE = ["DXC", "ELEXC", "EC", "DS", "M-III"]
PRACTICAL_SUBJECTS_SE = ["DXCp", "ELEXCp", "ECp", "DSp"]
TUTORIAL_SE = ["M-IIIt"]
SUBJECTS_TE = ["FJP", "DC", "EMFT", "MC", "DBMS"]
PRACTICAL_SUBJECTS_TE = ["FJPp", "DCp", "MCp", "DBMSp"]
TUTORIAL_TE = ["EMFTt"]
SUBJECTS_BE = ["JS", "VLSI", "RMT", "CC", "DL"]
PRACTICAL_SUBJECTS_BE = ["JSp", "VLSIp", "RMTp", "CCp"]
DIVISIONS = ["SE1", "SE2","TE1","TE2","BE1","BE2"]
MAX_MUTATION_ATTEMPTS = 5

LECTURES_BEFORE_LUNCH = 3
LECTURES_PER_DAY=4
DAYS_IN_WEEK=5

# Teachers for each subject and division for SE Division
TEACHERS = {
    "SE1": {
        "DXC": "SKB",
        "ELEXC": "YBT",
        "EC": "NDK",
        "DS": "MPP",
        "M-III": "ASS",
        "DXCp": "SKB",
        "ELEXCp": "YBT",
        "ECp": "NDK",
        "DSp": "MPP",
        "M-IIIt": "ASS"
    },
    "SE2": {
        "DXC": "PMB",
        "ELEXC": "ASN",
        "EC": "SJB",
        "DS": "DVV",
        "M-III": "RS",
        "DXCp": "PMB",
        "ELEXCp": "ASN",
        "ECp": "SJB",
        "DSp": "DVV",
        "M-IIIt": "RS"
    },
    "TE1": {
        "FJP": "NDC",
        "DC": "ASN",
        "EMFT": "VG",
        "MC": "SKB",
        "DBMS": "ASN",
        "FJPp": "NDC",
        "DCp": "ASN",
        "MCp": "SKB",
        "DBMSp": "ASN",
        "EMFTt": "VG"
    },
    "TE2": {
        "FJP": "VVS",
        "DC": "SLB",
        "EMFT": "RKP",
        "MC": "SKB",
        "DBMS": "DVV",
        "FJPp": "VVS",
        "DCp": "AD",
        "MCp": "VVS",
        "DBMSp": "DVV",
        "EMFTt": "RKP"
    },
    "BE1": {
        "JS": "VS",
        "VLSI": "VG",
        "RMT": "TK",
        "CC": "RC",
        "DL": "DV",
        "JSp": "NC",
        "VLSIp": "VG",
        "RMTp": "TK",
        "CCp": "RC",
    },
    "BE2": {
        "JS": "VS",
        "VLSI": "AD",
        "RMT": "YBT",
        "CC": "SRL",
        "DL": "RC",
        "JSp": "VS",
        "VLSIp": "AD",
        "RMTp": "YBT",
        "CCp": "SRL",
    }
}

# Index names for the table
index_names = ["Mon", "Tue", "Wed", "Thu", "Fri"]

#def check_teacher_busy(timetable,subject,day,hour):
  #for other_div in TEACHERS:
   #   if other_div in timetable and TEACHERS[other_div][timetable[other_div][day][hour]] == TEACHERS[other_div][subject]:
    #    return True

 # return False

def generate_se_timetable(timetable):
  division_schedule = []
  practicals_scheduled = {subject: False for subject in PRACTICAL_SUBJECTS_SE}
  subjects_lectures = {subject: 0 for subject in SUBJECTS_SE}
  for day in range(DAYS_IN_WEEK):
                daily_schedule = []

                # Assigning three lectures before lunch
                for _ in range(LECTURES_BEFORE_LUNCH):
                    subject = random.choice([subj for subj in SUBJECTS_SE if subjects_lectures[subj] < 3])
                    daily_schedule.append(subject)
                    subjects_lectures[subject] += 1
                daily_schedule.append("Lunch")  # Adding lunch break from 1-2
                # Assigning one practical/tutorial session after lunch
                if day < DAYS_IN_WEEK - 1:  # Not Friday
                    available_practicals = [subj for subj, scheduled in practicals_scheduled.items() if not scheduled]
                    if available_practicals:
                        practical = random.choice(available_practicals)
                        daily_schedule.append(practical)
                        practicals_scheduled[practical] = True
                    else:
                        daily_schedule.append(random.choice(PRACTICAL_SUBJECTS_SE))
                else:  # Friday
                    daily_schedule.append(random.choice(TUTORIAL_SE))
                division_schedule.append(daily_schedule)
  return division_schedule

def generate_te_timetable(timetable):
  division_schedule = []
  practicals_scheduled = {subject: False for subject in PRACTICAL_SUBJECTS_TE}
  subjects_lectures = {subject: 0 for subject in SUBJECTS_TE}
  for day in range(DAYS_IN_WEEK):
                daily_schedule = []

                # Assigning three lectures before lunch
                for _ in range(LECTURES_BEFORE_LUNCH):
                    subject = random.choice([subj for subj in SUBJECTS_TE if subjects_lectures[subj] < 3])
                    daily_schedule.append(subject)
                    subjects_lectures[subject] += 1
                daily_schedule.append("Lunch")  # Adding lunch break from 1-2
                # Assigning one practical/tutorial session after lunch
                if day < DAYS_IN_WEEK - 1:  # Not Friday
                    available_practicals = [subj for subj, scheduled in practicals_scheduled.items() if not scheduled]
                    if available_practicals:
                        practical = random.choice(available_practicals)
                        daily_schedule.append(practical)
                        practicals_scheduled[practical] = True
                    else:
                        daily_schedule.append(random.choice(PRACTICAL_SUBJECTS_TE))
                else:  # Friday
                    daily_schedule.append(random.choice(TUTORIAL_TE))
                division_schedule.append(daily_schedule)
  return division_schedule

def generate_be_timetable(timetable):
  division_schedule = []
  practicals_scheduled = {subject: False for subject in PRACTICAL_SUBJECTS_BE}
  subjects_lectures = {subject: 0 for subject in SUBJECTS_BE}
  for day in range(DAYS_IN_WEEK):
                daily_schedule = []

                # Assigning three lectures before lunch
                for _ in range(LECTURES_BEFORE_LUNCH):
                    subject = random.choice([subj for subj in SUBJECTS_BE if subjects_lectures[subj] < 3])
                    daily_schedule.append(subject)
                    subjects_lectures[subject] += 1
                daily_schedule.append("Lunch")  # Adding lunch break from 1-2
                # Assigning one practical/tutorial session after lunch
                if day < DAYS_IN_WEEK - 1:  # Not Friday
                    available_practicals = [subj for subj, scheduled in practicals_scheduled.items() if not scheduled]
                    if available_practicals:
                        practical = random.choice(available_practicals)
                        daily_schedule.append(practical)
                        practicals_scheduled[practical] = True
                    else:
                        daily_schedule.append(random.choice(PRACTICAL_SUBJECTS_BE))
                division_schedule.append(daily_schedule)
  return division_schedule

# Function to generate timetables for SE Division
def generate_timetable_population(population_size):
    population = []
    for _ in range(population_size):
        timetable = {division: [] for division in DIVISIONS}
        for division in DIVISIONS:
            division_schedule = []
            if division == "SE1" or division == "SE2":
              division_schedule = generate_se_timetable(timetable)
            elif division == "TE1" or division == "TE2":
              division_schedule = generate_te_timetable(timetable)
            elif division == "BE1" or division == "BE2":
              division_schedule = generate_be_timetable(timetable)

            timetable[division] = division_schedule
        population.append(timetable)
    return population

def calculate_fitness(timetable):
    fitness = 1000

    for division, days in timetable.items():
        for day_idx, day_schedule in enumerate(days):
            for hour_idx, schedule in enumerate(day_schedule):
                for other_div, other_days in timetable.items():
                    if other_div != division and day_idx < len(other_days) and hour_idx < len(other_days[day_idx]) :
                        other_schedule = other_days[day_idx][hour_idx]
                        if schedule[0] == other_schedule[0] and schedule[1] == other_schedule[1]:
                            fitness -= 100

    for division, days in timetable.items():
        if division == "SE1" or division == "SE2":
          SUBJECTS = SUBJECTS_SE
        elif division == "TE1" or division == "TE2":
          SUBJECTS = SUBJECTS_TE
        else :
          SUBJECTS = SUBJECTS_BE
        for day_schedule in days:
            theory_lectures = sum(1 for schedule in day_schedule if schedule[0] in SUBJECTS)
            if theory_lectures != 3:
                fitness -= abs(3 - theory_lectures)

    for division, days in timetable.items():
        if division == "SE1" or division == "SE2":
          PRACTICAL_SUBJECTS = PRACTICAL_SUBJECTS_SE
        elif division == "TE1" or division == "TE2":
          PRACTICAL_SUBJECTS = PRACTICAL_SUBJECTS_TE
        else :
          PRACTICAL_SUBJECTS = PRACTICAL_SUBJECTS_BE
        for day_schedule in days:
            practical_present = any(schedule[0] in PRACTICAL_SUBJECTS for schedule in day_schedule)
            if practical_present and day_schedule[-1][0] not in PRACTICAL_SUBJECTS:
                fitness -= 50

    rest_day = random.choice(index_names)
    for division, days in timetable.items():
        if rest_day not in index_names:
            fitness += 20

    return fitness

def select_parents(population, num_parents):
    parents = []
    population_size = len(population)
    for _ in range(num_parents):
        selected = random.choice(population)
        parents.append(selected)
    return parents

def crossover(parent1, parent2, crossover_division):
    offspring = {division: [] for division in DIVISIONS}
    for division in DIVISIONS:
        offspring_schedule = []
        for day in range(DAYS_IN_WEEK):
            daily_schedule = []

            if division == crossover_division:
                for idx, subject in enumerate(parent1[division][day]):
                    if day == 4 and idx == LECTURES_PER_DAY - 1:
                        daily_schedule.append("EMFTt" if division == "TE1" and idx == 4 else subject)
                    else:
                        daily_schedule.append(subject)
            else:
                for idx, subject in enumerate(parent2[division][day]):
                    if day == 4 and idx == LECTURES_PER_DAY - 1:
                        daily_schedule.append("EMFTt" if division == "TE1" and idx == 4 else subject)
                    else:
                        daily_schedule.append(subject)

            offspring_schedule.append(daily_schedule)

        offspring[division] = offspring_schedule

    return offspring

def mutate(timetable):
    for _ in range(MAX_MUTATION_ATTEMPTS):
        mutation_division = random.choice(DIVISIONS)
        mutation_day = random.choice(range(DAYS_IN_WEEK))
        mutation_hour = random.choice(range(LECTURES_PER_DAY-1))

        if mutation_division == "SE1" or mutation_division == "SE2":
          SUBS=SUBJECTS_SE
        elif mutation_division == "TE1" or mutation_division == "TE2":
          SUBS=SUBJECTS_TE
        elif mutation_division == "BE1" or mutation_division == "BE2":
          SUBS=SUBJECTS_BE
        mutation_subject = random.choice(SUBS)

        ''''replacement_day = random.choice(range(DAYS_IN_WEEK))
        replacement_hour = random.choice(range(LECTURES_PER_DAY-1))
        while(timetable[mutation_division][replacement_day][replacement_hour] != mutation_subject):
          replacement_day = random.choice(range(DAYS_IN_WEEK))
          replacement_hour = random.choice(range(LECTURES_PER_DAY-1))'''

        swap = timetable[mutation_division][mutation_day][mutation_hour]
        timetable[mutation_division][mutation_day][mutation_hour] = mutation_subject
        timetable[mutation_division][mutation_day][mutation_hour] = swap

        #print(timetable[mutation_division][replacement_day][replacement_hour], " ", timetable[mutation_division][mutation_day][mutation_hour])

        #timetable[mutation_division][replacement_day][replacement_hour] , timetable[mutation_division][mutation_day][mutation_hour] = timetable[mutation_division][mutation_day][mutation_hour] , timetable[mutation_division][replacement_day][replacement_hour]

    return timetable

def genetic_algorithm(population_size, num_generations, num_parents):
    population = generate_timetable_population(population_size)
    for generation in range(num_generations):
        fitness_scores = [calculate_fitness(timetable) for timetable in population]

        parents = select_parents(population, num_parents)

        new_population = []
        while len(new_population) < population_size:
            crossover_division = random.choice(DIVISIONS)
            parent1, parent2 = random.sample(parents, 2)
            child = crossover(parent1, parent2, crossover_division)
            child = mutate(child)
            #child = mutate(parent1)
            new_population.append(child)

        population = new_population

    best_timetable = min(population, key=calculate_fitness)
    return best_timetable

if __name__ == "__main__":
    population_size = 20
    num_generations = 10
    num_parents = 2
    timetables = genetic_algorithm(population_size,num_generations,num_parents)
    #timetables = generate_timetable_population(10)
    #print(len(timetables))
    for division, timetable in timetables.items():
        print(f"Division: {division}")
        headers = ["Day","10-11", "11-12", "12-1", "1-2","2-4"]
        formatted_timetable = []
        for day_schedule in timetable:
            formatted_schedule = []
            for subject in day_schedule:
                if subject == "Rest":
                    formatted_schedule.append("Rest")
                elif subject == "Lunch":
                    formatted_schedule.append("Lunch")
                else:
                    if subject in TEACHERS[division]:
                        teacher = TEACHERS[division][subject]
                        formatted_schedule.append(f"'{subject}', '{teacher}'")
                    else:
                        formatted_schedule.append(subject)
            formatted_timetable.append(formatted_schedule)
        print(tabulate(formatted_timetable, headers=headers, tablefmt="pretty", showindex=index_names))
def timetable_view1(request):
    population_size = 20
    num_generations = 10
    num_parents = 2
    timetables = genetic_algorithm(population_size, num_generations, num_parents)

    formatted_timetables = {}
    for division, timetable in timetables.items():
        headers = ["Day", "10-11", "11-12", "12-1", "1-2", "2-4"]
        formatted_timetable = []
        for day_schedule in timetable:
            formatted_schedule = []
            for subject in day_schedule:
                if subject == "Rest":
                    formatted_schedule.append("Rest")
                elif subject == "Lunch":
                    formatted_schedule.append("Lunch")
                else:
                    if subject in TEACHERS[division]:
                        teacher = TEACHERS[division][subject]
                        formatted_schedule.append(f"'{subject}', '{teacher}'")
                    else:
                        formatted_schedule.append(subject)
            formatted_timetable.append(formatted_schedule)
        formatted_timetables[division] = tabulate(formatted_timetable, headers=headers, tablefmt="html", showindex=index_names)

    return render(request, 'demoapp/home1.html', {'formatted_timetables': formatted_timetables})





# Create your views here.
