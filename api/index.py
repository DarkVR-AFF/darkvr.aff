@app.route('/api/TitleData', methods=['POST', 'GET'])
def titledata():
    response_data = {
        "AutoMuteCheckedHours": {
            "hours": 169
        },
        "AutoName_Adverbs": [
            "Cool", "Fine", "Bald", "Bold", "Half", 
            "Only", "Calm", "Fab", "Ice", "Mad", 
            "Rad", "Big", "New", "Old", "Shy"
        ],
        "AutoName_Nouns": [
            "Gorilla", "Chicken", "Darling", "Sloth", "King", 
            "Queen", "Royal", "Major", "Actor", "Agent", 
            "Elder", "Honey", "Nurse", "Doctor", "Rebel", 
            "Shape", "Ally", "Driver", "Deputy"
        ],
        "CreditsData": [
            {
                "Title": "DEV TEAM",
                "Entries": [
                    "LUCKY"
                ]
            },
            {
                "Title": "SPECIAL THANKS",
                "Entries": [
                    "SILLY GOOBERMAN (OWNER)",
                    "SYSTEM",
                    "TAS DIAM",
                    "JOHN PORK",
                    "LEMMING"
                ]
            },
            {
                "Title": "MUSIC BY",
                "Entries": [
                    "Stunshine",
                    "David Anderson Kirk",
                    "Jaguar Jen",
                    "Audiopfeil",
                    "Owlobe"
                ]
            }
        ],
        "BundleBoardSign": "<color=#ff4141>DISCORD.GG/BVSrswWYay</color>",
        "BundleKioskButton": "<color=#ff4141>DISCORD.GG/BVSrswWYay</color>",
        "BundleKioskSign": "<color=#ff4141>DISCORD.GG/BVSrswWYay</color>",
        "BundleLargeSign": "<color=#ff4141>DISCORD.GG/BVSrswWYay</color>",
        "EmptyFlashbackText": "FLOOR TWO NOW OPEN\n FOR BUSINESS\n\nSTILL SEARCHING FOR\nBOX LABELED 2021",
        "EnableCustomAuthentication": True,
        "GorillanalyticsChance": 4320,
        "LatestPrivacyPolicyVersion": "2024.09.20",
        "LatestTOSVersion": "2024.09.20",
        "MOTD": "<color=green>WELCOME TO AFF TAGGGERS!</color>\n<color=red>HJMAN 25 UPD!</color>\n<color=blue>OWNERS: DARKVR,LIGHTVR AND WLFVR\nCREDITS: DARKVR</color>\n<color=yellow>DISCORD.GG/BVSrswWYay</color>",
        "SeasonalStoreBoardSign": "<color=#80ff00>RATE THE GAME 5 STARS!</color>\n\n<color=#00ff88>.GG/BVSrswWYay</color>",
        "TOS_2024.09.20": "DISCORD.GG/BVSrswWYay",
        "TOBAlreadyOwnCompTxt": "DISCORD.GG/BVSrswWYay",
        "TOBAlreadyOwnPurchaseBundle": "RETRO",
        "TOBDefCompTxt": "DISCORD.GG/BVSrswWYay",
        "TOBDefPurchaseBtnDefTxt": "RETRO",
        "UseLegacyIAP": False
    }
    return jsonify(response_data)
