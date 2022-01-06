"""
1106_replace_query_with_parameter.py

范例 我们想象一个简单却又烦人的温度控制系统。
用户可以从一个温控终端（thermostat）指定温度，但指定的目标温度必须在温度控制计划（heating plan）允许的范围内。
"""


class HeatingPlan(object):
    @property
    def target_temperature(self, selected_temperature):
        if selected_temperature > self._max:
            return self._max
        elif selected_temperature < self._min:
            return self._min
        else:
            return selected_temperature


if __name__ == "__main__":
    thermostat = "..."
    if thePlan.target_temperature(thermostat.selected_temperature) > thermostat.current_temperature:
        set_to_heat()
    elif thePlan.target_temperature(thermostat.selected_temperature) < thermostat.current_temperature:
        set_to_cool()
    else:
        set_off()
