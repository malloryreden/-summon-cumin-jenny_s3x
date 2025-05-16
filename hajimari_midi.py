from midiutil import MIDIFile

midi = MIDIFile(1)
track = 0
time = 0
tempo = 80
channel = 0
volume = 100

midi.addTempo(track, time, tempo)

note_sequence = [
    ("shi", 52, 1),
    ("zu", 50, 1),
    ("ka", 48, 1),
    ("na", 50, 1),
    ("ka", 52, 1),
    ("ze", 53, 1),
    ("ga", 52, 2),
    ("sot", 50, 1),
    ("to", 48, 1),
    ("sa", 47, 1),
    ("sa", 48, 1),
    ("ya", 50, 1),
    ("ku", 52, 1),
    ("no", 50, 2),
]

current_time = time
for syllable, pitch, duration in note_sequence:
    midi.addNote(track, channel, pitch, current_time, duration, volume)
    current_time += duration

with open("hajimari_verse1.mid", "wb") as output_file:
    midi.writeFile(output_file)