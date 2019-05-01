def main():
    aboutMe()
    experiencesShapeMe()
    strengths_list = strengths()
    toImprove(strengths_list)
    dedicatedLifeTo()
    expectFromMe()
    mentorMission()


def aboutMe():
    nikki_age = 21
    if nikki_school in schools:
        print("I am a computer science major hoping to declare a computer security minor.")
    while nikki_age <= 21:
        print("I felt a sudden urgency to try out many hobbies because I was so sheltered in private\n"
              "Catholic school all my life (14 years). My recent creative outlets are the guitar and\n"
              "ukulele, powerlifting, and hiking. I actually wanted to become an architech major\n"
              "but pressured by my parents, I felt the need to please them after all the hardships\n"
              "they endured to give me an advantage in life. I fell in love with the actual freedom\n"
              "of going to music festivals and concerts but that doesn't stop me from focusing on\n"
              "school and just recently starting dragon boat.")
        nikki_age += 1 #let's see what happens when I turn 22

def experiencesShapeMe():
    exp1 = "Tearing my meniscus"
    exp2 = "Walk in Faith"
    exp3 = "Rejection from my top schools"
    exp4 = "The Halal Guys"
    print(exp1 + ", " + exp2 + ", " + exp3 + ", " + exp4)

def strengths():
    strengths_list = ["Passionate",
                 "Takes Initiative",
                 "Creative",
                 "Accountable",
                 "Dependable"]
    print(strengths_list)
    return strengths_list

def toImprove(strengths_list):
    improvement_list = ["Motivation",
                        "Procrastination",
                        "Impulsive",
                        "Not Finishing Tasks"]
    if improvement_list not in strengths_list:
        print(improvement_list)


def dedicatedLifeTo():
    isActive = True
    if(isActive):
        print("Being open to new opportunities")
    else:
        print("Making an impact on the people I meet")

def expectFromMe():
    isWorking = True
    while(isWorking):
        print(expectations)
        isWorking = False

def mentorMission():
    mentees = 9
    for mentee in range(mentees):
        print("I want to help my mentee to avoid the mistakes I made.\n"
              "There are also many resources I never utilized when I\n"
              "first arrived on campus, I want to show them.")

nikki_school = "csulb"
schools = ["uci", "ucla", "ucr", "csulb", "csuf", "ucsc", "occ"]
expectations = ["a friend", "professionalism", "productivity", "feedback"]
main()
