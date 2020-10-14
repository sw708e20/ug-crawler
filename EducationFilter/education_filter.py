import json

edu_type_translations = {
    'msc programme': 'Masters',
    'master programme': 'Masters',
    'erhvervsakademiuddannelse': 'Academies profession',
    'ma programme': 'Masters',
    'kandidatuddannelse': 'Masters',
    'bacheloruddannelse': 'Bachelors',
    'akademiuddannelse': 'Academies Programme',
    'professionsbacheloruddannelse': 'Professional bachelor',
    'diplomuddannelse': 'Diploma',
    'professional bachelor programme': 'Professional bachelor',
    'pædagogisk diplomuddannelse': 'Diploma',
    'teknologisk diplomuddannelse': 'Diploma',
    'politi og forsvar': 'Police and military',
    'ba programme': 'Bachelors',
    'kunstnerisk uddannelse': 'Artistic education',
    'sundhedsfaglig diplomuddannelse': 'Diploma',
    'academy profession programme': 'Academies profession',
    'bsc programme': 'Bachelors',
    'masteruddannelse': 'Masters',
    'andre uddannelser': 'Other educations',
    'msocsc': 'Masters',
    'arbejdsmarkedsuddannelse (amu)': 'Labor market training',
}

class Education:
    def __init__(self, dictionary):
        self.name = dictionary['name']
        self.edu_type = {
            edu_type_translations[dictionary['edu_type'].lower().strip()]: dictionary['link']
        }
        self.description = dictionary['description']


file = open("../educations_V2.json", 'r')
educations = json.load(file)

edu_dict = dict()
for education in educations:
    if education['edu_type'].lower().strip() in edu_type_translations:
        if education['name'] in edu_dict:
            edu_dict[education['name']].edu_type[edu_type_translations[education['edu_type'].lower().strip()]] = education['link']
        else:
            edu_dict[education['name']] = Education(education)

output_file = open('../educations_normalized.json', 'w')
output_file.write('[')
for education in edu_dict.values():
    json.dump(education.__dict__, output_file, ensure_ascii=False)
    output_file.write(',\n')
output_file.write(']')
output_file.close()
