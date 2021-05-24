# -*- coding: utf-8 -*-
"""
Created on Mon May 24 09:36:02 2021

@author: 7064554
"""

#split each score component into team and score
def team_score_split(team_score):
    space_split = team_score.split(' ');
    score = space_split[len(space_split)-1];
    team = ' '.join(space_split[0:len(space_split)-1]).strip();
    return team, score;

#populate the match parameters from a given result
def get_match_paramters(match):
    home_team, home_score = team_score_split(match[0]);
    away_team, away_score = team_score_split(match[1]);
    if home_score > away_score:
        outcome = home_team;
        home_points_gained = 3;
        away_points_gained = 0;
    elif home_score < away_score:
        outcome = away_team;
        home_points_gained = 0;
        away_points_gained = 3;
    else:
        outcome = 'Draw';
        home_points_gained = 1;
        away_points_gained = 1;
    return home_team, home_score, away_team, away_score, outcome, home_points_gained, away_points_gained;


#loop through each line in the input file
def calculate_league_table (textfile_path):
    league_table = [];
    with open(textfile_path, 'r') as f:
         for line in f.readlines():
             #seperate each match into team-score tuples
             match = line.strip().split(',');
             #calculate match parameters
             home_team, home_score, away_team, away_score, outcome, home_points_gained, away_points_gained = get_match_paramters(match)
     
             #add to array if not in the table
             if not home_team in  [row[0] for row in league_table]:
                 league_table.append([home_team, 0])
             if not away_team in  [row[0] for row in league_table]:
                 league_table.append([away_team, 0])
            
             #update the table
             league_table[[row[0] for row in league_table].index(home_team)][1] = league_table[[row[0] for row in league_table].index(home_team)][1] + home_points_gained;
             league_table[[row[0] for row in league_table].index(away_team)][1] = league_table[[row[0] for row in league_table].index(away_team)][1] + away_points_gained;
            
    #sort the league table        
    league_table =sorted(league_table, key=lambda x:(-x[1],x[0]))
    
    #create ranks
    position = 1
    ranks = [];
    increment = 1;
    for index in range(len(league_table)):
        current_score = [row[1] for row in league_table][index]
        ranks.append(position)
        if index < len(league_table) - 1:
            next_score  = [row[1] for row in league_table][index + 1]     
            if current_score > next_score:
                position = position + increment
                increment = 1
            elif current_score == next_score:
                increment = increment + 1
                
    
    #output results
    for index in range(len(league_table)):
         measure = "pts"
         if [row[1] for row in league_table][index] == 1:
             measure = "pt"
         print (ranks[index], ".", " ", [row[0] for row in league_table][index], ", ", [row[1] for row in league_table][index], " ", measure, sep='')                


#run the calculation for all textfiles in a given directory
def test_files_from_directory(directory):
    import os
    
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            #print os.path.join(subdir, file)
            filepath = subdir + os.sep + file
    
            if filepath.endswith(".txt"):
               calculate_league_table(filepath)
               print()
               
               

#store file path data;
directory = "C:/Users/7064554/Documents/Coding Challenge";
file_name = "matches1.txt";
path = directory + "/" + file_name;

#calculate the league table for one table
calculate_league_table(path)
print()
#calculate the league table for all tables in the directory
test_files_from_directory(directory)            
                 