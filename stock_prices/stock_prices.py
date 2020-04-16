#!/usr/bin/python

import argparse


def find_max_profit(prices):

    smallest_price = prices[0]
    largest_profit = prices[1]
    index = 0

    for i in range(1, len(prices)):
        if prices[i] > largest_profit:
            largest_profit = prices[i]
            index = i

    for i in range(0, index):
        if prices[i] < smallest_price:
            smallest_price = prices[i]

    return largest_profit - smallest_price


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
