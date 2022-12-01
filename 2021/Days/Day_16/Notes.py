# NOTES
"""
data is one big packet

extra 0s at the end - ignore

Standard Packet Header
Bits 
1-3 : VERSION
4-6 : TYPE ID
    4 = literal value
        encode a single binary number
        padded at front by 0s 
            until length is multiple of 4 bits
            then split into groups, 
                prefixed by 1, 0 if last group
    other - operator
        contains other packets
        length type id 
        - 0 
            next 15 bits = total length of contained bits
                of subpackets
        - 1 len 11
            next 11 bits represent the number of subpackets
                contained by the packet


"""