def ips_between(start, end):
    s = [int(i) for i in start.split('.')]
    e = [int(i) for i in end.split('.')]
    return (((e[0] - s[0]) * 256 + e[1] - s[1]) * 256 + e[2] - s[2]) * 256 + e[3] - s[3]

print(ips_between("10.0.0.1", "25.255.3.14"))
input()
