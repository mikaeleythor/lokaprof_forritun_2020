def get_vote(vote_str):
    """
    This function takes in a vote string and returns the candidate and int(votes) and keep_counting bool
    if vote string is valid
    """
    if vote_str == '':
        return None, None, False
    if ' ' in vote_str:
        name, votes = vote_str.split()
    else:
        return None, False, True
    try:
        int(votes)
    except ValueError as identifier:
        return name, False, True
    return name, int(votes), True
    
def register_vote(votes_dict, name, vote_int):
    name = name.lower()
    if name in votes_dict:
        votes_dict[name]+=vote_int
    elif name not in votes_dict:
        votes_dict[name]=vote_int


def total_votes(votes_dict):
    total_votes = 0
    for votes in votes_dict.values():
        total_votes+=votes
    return total_votes

def print_votes(votes_dict):
    """
    This function prents alphabetically sorted results of the election
    """
    results = []
    for candidate, votes in votes_dict.items():
        results.append(f'{candidate}: {votes}')
    results.sort()
    print('\n'.join(results))
    print(f'Total no. of votes: {total_votes(votes_dict)}')

# Main program starts here
count = True
votes_dict = {}
while count:
    name, valid_vote, count = get_vote(input('Candidate and votes: '))
    if count:
        if not valid_vote:
            print('Invalid no. of votes!')
        else:
            register_vote(votes_dict, name, valid_vote)

print_votes(votes_dict)