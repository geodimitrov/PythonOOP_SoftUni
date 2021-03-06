from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def get_obj_by_name(obj_name, obj_list):
        return [obj for obj in obj_list if obj.name == obj_name][0]

    @staticmethod
    def register_power_hardware(name, capacity, memory):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name, capacity, memory):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name, name, capacity_consumption, memory_consumption):
        if hardware_name not in [h.name for h in System._hardware]:
            return "Hardware does not exist"
        hardware = System.get_obj_by_name(hardware_name, System._hardware)
        try:
            hardware.install(ExpressSoftware(name, capacity_consumption, memory_consumption))
            System._software.append(ExpressSoftware(name, capacity_consumption, memory_consumption))
        except:
            return "Software cannot be installed"

    @staticmethod
    def register_light_software(hardware_name, name, capacity_consumption, memory_consumption):
        if hardware_name not in [h.name for h in System._hardware]:
            return "Hardware does not exist"
        hardware = System.get_obj_by_name(hardware_name, System._hardware)
        try:
            hardware.install(LightSoftware(name, capacity_consumption, memory_consumption))
            System._software.append(LightSoftware(name, capacity_consumption, memory_consumption))
        except:
            return "Software cannot be installed"

    @staticmethod
    def release_software_component(hardware_name, software_name):
        if hardware_name not in [h.name for h in System._hardware] \
                or software_name not in [s.name for s in System._software]:
            return "Some of the components do not exist"
        hardware = System.get_obj_by_name(hardware_name, System._hardware)
        software = System.get_obj_by_name(software_name, System._software)
        System._software.remove(software)
        hardware.uninstall(software)

    @staticmethod
    def get_total_used_capacity():
        return sum(s.capacity_consumption for s in System._software)

    @staticmethod
    def get_total_capacity():
        return sum(h.capacity for h in System._hardware)

    @staticmethod
    def get_total_used_memory():
        return sum(s.memory_consumption for s in System._software)

    @staticmethod
    def get_total_memory():
        return sum(h.memory for h in System._hardware)

    @staticmethod
    def analyze():
        return "System Analysis\n" + f"Hardware Components: {len(System._hardware)}\n"\
        + f"Software Components: {len(System._software)}\n" \
        + f"Total Operational Memory: {System.get_total_used_memory()} / {System.get_total_memory()}\n" \
        + f"Total Capacity Taken: {System.get_total_used_capacity()} / {System.get_total_capacity()}"

    @staticmethod
    def system_split():
        return "".join(f"{hardware.__repr__()}" for hardware in System._hardware)