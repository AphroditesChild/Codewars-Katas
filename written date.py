def format_duration(seconds):

    y = seconds//3600//24//365
    dd = seconds//3600//24%365
    hh = seconds//3600%24
    mm = seconds//60%60
    ss = seconds%60

    nums = [y, dd, hh, mm, ss]
    written = ["year", "day", "hour", "minute","second"]

    duration = [str(n)+" "+w+"s" if n>1 else str(n)+" "+w for n,w in zip(nums,written) if n >0]

    return ", ".join(duration[:-1]) + " and " + duration[-1] if len(duration) > 1 else duration[0]



print(format_duration(3601))

input()
