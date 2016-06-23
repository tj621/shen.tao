'''
2016/06/20
@author: Zxh
'''
from serial_output import println
from control import Control

Query_all="FE 01 00 00 00 08 29 C3"
Query_all_return="01 01 00 00 61 9C"
co=Control()

def get_control_state(str1,Control):
#     print control.build_json()
    return_message=delete_blank(str1)
    relay_number=string_to_bin(return_message[0:2])
    relay_state=return_message[4:6]
    relay_bin=string_to_bin(relay_state)
#     print 'relay_state:'+relay_number
#     print 'ralay_number:'+relay_bin
    get_relay_state(relay_number[7],relay_bin,Control)
    print Control.build_json()

def get_all_state():
    out_str=Query_all
    println(out_str)
    return Query_all_return

def delete_blank(str1):
    x=str1.split()
    return ''.join(x)
    
def get_relay_state(relay_number,relay_state,Control):
    if relay_number=='1':
        if relay_state[0]==relay_state[1]:
            if relay_state[0]=='0':        #0 means off
                Control.set_roof_vent_south("stop")
            else:
                print 'roof_vent_south error'
        elif relay_state[0]=='1' and relay_state[1]=='0':
            Control.set_roof_vent_south("on")
        elif relay_state[0]=='0' and relay_state[1]=='1':
            Control.set_roof_vent_south("off")
        
        if relay_state[2]==relay_state[3]:
            if relay_state[2]=='0':        #0 means off
                Control.set_roof_vent_north("stop")
            else:
                print 'roof_vent_south error'
        elif relay_state[2]=='1' and relay_state[3]=='0':
            Control.set_roof_vent_north("on")
        elif relay_state[2]=='0' and relay_state[3]=='1':
            Control.set_roof_vent_north("off")
            
        if relay_state[4]==relay_state[5]:
            if relay_state[4]=='0':        #0 means off
                Control.set_side_vent("stop")
            else:
                print 'roof_vent_south error'
        elif relay_state[4]=='1' and relay_state[5]=='0':
            Control.set_side_vent("on")
        elif relay_state[4]=='0' and relay_state[5]=='1':
            Control.set_side_vent("off")
            
        if relay_state[6]==relay_state[7]:
            if relay_state[6]=='0':        #0 means off
                Control.set_shade_screen_out("stop")
            else:
                print 'roof_vent_south error'
        elif relay_state[6]=='1' and relay_state[7]=='0':
            Control.set_shade_screen_out("on")
        elif relay_state[6]=='0' and relay_state[7]=='1':
            Control.set_shade_screen_out("off")
    
    elif relay_number=='2':
        if relay_state[0]==relay_state[1]:
            if relay_state[0]=='0':        #0 means off
                Control.set_shade_screen_in("stop")
            else:
                print 'roof_vent_south error'
        elif relay_state[0]=='1' and relay_state[1]=='0':
            Control.set_shade_screen_in("on")
        elif relay_state[0]=='0' and relay_state[1]=='1':
            Control.set_shade_screen_in("off")
            
        if relay_state[2]==relay_state[3]:
            if relay_state[2]=='0':        #0 means off
                Control.set_thermal_screen("stop")
            else:
                print 'roof_vent_south error'
        elif relay_state[2]=='1' and relay_state[3]=='0':
            Control.set_thermal_screen("on")
        elif relay_state[2]=='0' and relay_state[3]=='1':
            Control.set_thermal_screen("off")
        
        if relay_state[4]=='1':
            Control.set_cooling_pad("on")
        else:
            Control.set_cooling_pad("off")
            
        if relay_state[5]=='1':
            Control.set_fogging("on")
        else:
            Control.set_fogging("off")
            
        if relay_state[6]=='1':
            Control.set_heating("on")
        else:
            Control.set_heating("off")
            
        if relay_state[7]=='1':
            Control.set_co_2("on")
        else:
            Control.set_co_2("off")

    elif relay_number=='3':
        if relay_state[0]=='1':
            Control.set_lighting_1("on")
        else:
            Control.set_lighting_1("off")
        
        if relay_state[1]=='1':
            Control.set_lighting_2("on")
        else:
            Control.set_lighting_2("off")
        
        if relay_state[2]=='1':
            Control.set_irrigation("on")
        else:
            Control.set_irrigation("off")
    else:
        print 'relay_nymber error'

def string_to_bin(str_in):
    a='{0:b}'.format(int(str_in,16))
    if len(str(a))<7:
        str2=''
        for i in range(8-len(str(a))):
            str2+='0'
    return str2+str(a)

# str2="EF"
# print '{0:b}'.format(int(str2,16))
# get_control_state(Query_all_return,co)
