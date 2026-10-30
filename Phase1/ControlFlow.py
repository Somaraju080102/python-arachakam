# 1. if / elif / else

score = 72

if score >= 90:
    grade = "A"
elif score >= 60:
    grade = "B"
else:
    grade = "C"

print(f"Score: {score}, Grade: {grade}")    

# 2. for loops (these are Java’s for-each, always)

for server in ["web1", "web2", "db1"]:
    print(server,end=" ")

print()

for i in range(5):          # 0,1,2,3,4
    print(i,end=" ")

print()

for i in range(2, 10, 3):   # start, stop, step -> 2,5,8
    print(i,end=" ")

print()
# 3. enumerate and zip (replace 90% of index juggling)

servers = ["web1", "web2", "db1"]
ips = ["10.0.0.1", "10.0.0.2", "10.0.0.3"]

for idx, s in enumerate(servers, start=1):
    print(idx, s)

for s, ip in zip(servers, ips):
    print(f"{s} -> {ip}")

# 4. while, break, continue

attempts = 0
while attempts < 3:
    attempts += 1
    if attempts == 2:
        continue        # skip rest of this round
    print(attempts)

# 5. The weird one: else on loops

for n in [1, 3, 5]:
    if n % 2 == 0:
        print("found even")
        break
else:
    print("no even numbers")   # runs only if loop did NOT break


# 6. match-case (Python 3.10+, like Java’s switch on steroids)

status = 404

match status:
    case 200:
        print("OK")
    case 404 | 410:
        print("gone")
    case code if code >= 500:
        print("server error")
    case _:
        print("other")