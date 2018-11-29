import pandas as pd
import os,sys
import subprocess

script,file=sys.argv
print(file)

output = pd.read_csv(file,delimiter=';',na_values=['no info','.'])
lines = int(output.shape[0])

for i in range(0,lines):
    print("Criando o arquivo: "+output['host_name'][i]+".cfg")
    f = open(output['host_name'][i]+'.cfg','w')
    f.writelines(['define host {\n',
                 '\t\thost_name \t\t\t\t '+output['host_name'][i],
                 '\n\t\tuse \t\t\t\t\t linux-server',
                 '\n\t\taddress \t\t\t\t '+output['address'][i],
                 '\n\t\tcheck_command \t\t\t\t '+output['check_command'][i],
                 '\n\t\tmax_check_attempts \t\t\t 5',
                 '\n\t\tcheck_interval \t\t\t\t '+str(output['check_interval'][i]),
                 '\n\t\tretry_interval \t\t\t\t 1',
                 '\n\t\tcheck_period \t\t\t\t xi_timeperiod_24x7',
                 '\n\t\tnotification_interval \t\t\t 60',
                 '\n\t\tnotification_period \t\t\t xi_timeperiod_24x7',
                 '\n\t\ticon_image \t\t\t\t oraclequery.png',
                 '\n\t\tstatusmap_image \t\t\t oraclequery.png',
                 '\n\t\tnotes \t\t\t\t\t '+str(output['notes'][i]),
                 '\n\t\t_xiwizard \t\t\t\t oraclequery',
                 '\n\t\tregister \t\t\t\t 1',
                 '\n}'
                  ])
    f.close()
#subprocess.call(["mv","-v *.cfg","/usr/local/nagios/etc/import/"])

print("Movendo os arquivos .cfg para a pasta import")
os.system("mv -v *.cfg /usr/local/nagios/etc/import/")

print("Aplicando as configurações!!")
os.system("/usr/local/nagiosxi/scripts/reconfigure_nagios.sh")

print("Pronto! Feito!")
