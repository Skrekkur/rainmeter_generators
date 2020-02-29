from disktemplate import header

import string
from ctypes import windll

totalDiskTemplate = '''
[measureTotalDisk1]
; This measure returns the total disk space
Measure=FreeDiskSpace
Drive=#disk1#
Total=1
UpdateDivider=120
'''


def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1

    return drives

def get_drive_strings():
    result_strings = []
    drives = get_drives()
    counter = 1
    for drive in drives:
        result_strings.append(f"drive{counter}={drive}:")
        counter = counter+1
    return result_strings

drivestrings = get_drive_strings()
diskvars = "\n".join(get_drive_strings())


def get_total_disk_string(extravar):
    return f'''
[measureTotalDisk{extravar}]
; This measure returns the total disk space
Measure=FreeDiskSpace
Drive=#disk{extravar}#
Total=1
UpdateDivider=120
'''

def get_used_disk_string(extravar):
    return f'''
[measureTotalDisk{extravar}]
; This measure returns the total disk space
Measure=FreeDiskSpace
Drive=#disk{extravar}#
Total=1
UpdateDivider=120
'''

total_disk_measures = []

for number in range(len(drivestrings)):
    total_disk_measures.append(get_total_disk_string(number+1))

    print(number)

print(f"{header}"
      f"{diskvars}"
      f"{get_total_disk_string(2)}")

#print ("\n".join(get_drive_strings()))

#print(get_drive_strings() )


#testString = f"hello : {get_drive_strings()

#print (testString)