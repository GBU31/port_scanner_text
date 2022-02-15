import scan   
import geo
import os

def save(ip, ports, geo_info):
    try:
        f = open(f"{ip}.txt", "x")
    except:
        f = open(f"{ip}.txt", "w")
    if geo_info != None:
        f.write(f"ip:{ip}\n{ports}\n{geo_info}")
        f.close()
    else:
        f.write(f"ip:{ip}\n{ports}")
        f.close()

def check_geo(ip):
    try:
        return geo.GEO(ip)
    except:
        return None


def clear():
    os.system('clear')
    print('\ngithub:\33[36mbrookehorizon\x1b[0m\n')

def main():
    clear()
    ip = input(f'ip (\x1b[6;30;42m127.0.0.1\x1b[0m):')
    if ip == '':
        ip = '127.0.0.1'
    clear()
    ports = scan.Scan(ip)
    
    if len(ports) == 0:
        print('All ports are closed \33[31m:(\x1b[0m')
    else:
        for port in ports:
            print(f'\x1b[6;30;42m{port}\x1b[0m open')

    if check_geo(ip) != None:
        print(check_geo(ip))

    i = input('\n[\33[31me\x1b[0m]xist, press any key to rerun:')
    if i == 'e':
        save(ip, ports, check_geo(ip))
        exit()
    else:
        main()



main()