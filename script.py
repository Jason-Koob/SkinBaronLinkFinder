import time

baseURL = 'https://skinbaron.de/en/csgo'
endURL = '?sort=BE'


class color:
    PINK = '\033[95m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'

class itemType:
    Knife = '/Knife'
    Heavy = '/Heavy'
    SMG = '/SMG'
    Rifle = '/Rifle'
    Pistol = '/Pistol'
    Gloves = '/Gloves'
    Accessory = '/Accessory'
    Agents = '/Agents'

def menu():
    print(color.YELLOW + 'Welcome to my SkinBaron Link Finder\n\nAll names should be capitalized.\nSpaces should be replaced with dashes.\n')
    print(color.CYAN + 'Select an weapon type:  (Ex. Knife)\n' + color.GREEN)

    # itemType Options
    print(color.GREEN + 'Knife\nHeavy\nSMG\nRifle\nPistol\nGloves\nAccessories\nAgents\n' + color.CYAN)
    chooseItemType = str(input())

    # ItemName Options
    print(color.GREEN + '\nWhat is the name of the weapon?: (ex.Sawed-Off)\n' + color.CYAN)
    chooseItemName = str(input())

    # ItemName Options
    print(color.GREEN + '\nWhat is the name of the skin?: (Ex.Orange-Peel)\n' + color.CYAN)
    chooseSkinName = str(input())

    # Wear Options
    print(color.GREEN + '\nWhat is the wear of the skin?: (Field-Tested)\n' + color.CYAN)
    chooseSkinWear = str(input())

    fullURL = baseURL + '/' + chooseItemType + '/' + chooseItemName + '/' + chooseSkinName + '/' + chooseSkinWear + endURL

    # Record Data to records.txt
    with open('links.txt', 'a') as docWrite:
        docWrite.write(chooseItemName+ ' / ' + chooseSkinName + ' / ' + chooseSkinWear + '  -  ' + fullURL + '\n')
    
    # Print URL
    print('\n' + color.YELLOW + fullURL )
    print(color.CYAN + '\nThis link has been recorded to the local document called links.txt')
    time.sleep(3600)

menu()