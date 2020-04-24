try:
    import requests, sys, time
    url = raw_input("Enter the URL: ")
    speed = input("Enter the speed[1-10]: ")
    speed = 1 / speed
    if "http://" in url or "https://" in url:
        pass
    else:
        url = "http://" + url
    num = 0
    while True:
        r = requests.get(url)
        num += 1
        sys.stdout.write("\r{} Requests Sent!".format(num))
        sys.stdout.flush()
        time.sleep(speed)
except Exception as e:
    print "An Error Occurred: " + str(e)