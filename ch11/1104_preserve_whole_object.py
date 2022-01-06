"""
1104_preserve_whole_object.py

范例 我们想象一个室温监控系统，它负责记录房间一天中的最高温度和最低温度，
然后将实际的温度范围与预先规定的温度控制计划（heating plan）相比较，如果当天温度不符合计划要求，就发出警告。
直接编写新函数

范例 通过重构手法的组合来创建新函数
这种方式的好处在于，它完全是由其他重构手法组合而成的。如果我使用的开发工具支持可靠的提炼和内联操作，用这种方式进行本重构会特别流畅
"""
# === origin
# caller
low = room.days_temp_range.low
high = room.days_temp_range.high
if plan.within_range(low, high):
    alerts.push("room temperature went outside range")

# ==== 6.3-提炼变量
low = room.days_temp_range.low
high = room.days_temp_range.high
is_within_range = plan.within_range(low, high)
if is_within_range:
    alerts.push("room temperature went outside range")

# ==== 6.1-提炼函数
# caller
temp_range = room.days_temp_range
is_within_range = rfc_within_range(plan, temp_range)
if is_within_range:
    alerts.push("room temperature went outside range")

# provider
def rfc_within_range(plan, temp_range):
    low = temp_range.low
    high = temp_range.high
    return plan.within_range(low, high)


# ==== 8.1-搬移函数
# caller
temp_range = room.days_temp_range
is_within_range = plan.rfc_within_range(temp_range)
if is_within_range:
    alerts.push("room temperature went outside range")

# class HeatingPlan
def rfc_within_range(self, temp_range):
    low = temp_range.low
    high = temp_range.high
    return self.within_range(low, high)
