import django
from theapplication.models import RaceChoice, SchoolChoice


with open("schools.csv") as f:
    for school in f:
        s = SchoolChoice(school_string=school.strip())
        s.save()


with open("races.csv") as f:
    for race in f:
        r = RaceChoice(race_string=race.strip())
        r.save()
