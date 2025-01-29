# function to compare followers and return the most
def compare(data_A, data_B):
    if data_A['follower_count'] > data_B['follower_count']:
        return 'A'
    elif data_B['follower_count'] > data_A['follower_count']:
        return 'B'