from typing import List
    
def part1(lines: List[str]):
    result = 0

    for line in lines:
        _, output = line.split(" | ")
        result += sum([1 for o in output.split(" ") if (len(o) <= 4 or len(o) == 7)])

    return result

def part2(lines: List[str]):
    outputs = 0

    for line in lines:
        signals, output = line.split(" | ")
        signals = [set(x) for x in sorted(signals.split(" "), key=lambda y: len(y))]

        t = signals[1] - signals[0]

        for signal in signals[6:-1]:
            if (signals[2] | t) < signal:
                b = signal - (signals[2] | t)
        bl = signals[-1] - (signals[2] | t | b)

        for signal in signals[6:-1]:
            if (signals[1] | b | bl) < signal:
                tl = signal - (signals[1] | b | bl)
        m = signals[2] - (signals[0] | tl)

        for signal in signals[3:6]:
            if tl < signal:
                    br = signal - (t | tl | m | b)

        tr = signals[0] - br

        _map = [(t|tl|tr|bl|br|b), (tr|br), (t|tr|m|bl|b), (t|tr|m|br|b), (tl|tr|m|br), 
                (t|tl|m|br|b), (t|tl|m|bl|br|b), (t|tr|br), (t|tl|tr|m|bl|br|b), (t|tl|tr|m|br|b)]

        outputs += int("".join([str(_map.index(set(o))) for o in output.split(" ")]))

    return outputs