import heapq


def calculate_min_cost_of_joining(cables_lengths):
    heapq.heapify(cables_lengths)
    cost_sum = 0

    while len(cables_lengths) > 1:
        cable1 = heapq.heappop(cables_lengths)
        cable2 = heapq.heappop(cables_lengths)
        sum_cables = cable1 + cable2
        print(f'Current Joining lengths: {cable1} + {cable2} = {sum_cables}')
        cost_sum += sum_cables
        heapq.heappush(cables_lengths, sum_cables)

    return cost_sum


if __name__ == "__main__":
    cables_lengths = [4, 12, 3, 8, 5, 1]
    print(f'Cables lengths: {cables_lengths}')
    print(f'Total Min Cost of joining: {calculate_min_cost_of_joining(cables_lengths)}')
