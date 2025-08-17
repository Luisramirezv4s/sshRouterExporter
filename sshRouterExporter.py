import paramiko
from openpyxl import Workbook

class CiscoRouterSSH:
    def __init__(self, ip, username, password):
        self.ip = ip
        self.username = username
        self.password = password
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self):
        self.client.connect(self.ip, username=self.username, password=self.password)

    def get_interface_status(self):
        stdin, stdout, stderr = self.client.exec_command("show ip interface brief")
        return stdout.readlines()

    def disconnect(self):
        self.client.close()

class ExcelExporter:
    def __init__(self, filename):
        self.filename = filename
        self.wb = Workbook()
        self.ws = self.wb.active

    def add_data(self, data):
        for row in data:
            self.ws.append(row)

    def save(self):
        self.wb.save(self.filename)

class SQLExporter:
    def __init__(self, filename):
        self.filename = filename
        self.data = []

    def add_data(self, data):
        self.data = data

    def save(self):
        with open(self.filename, 'w') as file:
            file.write("CREATE TABLE interface_status (\n")
            file.write("    Interface VARCHAR(50),\n")
            file.write("    IP_Address VARCHAR(50),\n")
            file.write("    OK VARCHAR(10),\n")
            file.write("    Method VARCHAR(10),\n")
            file.write("    Status VARCHAR(10),\n")
            file.write("    Protocol VARCHAR(10)\n")
            file.write(");\n")
            for row in self.data:
                if len(row) == 6:
                    file.write(f"INSERT INTO interface_status VALUES ('{row[0]}', '{row[1]}', '{row[2]}', '{row[3]}', '{row[4]}', '{row[5]}');\n")

def main():
    router_ip = "192.168.56.129"
    username = "admin"
    password = "admin"

    while True:
        router = CiscoRouterSSH(router_ip, username, password)
        router.connect()
        interface_data = router.get_interface_status()
        router.disconnect()

        formatted_data = [line.strip().split() for line in interface_data]

        print("\nSeleccione el formato de exportación:")
        print("1. Excel (.xlsx)")
        print("2. SQL (.sql)")
        print("0. Cerrar sesión")
        choice = input("Ingrese el número de su elección: ")

        if choice == '1':
            output_file = "interface_status.xlsx"
            exporter = ExcelExporter(output_file)
        elif choice == '2':
            output_file = "interface_status.sql"
            exporter = SQLExporter(output_file)
        elif choice == '0':
            print("Cerrando sesión...")
            break
        else:
            print("Opción no válida")
            continue

        exporter.add_data(formatted_data)
        exporter.save()
        print(f"Datos exportados a {output_file}")

        another_import = input("¿Desea realizar otra importación? (1. Sí / 2. No): ")
        if another_import != '1':
            print("Cerrando sesión...")
            break

if __name__ == "__main__":
    main()
