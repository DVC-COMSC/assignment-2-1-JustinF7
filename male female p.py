def main():
    male = float(input("Number of Males - "))
    female = float(input("Number of Females - "))
    total = male + female
    m_perc = round(male/total * 100, 4)
    f_perc = round(female/total * 100, 4)
    
    print("Male Percentage - " + str(m_perc) + "%")
    print("Female Percentage - " + str(f_perc) + "%")
    return m_perc, f_perc




if __name__ == '__main__':
    main()
