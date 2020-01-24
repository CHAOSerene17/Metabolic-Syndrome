#Set up
yes_no = ["yes" , "no"]

#Criteria
is_elevated_waist_circumference = True
is_elevated_triglycerides = True
is_reduced_HDL = True
is_elevated_BP = True
is_elevated_fasting_glucose = True

Meta_Score = 0
Meta_limit = 3
Reached_Limit = False


#Introduction
print("Do you know if you have metabolic syndrome? \n" +
      "Follow this simple questionnaire to complete a screening and find out." +
      "\nPlease note that this is only a SCREENING not a diagnosis." +
      " See your primary care provider for a diagnosis." +
      "\nAre you ready to begin? \n")

#Begin
response_1a = input("Please type yes/no to begin the screening for metabolic syndrome: \n")
while response_1a not in yes_no:
    print("I didn't understand that.")
    response_1a = input("Please type \"yes\" or \"no\" to begin: ")

#First Criteria
if response_1a == "yes":
    print("First, we will determine your waist circumference and whether it is elevated.")
    answer = input("\nDo you know what your waist circumference is? Type yes or no as appropriate.\n")
    if answer == "yes":
        print("Is your weight circumference greater than the following: " +
            "\nMale: greater than or equal to 40 in (102 cm)?" +
            "\nFemale: greater than or equal to 35 in (88 cm)?")
        response_1a = input("\nType yes or no as appropriate: ")
        if response_1a == "yes":
            Meta_Score += 1
            print("Okay. Let's move onto the next question.\n")
        elif response_1a == "no":
            print("Okay. Let's move onto the next question.\n")
        else:
            print("I didn't understand that. Please type \"yes\" or \"no\". \n")
    elif answer == "no":
        print("Here is how to measure your waist circumference: \n" +
              "1) Obtain a measuring tape. \n" +
              "2. Locate the top right iliac crest. \n" +
              "3. Place the measuring tape around the abdomen at level of iliac crest.\n" +
              "4. Make sure the tape is snug and does not compress the skin. \n" +
              "5. Make sure the tape is parallel to the floor.\n" +
              "6. Measurement is taken at the end of normal exhalation.\n")
        response_1b = input("Is this measurement of your weight circumference greater than the following:? " +
            "\nMale: greater than or equal to 40 in (102 cm)?" +
            "\nFemale: greater than or equal to 35 in (88 cm)?" +
            "\nType yes or no as appropriate: ")
        if response_1b == "yes":
            Meta_Score += 1
            print("Okay. Let's move onto the next question.")
        elif response_1b == "no":
            print("Okay. Let's move onto the next question.")
        else:
            print("I didn't understand that. Please type \"yes\" or \"no\".")
elif response_1a == "no":
    print("Please complete the questionnaire when you are ready. Stay happy and healthy!")
    quit()
print(Meta_Score)

#Second Criteria
print("Second, we'll evaluate your triglyceride levels." +
" Triglycerides are part of the cholesterol screening when getting a blood test.")
response_2a = input("Is your triglyceride level equal to or ABOVE 150 mg/dL (1.7 mmol/L)?" +
                    "\nType yes or no: ")
if response_2a == "yes":
    Meta_Score += 1
    print("Okay. Let's move onto the next question.")
elif response_2a == "no":
    response_2b = input("Do you take medications for elevated triglycerides?" + "\nType yes or no: ")
    if response_2b == "yes":
        Meta_Score += 1
        print("Okay. Let's move onto the next question.\n")
    elif response_2b == "no":
        print("Okay. Let's move onto the next question.\n")
    else:
        print("I didn't understand that. Please type \"yes\" or \"no\".")
else:
    print("I didn't understand that. Please type \"yes\" or \"no\".")
print(Meta_Score)

#Third Criteria
print("Third, we'll evaluate your HDL cholesterol levels." +
      "\nHDLs are part of the cholesterol screening when getting a blood test.")
print("Is your HDL cholesterol level equal to or below the following:" +
                    "\nMale = <40 mg/dl (1.03 mmol/L ?" +
                    "\nFemale: <50 mg/dL (1.3 mmol/L ?")
response_3a = input("\nType yes or no as appropriate: ")
if response_3a == "yes":
            Meta_Score += 1
            print("Okay. Let's move onto the next question.\n")
elif response_3a == "no":
    response_3b = input("Do you take medications for reduced HDL?" + "\nType yes or no: ")
    if response_3b == "yes":
        Meta_Score += 1
        print("Okay. Let's move onto the next question.\n")
    elif response_3b == "no":
        print("Okay. Let's move onto the next question.\n")
    else:
        print("I didn't understand that. Please type \"yes\" or \"no\".")
else:
    print("I didn't understand that. Please type \"yes\" or \"no\".")
print(Meta_Score)

#Fourth Criteria
print("Fourth, we'll evaluate your blood pressure level." +
      "\nWe will evaluate the systolic and diastolic levels individually.")
response_4a = input("\nIs your systolic blood pressure equal to or above 130mm Hg? \nType yes or no: ")
if response_4a == "yes":
    print("Okay. Let's move onto the diastolic value.")
elif response_4a == "no":
    print("Okay. Let's move onto the diastolic value.")
else:
    print("I didn't understand that. Please type \"yes\" or \"no\".")
response_4aa = input("\nIs your diastolic blood pressure equal to or above 85mm Hg? \nType yes or no: ")
if response_4aa == "yes":
    print("Okay. Let's move onto the next question.")
elif response_4aa == "no":
    print("Okay. Let's move onto the next question.")
else:
    print("I didn't understand that. Please type \"yes\" or \"no\".")
response_4b = input("\nDo you take medications for elevated blood pressure?" + "\nType yes or no: ")
if response_4b == "yes":
    print("Okay. Let's move onto the next question.")
elif response_4b == "no":
    print("Okay. Let's move onto the next question.")
else:
    print("I didn't understand that. Please type \"yes\" or \"no\".")
if response_4a == "yes" or response_4aa == "yes" or response_4b == "yes":
    Meta_Score += 1
print(Meta_Score)

#Fifth Criteria
print("Lastly, we'll evaluate your fasting blood sugar level.")
print("Is your blood sugar level equal to or ABOVE the following:" +
                    "\n100 mg/dL")
response_5a = input("\nType yes or no as appropriate: ")
if response_5a == "yes":
    Meta_Score += 1
    print("Okay. Let's move onto the results.")
elif response_5a == "no":
    response_5b = input("Do you take medications to control your blood sugar?" + "\nType yes or no: ")
    if response_5b == "yes":
        Meta_Score += 1
        print("Okay. Let's move onto the results.")
    elif response_5b == "no":
        print("Okay. Let's move onto the results.")
    else:
        print("I didn't understand that. Please type \"yes\" or \"no\".")
else:
    print("I didn't understand that. Please type \"yes\" or \"no\".")
print(Meta_Score)

#Results
print("The screening has finished." +
      "\nOne is considered to have Metabolic Syndrome if one has 3 out of 5 of the following criteria: " +
      "\n1) Elevated waist circumference" +
      "\nElevated Triglyceride levels" +
      "\nReduced HDL cholesterol levels" +
      "\n Elevated blood pressure levels" +
      "\nElevated fasting blood sugar levels")
print("\nYou have met " + str(Meta_Score) + " out of the 5 criteria of Metabolic Syndrome.")
if Meta_Score >= Meta_limit:
    print("\nYou may have Metabolic Syndrome. Please consult your primary care physician for more information.")
elif Meta_Score < Meta_limit:
    print("\nYou may not have Metabolic Syndrome.")


