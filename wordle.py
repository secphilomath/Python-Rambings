# this will take a string and output the string encrypted using the Caesar Cipher
from colorama import Fore
import random

choices = ["about","alert","argue","beach","above","alike","arise","began","abuse","alive","array","begin","actor","allow","aside","begun","acute","alone","asset","being","admit","along","audio","below","adopt","alter","audit","bench","adult","among","avoid","billy","after","anger","award","birth","again","angle","aware","black","agent","angry","badly","blame","agree","apart","baker","blind","ahead","apple","bases","block","alarm","apply","basic","blood","album","arena","basis","board","boost","buyer","cover","booth","cable","chose","craft","bound","calif","civil","crash","brain","carry","claim","cream","brand","catch","class","crime","bread","cause","clean","cross","break","chain","clear","crowd","breed","chair","click","crown","brief","chart","clock","curve","bring","chase","close","cycle","broad","cheap","coach","daily","broke","check","coast","dance","brown","chest","could","dated","build","chief","count","dealt","built","child","court","death","debut","entry","forth","group","delay","equal","forty","grown","depth","error","forum","guard","doing","event","found","guess","doubt","every","frame","guest","dozen","exact","frank","guide","draft","exist","fraud","happy","drama","extra","fresh","harry","drawn","faith","front","heart","dream","false","fruit","heavy","dress","fault","fully","hence","drill","fibre","funny","night","drink","field","giant","horse","drive","fifth","given","hotel","drove","fifty","glass","house","dying","fight","globe","human","eager","final","going","ideal","early","first","grace","image","earth","fixed","grade","index","eight","flash","grand","inner","elite","fleet","grant","input","empty","floor","grass","issue","enemy","fluid","great","irony","enjoy","focus","green","juice","enter","force","gross","joint","judge","metal","media","newly","known","local","might","noise","label","logic","minor","north","large","loose","minus","noted","laser","lower","mixed","novel","later","lucky","model","nurse","laugh","lunch","money","occur","layer","lying","month","ocean","learn","magic","moral","offer","lease","major","motor","often","least","maker","mount","order","leave","march","mouse","other","legal","music","mouth","ought","level","match","movie","paint","light","mayor","needs","paper","limit","meant","never","party","peace","power","radio","round","panel","press","raise","route","phase","price","range","royal","phone","pride","rapid","rural","photo","prime","ratio","scale","piece","print","reach","scene","pilot","prior","ready","scope","pitch","prize","refer","score","place","proof","right","sense","plain","proud","rival","serve","plane","prove","river","seven","plant","queen","quick","shall","plate","sixth","stand","shape","point","quiet","roman","share","pound","quite","rough","sharp","sheet","spare","style","times","shelf","speak","sugar","tired","shell","speed","suite","title","shift","spend","super","today","shirt","spent","sweet","topic","shock","split","table","total","shoot","spoke","taken","touch","short","sport","taste","tough","shown","staff","taxes","tower","sight","stage","teach","track","since","stake","teeth","trade","sixty","start","texas","treat","sized","state","thank","trend","skill","steam","theft","trial","sleep","steel","their","tried","slide","stick","theme","tries","small","still","there","truck","smart","stock","these","truly","smile","stone","thick","trust","smith","stood","thing","truth","smoke","store","think","twice","solid","storm","third","under","solve","story","those","undue","sorry","strip","three","union","sound","stuck","threw","unity","south","study","throw","until","space","stuff","tight","upper","upset","whole","waste","wound","urban","whose","watch","write","usage","woman","water","wrong","usual","train","wheel","wrote","valid","world","where","yield","value","worry","which","young","video","worse","while","youth","virus","worst","white","worth","visit","would","vital","voice"]

def pickAnswer():
    
    #pick a random number
    element = random.randint(0,len(choices))    
    answer = choices[element]
    
    
    return answer


def isrealword(guess):
    
    #is the users guess a real word?
    try:
        element = choices.index(guess)
        return 1
    except:
        return 0

def CheckAnswer(guess, answer):
    
    lowercase = guess.lower()
    guessunpacked = [*lowercase]
    
    answerunpacked = [*answer]
    result = ""
    
    if lowercase == answer:
        result = "correct"
        return result
    i = 0
    while i < 5:
        if guessunpacked[i] == answerunpacked[i]:
             #correct letter in correct location guess
             result = result + Fore.GREEN + guessunpacked[i]
             
        elif guessunpacked[i] in answer:
            #letter is in the answer but not in this position
            #check to see if we have already guessed it and it isn't repeated in the answer
            if answerunpacked.count(guessunpacked[i]) > 1:
                 
                result = result + Fore.YELLOW + guessunpacked[i]
            else:
                result = result + Fore.YELLOW + guessunpacked[i]
            
        else:
            #letter is not in the answer
            result = result + Fore.RED + guessunpacked[i]
        i+=1
    
    return result



answer = pickAnswer()

#print("Today's answer is: " + answer)
guess = ""
guessnumber = 1
while guessnumber < 7:
    guess = input(Fore.WHITE + "What is your guess?")

    #Is the word guessed a real word?
    if isrealword(guess):
        result = CheckAnswer(guess,answer)
    else:
        print("Not a real word, please try again.")
        continue


    if result == "correct":
        print(Fore.GREEN + "You guessed Correct in " + str(guessnumber) + " guesses!")
        if guessnumber == 1:
            print(Fore.GREEN + "Genius!")
        elif guessnumber == 2:
            print(Fore.GREEN + "Magnificient!")
        elif guessnumber == 3:
            print(Fore.GREEN + "Impressive!")
        elif guessnumber == 4:
            print(Fore.GREEN + "Splended!")
        elif guessnumber == 5:
            print(Fore.GREEN + "Great!")
        elif guessnumber == 6:
            print(Fore.GREEN + "Phew!")
        exit()
    else:
        if guessnumber != 6:
            print(Fore.RED + "Try again: " + result)
            print(Fore.BLUE + "Number of guesses remaining:" + str(6 - int(guessnumber)))          
            guessnumber +=1
        else:
            print(Fore.RED + "Sorry out of guesses.  The answer was " + answer)
            break
    
print (Fore.RED + "Better luck next time.")
exit()


   
