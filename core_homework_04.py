#Task 1

from pathlib import Path

def total_salary(path)-> tuple:
    file_name = Path(path)
    salary = []
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            for line in file:
                salary.append(int(line.split(',')[1]))
            tot = int(sum(salary))
            av = int(tot / len(salary))
        return (tot, av)
    except Exception as error:
        return(error,error)

total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


#Task 2

from pathlib import Path

def get_cats_info(path) -> list:
    file_name = Path(path)
    cats_info_list = []
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            for line in file:
                dict = {"id":line.split(',')[0].strip(), "name":line.split(',')[1].strip(), "age":line.split(',')[2].strip()}
                cats_info_list.append(dict)
            return cats_info_list
    except Exception as error:
        return error

cats_info = get_cats_info("cats_file.txt")
print(cats_info)


#Task 4
