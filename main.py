from change_dns import list_network_interfaces,clear_dns_windows,set_dns_windows
import pprint
import get_admin_privilege



if __name__ == "__main__":

    get_admin_privilege.run_as_admin()
    interfaces = list_network_interfaces()
    print('\n------------------\n')
    pprint.pprint(interfaces)
    
    user_inter = interfaces.get(int(input('\nplease select your interface id \n\n')))

    print('\n------------------\n')

    list_dns = {
        1 : ['Shecan','178.22.122.100','185.51.200.2'],
        2 : ['Electro','78.157.42.101','78.157.42.100'],
        3 : ['RadarGame','10.202.10.10','10.202.10.11'],
        4 : ['Google','8.8.8.8','8.8.4.4'],
        5 : ['Begzar','185.55.226.26','185.55.225.25'],
        6 : ['403','10.202.10.202','10.202.10.102'],
        7 : ['Shelter','91.92.251.5','91.92.250.178']
    }
    
    clear_dns_windows(user_inter)
    print('\n------------------\n')
    
    pprint.pprint(list_dns)
    print('\nSelect your dns by ID\n')  
    print()
    selected_dns = list_dns.get(int(input()))
    
    print('\n------------------\n')
    print(f'Setting your dns to {selected_dns}')
    set_dns_windows(user_inter, selected_dns[1], selected_dns[2])

    input('Enter to exit')

