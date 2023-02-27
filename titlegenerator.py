from random import randint





def videoessaygenerator():
    while True:
        blankification = ["yass", "mrbeast", "anime", "fly", "vaush"]
        blank = blankification[randint(0,4)]

        videoessaytitleB = ["the problem with", "in defense of", f"the {blank}ification of", "the rise and fall of", ]
        prefix = videoessaytitleB[randint(0,3)]

        issue = ["forced diversity", "tiktok", "AI art", "smosh", "masturbation", "porn", "velma", "pedophillia", "beastiality", "necrophilia", "channel awesome", "creepshow art", "yandere dev", "keffals", "debate bros", "nikocado avocado", "mrbeast", "pedophiles", "zoophiles", "vaush", "necrophiles"]
        subject = issue[randint(0,20)]
        
        compositestatement = f"{prefix} {subject}"

        return(compositestatement)


while True:
    print(videoessaygenerator())