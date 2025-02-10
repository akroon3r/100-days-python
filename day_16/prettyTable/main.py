from prettytable import PrettyTable


if __name__ == '__main__':
    table = PrettyTable()
    table.add_column("Pokeman Name", ["Pikachu"])
    table.add_column("Type", ["Electric"])
    table.align = 'l'
    print(table)
