'''

@author: Zxh
'''
from serial_output import println

first_1st_on="FE 05 00 00 FF 00 98 35"
first_1st_off="FE 05 00 00 00 00 D9 C5"
first_2nd_on="FE 05 00 01 FF 00 C9 F5"
first_2nd_off="FE 05 00 01 00 00 88 05"
first_3rd_on="FE 05 00 02 FF 00 39 F5"
first_3rd_off="FE 05 00 02 00 00 78 05"
first_4th_on="FE 05 00 03 FF 00 68 35"
first_4th_off="FE 05 00 03 00 00 29 C5"
first_5th_on="FE 05 00 04 FF 00 D9 F4"
first_5th_off="FE 05 00 04 00 00 98 04"
first_6th_on="FE 05 00 05 FF 00 88 34"
first_6th_off="FE 05 00 05 00 00 C9 C4"
first_7th_on="FE 05 00 06 FF 00 78 34"
first_7th_off="FE 05 00 06 00 00 39 C4"
first_8th_on="FE 05 00 07 FF 00 29 F4"
first_8th_off="FE 05 00 07 00 00 68 04"

first_1st=(first_1st_on,first_1st_off)
first_2nd=(first_2nd_on,first_2nd_off)
first_3rd=(first_3rd_on,first_3rd_off)
first_4th=(first_4th_on,first_4th_off)
first_5th=(first_5th_on,first_5th_off)
first_6th=(first_6th_on,first_6th_off)
first_7th=(first_7th_on,first_7th_off)
first_8th=(first_8th_on,first_8th_off)
first_relay=[first_1st,first_2nd,first_3rd,first_4th,first_5th,first_6th,first_7th,first_8th]



second_1st_on="FE 05 00 00 FF 00 98 35"
second_1st_off="FE 05 00 00 00 00 D9 C5"
second_2nd_on="FE 05 00 01 FF 00 C9 F5"
second_2nd_off="FE 05 00 01 00 00 88 05"
second_3rd_on="FE 05 00 02 FF 00 39 F5"
second_3rd_off="FE 05 00 02 00 00 78 05"
second_4th_on="FE 05 00 03 FF 00 68 35"
second_4th_off="FE 05 00 03 00 00 29 C5"
second_5th_on="FE 05 00 04 FF 00 D9 F4"
second_5th_off="FE 05 00 04 00 00 98 04"
second_6th_on="FE 05 00 05 FF 00 88 34"
second_6th_off="FE 05 00 05 00 00 C9 C4"
second_7th_on="FE 05 00 06 FF 00 78 34"
second_7th_off="FE 05 00 06 00 00 39 C4"
second_8th_on="FE 05 00 07 FF 00 29 F4"
second_8th_off="FE 05 00 07 00 00 68 04"

second_1st=(second_1st_on,second_1st_off)
second_2nd=(second_2nd_on,second_2nd_off)
second_3rd=(second_3rd_on,second_3rd_off)
second_4th=(second_4th_on,second_4th_off)
second_5th=(second_5th_on,second_5th_off)
second_6th=(second_6th_on,second_6th_off)
second_7th=(second_7th_on,second_7th_off)
second_8th=(second_8th_on,second_8th_off)
second_relay=[second_1st,second_2nd,second_3rd,second_4th,second_5th,second_6th,second_7th,second_8th]


third_1st_on="FE 05 00 00 FF 00 98 35"
third_1st_off="FE 05 00 00 00 00 D9 C5"
third_2nd_on="FE 05 00 01 FF 00 C9 F5"
third_2nd_off="FE 05 00 01 00 00 88 05"
third_3rd_on="FE 05 00 02 FF 00 39 F5"
third_3rd_off="FE 05 00 02 00 00 78 05"
third_4th_on="FE 05 00 03 FF 00 68 35"
third_4th_off="FE 05 00 03 00 00 29 C5"
third_5th_on="FE 05 00 04 FF 00 D9 F4"
third_5th_off="FE 05 00 04 00 00 98 04"
third_6th_on="FE 05 00 05 FF 00 88 34"
third_6th_off="FE 05 00 05 00 00 C9 C4"
third_7th_on="FE 05 00 06 FF 00 78 34"
third_7th_off="FE 05 00 06 00 00 39 C4"
third_8th_on="FE 05 00 07 FF 00 29 F4"
third_8th_off="FE 05 00 07 00 00 68 04"

third_1st=(third_1st_on,third_1st_off)
third_2nd=(third_2nd_on,third_2nd_off)
third_3rd=(third_3rd_on,third_3rd_off)
third_4th=(third_4th_on,third_4th_off)
third_5th=(third_5th_on,third_5th_off)
third_6th=(third_6th_on,third_6th_off)
third_7th=(third_7th_on,third_7th_off)
third_8th=(third_8th_on,third_8th_off)
third_relay=[third_1st,third_2nd,third_3rd,third_4th,third_5th,third_6th,third_7th,third_8th]


# post={"roof_vent_south":"on"}
control_relay={
    "tri_state":{
                "roof_vent_south":{
                            "on":first_relay[0],
                            "off":first_relay[1]
                                   },
                "roof_vent_north": {
                            "on":first_relay[2],
                            "off":first_relay[3]
                                   },
                "side_vent": {
                            "on":first_relay[4],
                            "off":first_relay[5]
                                   },
                "shade_screen_out": {
                            "on":first_relay[6],
                            "off":first_relay[7]
                                   },
                "shade_screen_in": {
                            "on":second_relay[0],
                            "off":second_relay[1]
                                   },
                "thermal_screen": {
                            "on":second_relay[2],
                            "off":second_relay[3]
                                   }
                },
    "bi_state":{            
                "cooling_pad": second_relay[4],
                "fogging": second_relay[5],
                "heating": second_relay[6],
                "co2": second_relay[7],
                "lighting_1": third_relay[0],
                "lighting_2": third_relay[1],
                "irrigation": third_relay[2]
                }
}

def bi_state_relay_output(key,value):
    relay=control_relay.get("bi_state")
    str1=relay.get(key)
    if value=="on":
        out_str=str1[0]
        print '\n%s relay01 on' %key
        println(out_str)
    else:
        out_str=str1[1]
        print '\n%s relay01 off' %key
        println(out_str)

def tri_state_relay_output(key,value):
    relay=control_relay.get("tri_state")
    str1=relay.get(key)
    if value=="on":
        out_str=str1.get("off")[1]
        print '\n%s relay02 off' %key
        println(out_str)
        out_str=str1.get("on")[0]
        print '%s relay01 on' %key
        println(out_str)
    elif value=="off":
        out_str=str1.get("off")[1]
        print '\n%s relay01 off' %key
        println(out_str)
        out_str=str1.get("on")[0]
        print '%s relay02 on' %key
        println(out_str)
    else:
        out_str=str1.get("off")[1]
        print '\n%s relay01 off' %key
        println(out_str)
        out_str=str1.get("on")[1]
        print '%s relay02 off' %key
        println(out_str)


#test
# str="lighting_2"
# print control_relay.get("bi_state").get(str)
# print "%s relay01 off" %str

