


header = '''
; Lines starting ; (semicolons) are commented out.
; That is, they do not affect the code and are here for demonstration purposes only.
; ----------------------------------

; HOWTO: Adding more disks
; ----------------------------------
; Adding more disks is a pretty straightforward process. Follow the following steps to turn
; this 2 disks skin into a 3 disks skin. You can then extend it even further as you wish.
;
; 1) Create a new variable called disk3=X: directly below disk2=D: in the [Variables] section
; 2) Create a copy of the [measureTotalDisk2] and [measureUsedDisk2] sections
; 3) Rename the copied sections to [measureTotalDisk3] and [measureUsedDisk3], respectively.
;    Also change Drive=#disk2# to Drive=#disk3#
; 4) Create a copy of the [meterLabelDisk2], [meterValueDisk2], and [meterBarDisk2].
;    Rename all Disk2's in the copied sections to Disk3.
; 5) Now we need to change the Y= values to adjust height. Change Y= under [meterLabelDisk3]
;    to Y=80 (calculated by adding 20 to the Y= value of previous meterLabel).
;    Then change Y= under [meterBarDisk3] to Y=92 (calculated by adding 20 to the Y= value of previous meterBar).
; 6) Save the file as '3 Disks.ini'. Now right-click on the Rainmeter tray icon and select
;    'Refresh All'. Now go activate the '3 Disks.ini' skin and enjoy! :)

[Rainmeter]
; This section contains general settings that can be used to change how Rainmeter behaves.
Update=1000
Background=#@#Background.png
; #@# is equal to Rainmeter\Skins\illustro\@Resources
BackgroundMode=3
BackgroundMargins=0,34,0,14

[Metadata]
; Contains basic information of the skin.
Name=Disk
Author=poiru
Information=Displays disk usage.
License=Creative Commons BY-NC-SA 3.0
Version=1.0.0

[Variables]
; Variables declared here can be used later on between two # characters (e.g. #MyVariable#).
fontName=Trebuchet MS
textSize=8
colorBar=235,170,0,255
colorText=255,255,255,205
'''



"disk1=C:"
"disk2=D:"

'''
; ----------------------------------
; MEASURES return some kind of value
; ----------------------------------

[measureTotalDisk1]
; This measure returns the total disk space
Measure=FreeDiskSpace
Drive=#disk1#
Total=1
UpdateDivider=120

[measureUsedDisk1]
; Returns inverted value of free disk space (i.e. used disk space)
Measure=FreeDiskSpace
Drive=#disk1#
InvertMeasure=1
UpdateDivider=120

[measureTotalDisk2]
Measure=FreeDiskSpace
Drive=#disk2#
Total=1
UpdateDivider=120

[measureUsedDisk2]
Measure=FreeDiskSpace
Drive=#disk2#
InvertMeasure=1
UpdateDivider=120

; ----------------------------------
; STYLES are used to "centralize" options
; ----------------------------------

[styleTitle]
StringAlign=Center
StringCase=Upper
StringStyle=Bold
StringEffect=Shadow
FontEffectColor=0,0,0,50
FontColor=#colorText#
FontFace=#fontName#
FontSize=10
AntiAlias=1
ClipString=1

[styleLeftText]
StringAlign=Left
; Meters using styleLeftText will be left-aligned.
StringCase=None
StringStyle=Bold
StringEffect=Shadow
FontEffectColor=0,0,0,20
FontColor=#colorText#
FontFace=#fontName#
FontSize=#textSize#
AntiAlias=1
ClipString=1

[styleRightText]
StringAlign=Right
StringCase=None
StringStyle=Bold
StringEffect=Shadow
FontEffectColor=0,0,0,20
FontColor=#colorText#
FontFace=#fontName#
FontSize=#textSize#
AntiAlias=1
ClipString=1

[styleBar]
BarColor=#colorBar#
BarOrientation=HORIZONTAL
SolidColor=255,255,255,15

; ----------------------------------
; METERS display images, text, bars, etc.
; ----------------------------------

[meterTitle]
Meter=String
MeterStyle=styleTitle
; Using MeterStyle=styleTitle will basically "copy" the
; contents of the [styleTitle] section here during runtime.
X=100
Y=12
W=190
H=18
Text=Disks
; Even though the text is set to Disks, Rainmeter will display
; it as DISKS, because styleTitle contains StringCase=Upper.

[meterLabelDisk1]
Meter=String
MeterStyle=styleLeftText
X=10
Y=40
W=190
H=14
Text=#disk1#\

[meterValueDisk1]
Meter=String
MeterStyle=styleRightText
MeasureName=measureUsedDisk1
MeasureName2=measureTotalDisk1
X=200
Y=0r
; r stands for relative. In this case, the Y postition of meterValueCPU is 0 pixels
; below the Y value of the previous meter (i.e it's the same as in meterLabelCPU).
W=190
H=14
Text=%1B/%2B used
; %1 stands for the value of MeasureName (measureUsedDisk1 in this case).
; %2 stands for the value of MeasureName2.
NumOfDecimals=1
AutoScale=1
; Because disk measures return the free/used space in bytes, we must use AutoScale=1 to
; automatically scale the value into a more readable figure.
LeftMouseUpAction=["#disk1#\"]
; Open #disk1# on click

[meterBarDisk1]
Meter=Bar
MeterStyle=styleBar
MeasureName=measureUsedDisk1
X=10
Y=52
W=190
H=1

[meterLabelDisk2]
Meter=String
MeterStyle=styleLeftText
X=10
Y=60
W=190
H=14
Text=#disk2#\
LeftMouseUpAction=["#disk2#\"]

[meterValueDisk2]
Meter=String
MeterStyle=styleRightText
MeasureName=measureUsedDisk2
MeasureName2=measureTotalDisk2
X=200
Y=0r
W=190
H=14
Text=%1B/%2B used
NumOfDecimals=1
AutoScale=1

[meterBarDisk2]
Meter=Bar
MeterStyle=styleBar
MeasureName=measureUsedDisk2
X=10
Y=72
W=190
H=1
"
'''
