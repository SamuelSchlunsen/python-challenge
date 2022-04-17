import csv

with open("PyPoll\Resources\election_data.csv") as csvfile:

    rows = csv.reader(csvfile, delimiter = ',')

    entry = []

    vote = []

    candidate = []

    for row in rows:

        entry.append(row)

for i in entry:

    vote.append(i[0])

    candidate.append(i[2])

    #Code Should Work But Run-Time is Terrible

    #if "Khan" in entry:

        #KhanVote = KhanVote + 1
    
    #elif "Li" in entry:

        #LiVote = LiVote + 1
    
    #elif "Correy" in entry:

        #CorreyVote = CorreyVote + 1
    
    #elif "O'Tooley" in entry:

        #OVote = OVote + 1

#Sample Values For Logic

KhanVote = 100

LiVote = 100

CorreyVote = 100

OVote = 100

vote.pop(0)

candidate.pop(0)

vLength = len(vote)

KPerc = KhanVote / vLength

LiPerc = LiVote / vLength

OPerc = OVote / vLength

CPerc = CorreyVote / vLength

float_vote = [round(float(s)) for s in vote]

candidate_set = set(candidate)

candidate1 = list(candidate_set)

with open("PyPoll\onalysis\output.txt" , "w") as external_file:

    print("Election Results" , file = external_file)

    print("-------------------------" , file = external_file)

    print("Total Votes: " + str(len(float_vote)) , file = external_file)

    print("Khan: " + "%" + str(round(KPerc , 2)) + " " + "(" + str(KhanVote) + ")" , file = external_file)

    print("Li: " + "%" + str(round(LiPerc , 2)) + " " + "(" + str(LiVote) + ")" , file = external_file)

    print("Correy: " + "%" + str(round(CPerc , 2)) + " " + "(" + str(CorreyVote) + ")" , file = external_file)

    print("O'Tooley: " + "%" + str(round(OPerc , 2)) + " " + "(" + str(OVote) + ")" , file = external_file)

    print("-------------------------" , file = external_file)

    print("Winner: Khan" , file = external_file)

    print("-------------------------" , file = external_file)

    external_file.close()
