import pandas as pd

#directions_data = pd.read_csv('data.csv')

def user_data(user_input):
    user_input_dict = {}
    user_input = user_input.split()
    if 'русский' in user_input:
        subject_index = user_input.index('русский') 
        user_input[subject_index:subject_index+2] = [' '.join(user_input[subject_index:subject_index+2])] 
    if 'иностранный' in user_input:
        subject_index = user_input.index('иностранный') 
        user_input[subject_index:subject_index+2] = [' '.join(user_input[subject_index:subject_index+2])]  
    key = None
    for word in user_input:
        if user_input.index(word) % 2 == 0:
            key = word
        else:
            user_input_dict[key] = int(word)
    return user_input_dict

def all_subjects(user_input, data):
    all_subjects = []
    for subject in user_input.keys():
        result = data.loc[data['entrance_tests'] == subject]
        result_list = list(result.program_spec.values)
        all_subjects += result_list
    all_subjects.sort()
    check_list = []
    final_result = []
    count = 0
    for prog in all_subjects:
        if prog in check_list:
            count += 1
            if count == 3:
                final_result.append(prog)
        else:
            count = 1
            check_list.append(prog)
    return final_result

def check_score(user_input, subject_list, data):
    final_result = []
    for subject in subject_list:
        program_data = data.loc[data['program_spec']==subject]
        program_dict = dict(zip(list(program_data.entrance_tests), list(program_data.min_score)))
        if len(program_dict) > len(user_input):
            continue
        count = 0
        for user_subject in user_input:
            try:
                if program_dict[user_subject] > user_input[user_subject]:
                    break
                else:
                    count += 1
                    if count == 3:
                        final_result.append(subject)
            except KeyError:
                continue
    return final_result

def output(user_input, data):
    user_querry = user_data(user_input)
    check_subjects = all_subjects(user_querry, data)
    result = check_score(user_querry, check_subjects, data)
    return result

