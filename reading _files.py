def merge_files(file_list, output_file):
    file_info = []

    # Открытие файлов, кол-во строк и формирование
    for file_name in file_list:
        with open(file_name, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            line_count = len(lines)
            file_info.append((file_name, line_count, lines))

    # Сортировка
    file_info.sort(key=lambda x: x[1])

    # Запись в итоговый файл
    with open(output_file, 'w', encoding='utf-8') as out_file:
        for file_name, line_count, lines in file_info:
            out_file.write(f"{file_name}\n{line_count}\n")
            out_file.writelines(lines)

# Список файлов для открытия
files_to_merge = ['1.txt', '2.txt', '3.txt']
output_filename = 'final_file.txt'

merge_files(files_to_merge, output_filename)

print(f"Файлы успешно объединены в {output_filename}")