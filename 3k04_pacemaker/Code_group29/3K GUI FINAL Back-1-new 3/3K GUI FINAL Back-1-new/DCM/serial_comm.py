import serial
import struct


def writePara(mode=0, Lower_Rate=60, MSR=120, AV_Delay=150, ATR_Amplitude=75, VENT_Amplitude=75, ATR_Width=10,
              VENT_Width=10,
              VENT_Refractory=320, ATR_Refractory=250, Activity_Threshold=2, Reaction_Time=5, Response_Factor=10,
              Recovery_Time=5):
    ser = serial.Serial(port='COM4', baudrate=115200)
    # mode = 1
    # Lower_Rate = 60
    # MSR = 120
    # AV_Delay = 150
    #
    # ATR_Amplitude = 75
    # VENT_Amplitude = 75
    #
    # ATR_Width = 10
    # VENT_Width = 10
    #
    # VENT_Refractory = 320
    # ATR_Refractory = 250
    #
    # Activity_Threshold = 2
    # Reaction_Time = 5
    # Response_Factor = 10
    # Recovery_Time = 5

    Header = '<3B3H2B8H'
    spk = struct.pack(Header, 0x16, 0x55, mode, Lower_Rate, MSR, AV_Delay, ATR_Amplitude, VENT_Amplitude,
                      ATR_Width, VENT_Width, VENT_Refractory, ATR_Refractory, Activity_Threshold, Reaction_Time,
                      Response_Factor, Recovery_Time)

    ser.write(spk)
    ser.close()


if __name__ == '__main__':
    writePara()
