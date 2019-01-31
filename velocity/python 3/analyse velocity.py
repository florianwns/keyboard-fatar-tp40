"""
Anlyse velocity from MIDI Monitor log, and make some stats
"""
import matplotlib.pyplot as plt

v = set()
for line in open('midilog.txt'):
    v.add(int(line.split()[-1]))
v = list(v)
ecart = [0]+[v[i+1]-v[i] for i in range(len(v) - 1)]
nb = len(v)
f = ''.join(['{:<4}'] * nb)

print("Set    :", f.format(*v))
print("Ecart  :", f.format(*ecart))
print("Min Ec  :", min(ecart))
print("Max Ec  :", max(ecart))
print("Max Ve  :", max(v))
print("Nombre :", nb)



"""
Results :

Set    : 0   3   4   5   8   9   10  11  13  15  16  17  19  20  21  22  23  24  26  27  29  30  32  33  34  37  38  40  42  43  44  45  47  49  50  51  53  54  56  57  59  60  61  63  66  67  69  70  72  73  75  76  78  80  83  85  88  89  91  93  94  96  98  99  101 103 105 107 108 110 112 114 116 117 119 121 125 127
Ecart  : 0   3   1   1   3   1   1   1   2   2   1   1   2   1   1   1   1   1   2   1   2   1   2   1   1   3   1   2   2   1   1   1   2   2   1   1   2   1   2   1   2   1   1   2   3   1   2   1   2   1   2   1   2   2   3   2   3   1   2   2   1   2   2   1   2   2   2   2   1   2   2   2   2   1   2   2   4   2
Min Ec  : 0
Max Ec  : 4
Max Ve  : 127
Nombre : 78

-----------------

KEYBOARD n=1   rows=12  dout_sr1=1  dout_sr2=2  din_sr1=1  din_sr2=2 \
               din_inverted=0  break_inverted=0  din_key_offset=40 \
               scan_velocity=1 scan_optimized=1  note_offset=21 \
               delay_fastest=30  delay_fastest_black_keys=28  delay_slowest=250 \
               make_debounced=0

# using an interpolation map to define the velocity curve
MAP1/BYTEI  0:1 10:7 30:15 62:30 79:49 85:72 100:98 120:127

1  22  23  24  25  26  27  28  29  30  31  32  34  35  36  37  38  40  41  42  43  44  45  46  47  49  52  56  60  64  68  72  73  75  77  78  80  82  84  85  87  89  91  92  94  96  98  99  100 102 103 106 108 109 111 112 113 115 116 118 119 121 122 124 125 127
Ecart  : 0   1   1   2   1   1   1   1   1   1   1   1   1   1   1   1   1   1   1   1   1   1   1   1   1   1   1   1   1   1   1   1   2   1   1   1   1   2   1   1   1   1   1   1   1   2   3   4   4   4   4   4   1   2   2   1   2   2   2   1   2   2   2   1   2   2   2   1   1   2   1   3   2   1   2   1   1   2   1   2   1   2   1   2   1   2
Min Ec  : 0
Max Ec  : 4
Max Ve  : 127
Nombre : 86

-----------------


"""
