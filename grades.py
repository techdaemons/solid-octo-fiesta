testgrade = float(raw_input ("please input your test grade average:\n"))

quizgrade = float(raw_input ("Please input your quiz grade average:\n"))

homeworkgrade = float(raw_input("Please input your homework grade average:\n"))

finaltest = (testgrade * 0.30)

finalquiz = (quizgrade * 0.30)

finalhomework = (homeworkgrade * 0.40)

finalgrade = (finaltest + finalquiz + finalhomework)

print ("here is your weighted average:\n" + str(finalgrade))

