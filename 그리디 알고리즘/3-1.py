money = 1260
cnt = 0

# 그리디 알고리즘이기 때문에 큰 화폐 단위부터 사용
cointypes = [500, 100, 50, 10]
for i in cointypes:
  cnt += (money // i)
  money %= i

print(cnt)