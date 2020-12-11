import re


def validate(code_list):
    result = 0
    checkList = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for aCode in code_list.keys():
        if aCode in checkList:
            checkList.remove(aCode)
    if len(checkList) == 0:
        result = 1
    return result


def validate2(code_list):
    checkList = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for aCode in code_list.keys():
        if aCode == "byr":
            if 1920 <= int(code_list[aCode]) <= 2002:
                checkList.remove(aCode)
        elif aCode == "iyr":
            if 2010 <= int(code_list[aCode]) <= 2020:
                checkList.remove(aCode)
        elif aCode == "eyr":
            if 2020 <= int(code_list[aCode]) <= 2030:
                checkList.remove(aCode)
        elif aCode == "hgt":
            if "cm" in code_list[aCode]:
                if 150 <= int(code_list[aCode].split("cm")[0]) <= 193:
                    checkList.remove(aCode)
            elif "in" in code_list[aCode]:
                if 59 <= int(code_list[aCode].split("in")[0]) <= 76:
                    checkList.remove(aCode)
        elif aCode == "hcl":
            valid = re.match(r'#[0-9a-f]{6}', code_list[aCode])
            if valid:
                checkList.remove(aCode)
        elif aCode == "ecl":
            clr_list = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            if code_list[aCode] in clr_list:
                checkList.remove(aCode)
        elif aCode == "pid":
            valid = re.match(r'\d{9}', code_list[aCode])
            if valid:
                checkList.remove(aCode)
    if len(checkList) == 0:
        return 1
    return 0


aFile = open("../inputs/passports.txt")
lines = aFile.readlines()
count = 0
passport = {}
for aLine in lines:
    if not(aLine == "\n"):
        entries = aLine.split(" ")
        for entry in entries:
            key = entry.split(":")[0].strip()
            value = entry.split(":")[1].strip()
            passport[key] = value
    else:
        count += validate2(passport)
        passport = {}
count += validate2(passport)
print(count)
