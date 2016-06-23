'''
Created on 2016/06/20

@author: Zxh
'''
from indoor import Indoor
from outdoor import Outdoor
from control import Control
from parameter import Parameter
from autorun import autorun_main
node0=Indoor('node0')
outdoor=Outdoor()
control=Control()
parameter=Parameter()
# parameter.set_month_to_open_lighting("5")
# parameter.set_month_to_close_lighting("7")
# parameter.set_period_1_start_lighting("0")
# parameter.set_period_1_stop_lighting("24")
# outdoor.set_radiation("400")
# parameter.set_radiation_1_to_open_lighting("500")
# control.set_lighting_1("off")
# control.set_lighting_2("off")
node0.set_temperature("-3")

autorun_main(node0,outdoor,control,parameter)