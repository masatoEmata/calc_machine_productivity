from dataclasses import dataclass

@dataclass
class ManConf:
    workers: int
    daily_work_hours: int
    monthly_work_days: int


@dataclass
class Output:
    workers: int
    machine_capacity: float  #一人あたりの対応可能機械数
    operation_rate: float  #ボトルネックを除いた実質稼働率
    man_hours: int
    theoretical_hourly_machine_output: int = 4

    def calc_theoretical_throughput(self):
        '''
        N機時間当たり枚数
        N X 労働時間 X マシン稼働率 x 枚数
        25 X 8 X 0.7 X 4
        '''
        return self.need_machine() * self.__real_machine_hours() * self.theoretical_hourly_machine_output

    def need_machine(self):
        return self.workers * self.machine_capacity

    def __real_machine_hours(self):
        return self.man_hours * self.operation_rate

def days_to_hours(days, daily_hours):
    return days * daily_hours



man = ManConf(workers=2, daily_work_hours=8, monthly_work_days=20)
monthly_hours = days_to_hours(days=man.monthly_work_days, daily_hours=man.daily_work_hours)
monthly_output = Output(workers=man.workers, machine_capacity=12.5, operation_rate=0.65, man_hours=monthly_hours, theoretical_hourly_machine_output=4)
print(monthly_output.calc_theoretical_throughput())
print(monthly_output.need_machine())

# man = ManConf(workers=2, daily_work_hours=10, monthly_work_days=30)
# monthly_hours = days_to_hours(days=man.monthly_work_days, daily_hours=man.daily_work_hours)
# monthly_output = Output(workers=man.workers, machine_capacity=12.5, operation_rate=0.65, man_hours=monthly_hours, theoretical_hourly_machine_output=4)
# print(monthly_output.calc_theoretical_throughput())
# print(monthly_output.need_machine())


man = ManConf(workers=2, daily_work_hours=10, monthly_work_days=30)
monthly_hours = days_to_hours(days=man.monthly_work_days, daily_hours=man.daily_work_hours)
monthly_output = Output(workers=man.workers, machine_capacity=12.5, operation_rate=0.65, man_hours=monthly_hours, theoretical_hourly_machine_output=4)
print(monthly_output.calc_theoretical_throughput())
print(monthly_output.need_machine())