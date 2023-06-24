def main():
    male = float(input("Number of Males - "))
    female = float(input("Number of Females - "))
    total = male + female
    m_perc = round(male/total * 100, 2)
    f_perc = round(female/total * 100, 2)
    
    print("Male Percentage - " + str(m_perc) + "%")
    print("Female Percentage - " + str(f_perc) + "%")
    print(total)
    return m_perc, f_perc




if __name__ == '__main__':
    main()