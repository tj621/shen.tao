'''

@author: Zxh
'''
from flask import Flask, g
import sqlite3
import os
from currenttime import get_current_time
from parameter import Parameter

app=Flask(__name__)

global para
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'greenhouse.db'),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
    ))

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db=connect_db()
    return g.sqlite_db

def close_db():
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()    

def save_db_indoor(Indoor):
    with app.app_context():
        db=get_db()
        db.execute('insert into indoor(node_number,update_time,temperature,humidity,radiation,co2) values(?,?,?,?,?,?)',
                    [Indoor.name,get_current_time(),Indoor.get_temperature(),Indoor.get_humidity(),Indoor.get_radiation(),Indoor.get_co2()])
        db.commit()
    print 'indoor save success'    
    
def save_db_outdoor(Outdoor):
    with app.app_context():
        db=get_db()
        db.execute('insert into outdoor(update_time,temperature,humidity,radiation,co2,wind_direction,wind_speed,rain_snow,atmosphere)\
                   values(?,?,?,?,?,?,?,?,?)', [get_current_time(),Outdoor.temperature,Outdoor.humidity,Outdoor.radiation,Outdoor.co2,Outdoor.wind_direction,\
                                                Outdoor.wind_speed,Outdoor.rain,Outdoor.atmosphere])
        db.commit()
    print 'outdoor save success'

def save_db_control(Control):
    with app.app_context():
        db=get_db()
        db.execute('insert into control_state(update_time,roof_vent_south,roof_vent_north,side_vent,shade_screen_out,shade_screen_in,thermal_screen,\
        cooling_pad,fogging,heating,co2,lighting_1,lighting_2,irrigation) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
        [get_current_time(),Control.get_roof_vent_south(),Control.get_roof_vent_north(),Control.get_side_vent(),Control.get_shade_screen_out(),Control.get_shade_screen_in(),\
         Control.get_thermal_screen(),Control.get_cooling_pad(),Control.get_fogging(),Control.get_heating(),Control.get_co2(),Control.get_lighting_1(),Control.get_lighting_2(),Control.get_irrigation()])
        db.commit()
    print 'control save success'

def save_db_parameter(Parameter):
    with app.app_context():
        db=get_db()
        db.execute('insert into parameter(update_time,time1,temperature1,time2,temperature2,time3,temperature3,time4,temperature4, co2_upper_limit,co2_lower_limit, cooling_start_temperature,cooling_stop_temperature,\
                    expect_humidity,humidity_influence_range_of_air_temperature,low_humidity_influence_on_air_temperature,high_humidity_influence_on_air_temperature,expect_light,light_influence_on_air_temperature_slope,high_light_influence_on_temperature,low_light_influence_on_temperature,frost_temperature,\
                    indoor_temperature_lower_limit,roof_vent_wind_speed_upper_limit,roof_vent_rain_upper_limit, heating_start_lowest_temperature,heating_stop_highest_temperature, month_to_open_thermal_screen,month_to_close_thermal_screen,time_to_open_thermal_screen,time_to_close_thermal_screen, temperature_to_open_side,\
                    wait_time_to_open_side,rain_upper_limit_to_close, upper_limit_light_to_open_shade_screen_out,upper_limit_light_to_open_shade_screen_in,soil_humidity_to_start_irrigation,soil_humidity_to_stop_irrigation,temperature_to_open_fogging,temperature_to_open_cooling_pad,\
                    month_to_open_lighting,month_to_close_lighting,period1_start_lighting,period1_stop_lighting,period2_start_lighting,period2_stop_lighting,radiation1_to_open_lighting,radiation2_to_open_lighting,roof_vent_open_time,side_vent_open_time,shade_screen_out_open_time,\
                    shade_screen_in_open_time,thermal_screen_open_time ) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',\
                    [get_current_time(),Parameter.get_time_1(),Parameter.get_temperature_1(),Parameter.get_time_2(),Parameter.get_temperature_2(),Parameter.get_time_3(),Parameter.get_temperature_3(),Parameter.get_time_4(),Parameter.get_temperature_4(),Parameter.get_co_2_upper_limit(),Parameter.get_co_2_lower_limit(),
                     Parameter.get_cooling_start_temperature(),Parameter.get_cooling_stop_temperature(),
                     Parameter.get_expect_humidity(),Parameter.get_humidity_influence_range_of_air_temperature(),Parameter.get_low_humidity_influence_on_air_temperature(),Parameter.get_high_humidity_influence_on_air_temperature(),Parameter.get_expect_light(),Parameter.get_light_influence_on_air_temperature_slope(),
                     Parameter.get_high_light_influence_on_temperature(),Parameter.get_low_light_influence_on_temperature(),Parameter.get_frost_temperature(),Parameter.get_indoor_temperature_lower_limit(),Parameter.get_roof_vent_wind_speed_upper_limit(),Parameter.get_roof_vent_rain_upper_limit(),
                     Parameter.get_heating_start_lowest_temperature(),Parameter.get_heating_stop_highest_temperature(),Parameter.get_month_to_open_thermal_screen(),Parameter.get_month_to_close_thermal_screen(),Parameter.get_time_to_open_thermal_screen(),Parameter.get_time_to_close_thermal_screen(),
                     Parameter.get_temperature_to_open_side(),
                     Parameter.get_wait_time_to_open_side(),
                     Parameter.get_rani_upper_limit_to_close(),
                     Parameter.get_upper_limit_light_to_open_shade_screen_out(),
                     Parameter.get_upper_limit_light_to_open_shade_screen_in(),
                     Parameter.get_soil_humidity_to_start_irrigation(),
                     Parameter.get_soil_humidity_to_stop_irrigation(),
                     Parameter.get_temperature_to_open_fogging(),
                     Parameter.get_temperature_to_open_cooling_pad(),
                     Parameter.get_month_to_open_lighting(),
                     Parameter.get_month_to_close_lighting(),
                     Parameter.get_period_1_start_lighting(),
                     Parameter.get_period_1_stop_lighting(),
                     Parameter.get_period_2_start_lighting(),
                     Parameter.get_period_2_stop_lighting(),
                     Parameter.get_radiation_1_to_open_lighting(),
                     Parameter.get_radiation_2_to_open_lighting(),
                     Parameter.get_roof_vent_open_time(),
                     Parameter.get_side_vent_time(),
                     Parameter.get_shade_screen_out_time(),
                     Parameter.get_shade_screen_in_time(),
                     Parameter.get_thermal_screen_open_time()
                     ])
        db.commit()
        print 'parameter save success'
def get_db_parameter():
    query='select * from parameter where id=(select max(id) from parameter)'
    row=query_db(query)
    a=1
    para=Parameter()
    para.set_time_1(row[a])
    para.set_temperature_1(row[a+1])
    para.set_time_2(row[a+2])
    para.set_temperature_2(row[a+3])
    para.set_time_3(row[a+4])
    para.set_temperature_3(row[a+5])
    para.set_time_4(row[a+6])
    para.set_temperature_4(row[a+7])
    
    para.set_co_2_upper_limit(row[a+8])
    para.set_co_2_lower_limit(row[a+9])
    para.set_cooling_start_temperature(row[a+10])
    para.set_cooling_stop_temperature(row[a+11])
    
    para.set_expect_humidity(row[a+12])
    para.set_humidity_influence_range_of_air_temperature(row[a+13])
    para.set_low_humidity_influence_on_air_temperature(row[a+14])
    para.set_high_humidity_influence_on_air_temperature(row[a+15])
    para.set_expect_light(row[a+16])
    para.set_light_influence_on_air_temperature_slope(row[a+17])
    para.set_high_light_influence_on_temperature(row[a+18])
    para.set_low_light_influence_on_temperature(row[a+19])
    para.set_frost_temperature(row[a+20])
    para.set_indoor_temperature_lower_limit(row[a+21])
    para.set_roof_vent_wind_speed_upper_limit(row[a+22])
    para.set_roof_vent_rain_upper_limit(row[a+23])
    
    para.set_heating_start_lowest_temperature(row[a+24])
    para.set_heating_stop_highest_temperature(row[a+25])
    
    para.set_month_to_open_thermal_screen(row[a+26])
    para.set_month_to_close_thermal_screen(row[a+27])
    para.set_time_to_open_thermal_screen(row[a+28])
    para.set_time_to_close_thermal_screen(row[a+29])
    
    para.set_temperature_to_open_side(row[a+30])
    para.set_wait_time_to_open_side(row[a+31])
    para.set_rani_upper_limit_to_close(row[a+32])
    
    para.set_upper_limit_light_to_open_shade_screen_out(row[a+33])
    para.set_upper_limit_light_to_open_shade_screen_in(row[a+34])
    para.set_soil_humidity_to_start_irrigation(row[a+35])
    para.set_soil_humidity_to_stop_irrigation(row[a+36])
    para.set_temperature_to_open_fogging(row[a+37])
    para.set_temperature_to_open_cooling_pad(row[a+38])
    
    para.set_month_to_open_lighting(row[a+39])
    para.set_month_to_close_lighting(row[a+40])
    para.set_period_1_start_lighting(row[a+41])
    para.set_period_1_stop_lighting(row[a+42])
    para.set_period_2_start_lighting(row[a+43])
    para.set_period_2_stop_lighting(row[a+44])
    para.set_radiation_1_to_open_lighting(row[a+45])
    para.set_radiation_2_to_open_lighting(row[a+46])
    
    para.set_roof_vent_open_time(row[a+47])
    para.set_side_vent_time(row[a+48])
    para.set_shade_screen_out_time(row[a+49])
    para.set_shade_screen_in_time(row[a+50])
    para.set_thermal_screen_open_time(row[a+51])
    
    return para.build_to_json() 
    print 'get parameter success'
    
def query_db(query,args=(),one=False):
    with app.app_context():
        cur=get_db().execute(query,args)
        rv=cur.fetchall()
        cur.close()
        return rv[0]



# if __name__ == '__main__':
#     p=Parameter()
#     init_db()
    
#     p=Parameter()
#     save_db_parameter(p)
#     query='select * from parameter where id=(select max(id) from parameter)'
#     print query_db(query)
#     get_db_parameter()
    
#     print p.get_co2_lower_limit()
    
#      out=Outdoor()
#      with app.app_context():
#          db=get_db()
#          db.execute('''insert into outdoor(update_time,temperature,humidity,radiation,co2,wind_direction,wind_speed,rain_snow,atmosphere)\
#                         values(?,?,?,?,?,?,?,?,?)''', [out.update_time,out.temperature,out.humidity,out.radiation,out.co2,out.wind_direction,\
#                                                      out.wind_speed,out.rain,out.atmosphere])
#          db.commit()
#      print(out.classtoJson())   