def main():
    male = float(input("Number of Males - "))
    female = float(input("Number of Females - "))
    total = male + female
    m_perc = str(round(male/total * 100))
    f_perc = str(round(female/total * 100))
    
    print("Male Percentage - " + m_perc + "%")
    print("Female Percentage - " + f_perc + "%")
    return m_perc, f_perc




if __name__ == '__main__':
    main()
