# Creates quizzes with questions and answers in # random order, along with the answer key.
import random

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 
'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 
'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 
'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 
'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 
'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 
'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 
'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 
'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 
'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

#generate 35 quiz files
for quiz_num in range(35):
    # create the quiz and answer key files
    quiz_file = open(f'capitalsquiz{quiz_num + 1}.txt','w')
    answer_key_file = open(f'capitalsQuizAnswers{quiz_num + 1}.txt','w')

    #write out the header for the quiz
    quiz_file.write("Name:\n\nDate:\n\nPeriod:\n\n")
    quiz_file.write(('' * 20) + f'State Capitals Quiz (Form{quiz_num + 1})')
    quiz_file.write('\n\n')

    # shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states)
    