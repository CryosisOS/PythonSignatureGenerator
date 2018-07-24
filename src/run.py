# Author: CryosisOS
# Date Created: 2018-07-24

from conditional.Validation import Validation

choice = ""
while Validation.condition(choice) == False:
    print("Please select the file type that you wish to generate: ")
    print("1. HTML")
    print("2. Rich Text Format [N/A]")
    print("3. Text Format [N/A]")
    print("Please enter the choice below...")
    choice = input()
    
    if choice == "1" or choice == "html" or choice == "HTML":
        # goto generating HTML Signatures
        print("Getting template files...")
    elif choice == "2" or choice == "rtf" or choice == "RTF":
        # goto generating RTF Signatures
        print("This section is not available yet.")
    elif choice == "3" or choice == "txt" or choice == "TXT":
        # goto generating TXT Signatures
        print("This section is not available yet.")
    else:
        print("This is an invalid option please choose again.")
