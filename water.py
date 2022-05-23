def validate(N, points):
    if N == 2:
        return "safe"
    for i in range(1, len(points)-1):
        if (points[i-1]["y"] > points[i]["y"]) and (points[i+1]["y"] > points[i]["y"]):
            return "disaster"
    return "safe"

def run():
    while True:
        N = int(input())
        if N == 0:
            break
        points = []
        for i in range(N):
            point = input()
            points.append({
                "x":int(point.split()[0]),
                "y": int(point.split()[1]),
            })
        print(validate(N, points))


if __name__ == "__main__":
    run()

