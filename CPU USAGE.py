#importing Python module 
import psutil 

cpu =psutil.cpu_count()
print(cpu)

while True:
    Cpu_Percent = psutil.cpu_percent(1)
    print(Cpu_Percent)