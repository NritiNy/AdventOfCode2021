from typing import List

def parse_packet(bits: str):
        version = int(bits[:3], 2)
        typeID = int(bits[3:6], 2)
        packet_length = 0

        value = 0
        sub_packets = []

        bits = bits[6:]
        packet_length += 6

        if typeID == 4:
            v = ""
            while bits[0] == "1":
                v += bits[1:5]
                bits = bits[5:] 
                packet_length += 5
            v += bits[1:5]
            bits = bits[5:] 
            packet_length += 5
            value = int(v, 2)
        else:
            l = 16 if bits[0] == "0" else 12
            total_length = int(bits[1:16], 2) if bits[0] == "0" else 0
            n_subpackets = int(bits[1:12], 2) if bits[0] == "1" else 0

            bits = bits[l:]
            packet_length += l

            while total_length > 0:
                sub_packet = parse_packet(bits)
                sub_packets.append(sub_packet)
                total_length -= sub_packet[-1]
                packet_length += sub_packet[-1]
                bits = bits[sub_packet[-1]:]

            while n_subpackets > 0:
                sub_packet = parse_packet(bits)
                sub_packets.append(sub_packet)
                n_subpackets -= 1
                packet_length += sub_packet[-1]
                bits = bits[sub_packet[-1]:]

        return version, typeID, value, sub_packets, packet_length
    
def part1(lines: List[str]):
    input_data = lines[0]
    bits = "".join([f"{int(b, 16):0>4b}" for b in input_data])

    main_packet = parse_packet(bits)

    version_sum = 0
    packets = [main_packet]
    while len(packets) > 0:
        p = packets.pop(0)
        version_sum += p[0]
        packets += p[-2]

    return version_sum

def part2(lines: List[str]):
    input_data = lines[0]
    bits = "".join([f"{int(b, 16):0>4b}" for b in input_data])
    
    main_packet = parse_packet(bits)

    def interpret_packet(packet):
        if packet[1] == 0:
            return sum([interpret_packet(p) for p in packet[-2]])
        elif packet[1] == 1:
            val = 1
            for p in [interpret_packet(p) for p in packet[-2]]:
                val *= p
            return val
        elif packet[1] == 2:
            return min([interpret_packet(p) for p in packet[-2]])
        elif packet[1] == 3:
            return max([interpret_packet(p) for p in packet[-2]])
        elif packet[1] == 4:
            return packet[2]
        elif packet[1] == 5:
            return 1 if interpret_packet(packet[-2][0]) > interpret_packet(packet[-2][1]) else 0
        elif packet[1] == 6:
            return 1 if interpret_packet(packet[-2][0]) < interpret_packet(packet[-2][1]) else 0
        elif packet[1] == 7:
            return 1 if interpret_packet(packet[-2][0]) == interpret_packet(packet[-2][1]) else 0

    return interpret_packet(main_packet)