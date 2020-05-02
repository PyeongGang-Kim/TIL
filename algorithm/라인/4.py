'''

'''

def solution(snapshots, transactions):
    D = dict()
    transaction_chk = set()
    for account in snapshots:
        D[account[0]] = int(account[1])
    for transaction in transactions:
        if transaction[0] not in transaction_chk:
            transaction_chk.add(transaction[0])
            if transaction[1] == "SAVE":
                if D.get(transaction[2]):
                    D[transaction[2]] += int(transaction[3])
                else:
                    D[transaction[2]] = int(transaction[3])
            else:
                if D.get(transaction[2]):
                    D[transaction[2]] -= int(transaction[3])
                else:
                    D[transaction[2]] = -int(transaction[3])

    answer = [[accoun_name, str(balance)] for accoun_name, balance in D.items()]
    answer.sort(key=lambda x: x[0])
    return answer

snapshots, transactions =[
  ["ACCOUNT1", "100"],
  ["ACCOUNT2", "150"]
], [
  ["1", "SAVE", "ACCOUNT2", "100"],
  ["2", "WITHDRAW", "ACCOUNT1", "50"],
  ["1", "SAVE", "ACCOUNT2", "100"],
  ["4", "SAVE", "ACCOUNT3", "500"],
  ["3", "WITHDRAW", "ACCOUNT2", "30"]
]