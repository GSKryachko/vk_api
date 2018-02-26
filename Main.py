from FollowerPrinter import *
import argparse


parser = argparse.ArgumentParser(description='Returns list of followers of requested user')
parser.add_argument('user_id', type=int, help='User id')
parser.add_argument('token', type=str, help='Access token', nargs='?')
parser.add_argument('count', type=int, help='Number of users to return', nargs='?', default=100)
args = parser.parse_args()

followers = get_followers(args.user_id, args.count, args.token)
print_followers(followers)
