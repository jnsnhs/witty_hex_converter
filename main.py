# DISCLAIMER: Die Inhalte in der Klasse TEXT sind zum Großteil mit Hilfe von
# Google Gemini generiert worden. Normalerweise wäre es mein Anspruch, solche
# Texte selbst zu formulieren, aber dafür war nun wirklich keine Zeit ;)
# Außerhalb der Klasse TEXT wurde selbstverständlich nicht auf den Einsatz der
# KI zurückgegriffen. Dafür macht mir das Basteln und Tüfteln am Code viel zu
# viel Spaß. Warum sollte ich mir dieses Vergnügen von einer KI rauben lassen?
#
# Die Zahlen, die in der Funktion get_contrasting_color() mit den
# RGB-Werten multipliziert weden, sind folgendem Blog-Artikel entnommen:
# https://nemecek.be/blog/172/how-to-calculate-contrast-color-in-python
# Mir ist nicht bekannt, wie der Autor auf die Werte gekommen ist, vielleicht
# durch Ausprobieren. Möglicherweise steckt auch mehr dahinter. Jedenfalls 
# sorgen die Werte dafür, dass für eine beliebige RGB-Farbe sehr treffsicher
# ermittelt wird, ob Schwarz oder Weiß den besseren Kontrast darstellt.

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msgbox
from random import random, randint, choice, choices
import time
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

CANVAS_WIDTH = 1024    # Diese Werte können auf 1920x1080 gesetzt werden,
CANVAS_HEIGHT = 768    # um das versteckte Spiel in HD spielen zu können ;)

COLOR_NAMES =  {
    "AliceBlue": "F0F8FF",
    "AntiqueWhite": "FAEBD7",
    "Aquamarine": "7FFFD4",
    "Azure": "F0FFFF",
    "Beige": "F5F5DC",
    "Bisque": "FFE4C4",
    "Black": "000000",
    "BlanchedAlmond": "FFEBCD",
    "Blue": "0000FF",
    "BlueViolet": "8A2BE2",
    "Brown": "A52A2A",
    "BurlyWood": "DEB887",
    "CadetBlue": "5F9EA0",
    "Chartreuse": "7FFF00",
    "Chocolate": "D2691E",
    "Coral": "FF7F50",
    "CornflowerBlue": "6495ED",
    "Cornsilk": "FFF8DC",
    "Crimson": "DC143C",
    "Cyan/Aqua": "00FFFF",
    "DarkBlue": "00008B",
    "DarkCyan": "008B8B",
    "DarkGoldenrod": "B8860B",
    "DarkGray": "A9A9A9",
    "DarkGreen": "006400",
    "DarkKhaki": "BDB76B",
    "DarkMagenta": "8B008B",
    "DarkOliveGreen": "556B2F",
    "DarkOrange": "FF8C00",
    "DarkOrchid": "9932CC",
    "DarkRed": "8B0000",
    "DarkSalmon": "E9967A",
    "DarkSeaGreen": "8FBC8F",
    "DarkSlateBlue": "483D8B",
    "DarkSlateGray": "2F4F4F",
    "DarkTurquoise": "00CED1",
    "DarkViolet": "9400D3",
    "DeepPink": "FF1493",
    "DeepSkyBlue": "00BFFF",
    "DimGray": "696969",
    "DodgerBlue": "1E90FF",
    "FireBrick": "B22222",
    "FloralWhite": "FFFAF0",
    "ForestGreen": "228B22",
    "Gainsboro": "DCDCDC",
    "GhostWhite": "F8F8FF",
    "Gold": "FFD700",
    "Goldenrod": "DAA520",
    "Gray": "808080",
    "Green": "008000",
    "GreenYellow": "ADFF2F",
    "Honeydew": "F0FFF0",
    "HotPink": "FF69B4",
    "IndianRed": "CD5C5C",
    "Indigo": "4B0082",
    "Ivory": "FFFFF0",
    "Khaki": "F0E68C",
    "Lavender": "E6E6FA",
    "LavenderBlush": "FFF0F5",
    "LawnGreen": "7CFC00",
    "LemonChiffon": "FFFACD",
    "LightBlue": "ADD8E6",
    "LightCoral": "F08080",
    "LightCyan": "E0FFFF",
    "LightGoldenrodYellow": "FAFAD2",
    "LightGray": "D3D3D3",
    "LightGreen": "90EE90",
    "LightPink": "FFB6C1",
    "LightSalmon": "FFA07A",
    "LightSeaGreen": "20B2AA",
    "LightSkyBlue": "87CEFA",
    "LightSlateGray": "778899",
    "LightSteelBlue": "B0C4DE",
    "LightYellow": "FFFFE0",
    "Lime": "00FF00",
    "LimeGreen": "32CD32",
    "Linen": "FAF0E6",
    "Magenta/Fuchsia": "FF00FF",
    "Maroon": "800000",
    "MediumAquamarine": "66CDAA",
    "MediumBlue": "0000CD",
    "MediumOrchid": "BA55D3",
    "MediumPurple": "9370DB",
    "MediumSeaGreen": "3CB371",
    "MediumSlateBlue": "7B68EE",
    "MediumSpringGreen": "00FA9A",
    "MediumTurquoise": "48D1CC",
    "MediumVioletRed": "C71585",
    "MidnightBlue": "191970",
    "MintCream": "F5FFFA",
    "MistyRose": "FFE4E1",
    "Moccasin": "FFE4B5",
    "NavajoWhite": "FFDEAD",
    "Navy": "000080",
    "OldLace": "FDF5E6",
    "Olive": "808000",
    "OliveDrab": "6B8E23",
    "Orange": "FFA500",
    "OrangeRed": "FF4500",
    "Orchid": "DA70D6",
    "PaleGoldenrod": "EEE8AA",
    "PaleGreen": "98FB98",
    "PaleTurquoise": "AFEEEE",
    "PaleVioletRed": "DB7093",
    "PapayaWhip": "FFEFD5",
    "PeachPuff": "FFDAB9",
    "Peru": "CD853F",
    "Pink": "FFC0CB",
    "Plum": "DDA0DD",
    "PowderBlue": "B0E0E6",
    "Purple": "800080",
    "RebeccaPurple": "663399",
    "Red": "FF0000",
    "RosyBrown": "BC8F8F",
    "RoyalBlue": "4169E1",
    "SaddleBrown": "8B4513",
    "Salmon": "FA8072",
    "SandyBrown": "F4A460",
    "SeaGreen": "2E8B57",
    "Seashell": "FFF5EE",
    "Sienna": "A0522D",
    "Silver": "C0C0C0",
    "SkyBlue": "87CEEB",
    "SlateBlue": "6A5ACD",
    "SlateGray": "708090",
    "Snow": "FFFAFA",
    "SpringGreen": "00FF7F",
    "SteelBlue": "4682B4",
    "Tan": "D2B48C",
    "Teal": "008080",
    "Thistle": "D8BFD8",
    "Tomato": "FF6347",
    "Turquoise": "40E0D0",
    "Violet": "EE82EE",
    "Wheat": "F5DEB3",
    "White": "FFFFFF",
    "WhiteSmoke": "F5F5F5",
    "Yellow": "FFFF00",
    "YellowGreen": "9ACD32"
    }


class TEXT:
    
    APP_TITLE = "HEX 9000"
    DEFAULT_COMMENT = "Bitte geben Sie einen gültigen\nHex-Wert ein oder wählen Sie eine\nder vordefinierten Webfarbe aus."
    LABEL_RANDOM_BTN = "Zufallswert ausgeben"
    LABEL_SECRET_BTN = "\"Hex-Huhn\" spielen"
    LABEL_CONVERT_BTN = "Nach RGB konvertieren"
    LABEL_CHECKBOX = "Fenster immer oben anzeigen"
    LABEL_INVALID_INPUT = "Eingabe\nungültig"
    LABEL_EMPTY_INPUT = "Leere\nEingabe"
    LABEL_TRANSPARENT_COLOR = "Anzeige\nnicht möglich"
    LABEL_SECRET_UNLOCKED = "Bonus-Spiel\nfreigeschaltet"
    EXIT_CONF_TITLE = "Obacht!"
    EXIT_CONF_MSG = "Wollen Sie das Programm wirklich beenden?"
    EXIT_CONF_DETAIL = "Sie haben noch längst nicht alles gesehen, was dieses unscheinbare Tool zu bieten hat. Konvertieren Sie doch noch ein paar weitere Farben. Es könnte sich lohnen... Oder haben Sie heute noch etwas vor?"
    SECRET_TITLE = "Herzlichen Glückwunsch!"
    SECRET_MSG = "Menschenskind, jetzt Sie haben schon 42 verschiedene Farben konvertiert! Wissen Sie, was das bedeutet? "
    SECRET_DETAIL = "Erstens: Sie sind ein ganz schöner Farben-Nerd...\n\nZweitens: Sie haben ein verstecktes Spiel freigeschaltet! Ja, ganz richtig! Klicken Sie doch mal auf den Button, der neu hinzugekommen ist.\n\nKleiner Tipp: In Zukunft brauchen Sie nicht mehr endlos zu klicken, sondern können das Spiel direkt freischalten, indem Sie \"hexhuhn\" eingeben. Praktisch, oder?"
    CHEAT_USED = "Sie machen es sich ja sehr einfach..."
    CHEAT_CODE = "hexhuhn"
    NAMED_CODES = {
        "F0F8FF": ("Wer ist Alice, und warum hat ihre spezielle Art von Blau einen eigenen Namen? Fragen über Fragen.", "Das Blau des Himmels im ersten Level von \"Sonic the Hedgehog\". Unschuldig, bevor die Geschwindigkeit kommt.", "Die Farbe des Himmels über der Steuererklärung, bevor der Frust einsetzt.", "Die Farbe, die Alice sah, nachdem sie durch den Kaninchenbau fiel und der Kuchen ein bisschen zu stark war. Sehr verträumt."),
        "FAEBD7": ("Antikes Weiß. Wahrscheinlich die Farbe von Omas Gardinen, die mal weiß waren.", "Der Farbton des alten Buches, das man schon ewig lesen wollte, aber nie dazu kommt.", "Die Farbe der Tapeten, die nach dem Wirtschaftswunder in jeder guten Stube hingen. Gediegen und leicht vergilbt.", "Die Farbe von Omas Spitzendeckchen, das seit der Titanic-Ära niemand mehr gewaschen hat. Hat definitiv Charakter."),
        "7FFFD4": ("Klingt nach einem Juwel aus dem Meer. Sieht aus wie ein leicht bläuliches Grün, das sich wichtig macht.", "Der Farbton des Juwels, das man in einem obskuren Point-and-Click-Adventure aus dem 90er-Jahre-Inventar zieht. Sehr wertvoll.", "Die Farbe des Meeres in den Urlaubskatalogen für Mallorca. Ein Traum in Türkis.", "Die Farbe des Ozeans, aus dem Arielle auftauchen könnte. Oder des Schmuckstücks, das man ihr vom Hals gerissen hat."),
        "F0FFFF": ("Himmelblau. Versucht, so unendlich zu wirken wie der Himmel. Ist aber nur ein Farbcode.", "Das Blau, das über dem Traumland von \"Peter Pan\" liegt. Oder die Lieblingsfarbe jedes Marketing-Heinis, der \"unendlich\" verkaufen will.", "Das Blau der Social-Media-Benachrichtigung, die man lieber ignoriert hätte.", "Der unendliche Himmel, den man sich vorstellt, wenn man im Stau steht."),
        "F5F5DC": ("Die Farbe der puren Mittelmäßigkeit. Weder Fisch noch Fleisch, einfach nur... Beige.", "Die Farbe des ersten PC-Gehäuses, auf dem man \"Doom\" gespielt hat. Unauffällig, aber mit teuflischer Power innen", "Das Beige der Bonner Republik. Funktional, unauffällig, aber stabil wie der Kanzlerbungalow.", "Die Farbe der Tapete in jedem 80er-Jahre-Büro, das nicht vom Chaos Computer Club gehackt wurde. Sehr unauffällig."),
        "FFE4C4": ("Der Teint nach einem Online-Meeting, das eigentlich eine E-Mail hätte sein können.", "Die Hautfarbe nach dem ersten Sonnenbrand des Jahres, den man unbedingt vermeiden wollte.", "Die Gesichtsfarbe deines Spielcharakters, nachdem er in \"Mortal Kombat\" einen Fatality abbekommen hat. Sehr blass", "Klingt nach dem Teint einer Comicfigur, die gerade den Schock ihres Lebens erlebt hat. So bleich wie ein Geist."),
        "000000": ("Schwarz. Elegant, geheimnisvoll. Oder einfach nur die Abwesenheit von Licht. Kommt drauf an, wen man fragt.", "Die Farbe des Kaffees am Montagmorgen, ohne den nichts geht.", "Der Hintergrund in \"Space Invaders\". Oder der Ladebildschirm. Oder die Farbe der Angst, wenn die Gegner kommen.", "Die Farbe von Batmans Umhang, Darth Vaders Rüstung und dem Kaffe in den frühen Morgenstunden. Sehr dominant."),
        "FFEBCD": ("Blassgebleichte Mandel. Klingt nach etwas, das man auf einer Diät isst und das nach nichts schmeckt.", "Die Hautfarbe nach einer durchzechten Nacht, die man lieber vergessen würde.", "Der Farbton der ersten Bio-Mandelmilch in den 80ern, als \"gesunde Ernährung\" noch ein Nischenthema war. Sehr blass und teuer.", "Die Farbe einer Mandel, die zu lange in der Sauna war. Oder die Hautfarbe eines Charakters aus \"Twilight\" bei Tageslicht."),
        "0000FF": ("Blau. Der Klassiker. Die Farbe des Himmels, des Meeres... und der gefürchteten Fehlermeldung.", "Der Montags-Morgen-Blues, der sich durch die ganze Woche zieht.", "Sonics Fellfarbe, Mega Mans Rüstung, oder der Blue Shell in \"Mario Kart\". Ein omnipräsenter Albtraum oder Retter.", "Das Blau der TARDIS, der Schlumpfhaut und des Cookie Monsters. Weniger ein Farbton, mehr ein Lebensgefühl."),
        "8A2BE2": ("Blau trifft Violett. Kann sich nicht entscheiden. Ein bisschen schüchtern.", "Die Farbe des Laserstrahls, der dich in einem Arcade-Shooter trifft. Schmerzhaft und pixelig.", "Die Farbe von Captain Kirk, wenn er sich nicht entscheiden kann, ob er Forschung oder Diplomatie betreiben soll.", "Das Lila des Zaubertranks, der laut Etikett alles kann, aber nichts bewirkt."),
        "A52A2A": ("Braun. Erdverbunden. Oder einfach nur langweilig.", "Die Farbe von Donkey Kongs Fell. Oder der Holzkisten in jedem zweiten 90er-Jahre-Jump'n'Run.", "Das Braun der guten alten Holzvertäfelung in den 70er-Jahren. Gemütlich und ein bisschen muffig.", "Die Farbe von Chewbacca, Groot und dem guten alten Schokopudding. Erdverbunden und verlässlich."),
        "DEB887": ("Klingt nach kernigem Holz. Sieht aus wie... braun. Mit einem Hauch von Beige. Sehr kernig.", "Das Furnier der Einbauküche aus den 80ern, die immer noch ihren Dienst tut.", "Die Farbe der Bäume im \"Secret of Mana\" auf dem SNES. Sehr detailliert für damalige Verhältnisse.", "Der Farbton von Holz, das schon bei \"Herr der Ringe\" im Auenland stand. Rustikal und zeitlos."),
        "5F9EA0": ("Kadettenblau. Die Farbe der Disziplin? Sieht eher aus wie ein blasses Blaugrün, das Befehle entgegennimmt.", "Die Uniformfarbe jedes übermotivierten Security-Mitarbeiters im Supermarkt.", "Die Uniform des Kundendienstmitarbeiters, der leider nicht helfen kann.", "Das Blau der unglücklichen Starfleet-Kadetten, die bei Außenmissionen immer als Erste verschwinden. Sehr unauffällig."),
        "7FFF00": ("Klingt nach einem exotischen Likör. Sieht aus wie... giftiges Grün. Vorsicht!", "Der Smoothie, der so gesund sein soll, aber schmeckt wie Rasenmäher-Reste.", "Das Grün des Codes, der über den Bildschirm läuft, wenn man in einem DOS-Spiel die Cheats eingibt. Geheimnisvoll.", "Die Farbe von Absinth und dem Code in der Matrix. Sehr intellektuell, aber auch ein bisschen giftig."),
        "D2691E": ("Schokolade! Sieht aus wie Vollmilchschokolade. Macht aber nicht glücklich (oder dick).", "Die Farbe des Gewissens, nachdem man die ganze Tafel aufgegessen hat.", "Die Farbe, die man nach einer durchzechten Nacht im Kühlschrank sucht. Verspricht Glück, liefert aber nur einen Farbcode.", "Das tiefe Braun der Schokolade, die man sich nach einem anstrengenden Tag gönnt - und dann bereut."),
        "FF7F50": ("Koralle. Sieht aus wie etwas, das im Meer wächst. Versucht, tropisch zu wirken.", "Der Lippenstift, der laut Werbung perfekt ist, aber niemandenem steht.", "Der Korallenriff-Print auf dem Hemd, das man nur im Urlaub trägt.", "Die Farbe des Urlaubs-Souvenirs, das zu Hause nur noch seltsam aussieht."),
        "6495ED": ("Kornblumenblau. Eine sehr spezifische Blume, für eine sehr spezifische Farbe. Ist das ein Wettbewerb?", "Der Himmel über dem Schrebergarten, wenn man gerade mit dem Rasenmähen fertig ist.", "Der Himmel, den man nur noch auf alten Postkarten sieht.", "Das Blau einer Blume, die so unscheinbar ist, dass selbst die Schlümpfe sie kaum bemerken würden."),
        "FFF8DC": ("Die Farbe des vergilbten Rezepts von Oma, das man angeblich nie umsetzen konnte, weil die Schrift zu klein war.", "Der Farbton der ersten Sonnencreme-Schicht im Frühling, die garantiert keinen Sonnenbrand verhindert.", "Das unschuldige Gelb des Antragsformulars, das man in dreifacher Ausfertigung ausfüllen muss, nur um dann doch eine Nummer ziehen zu müssen.", "Der dezente Schimmer des ungelesenen E-Books, das seit Monaten auf dem E-Reader schlummert."),
        "DC143C": ("Das Rot der Wut, wenn der Drucker mal wieder streikt.", "Das intensive Rot der Kreditkartenabrechnung, die man lieber ignoriert.", "Die Farbe des Blutes in \"Doom\", wenn man die Gegner in Stücke schießt. Sehr... präsent.", "Die Farbe des Blutes in einem Quentin-Tarantino-Film. Sehr dramatisch und ein bisschen übertrieben."),
        "00FFFF": ("Sehr nass klingende Farbe. Ist es Wasser? Oder einfach nur Türkis, das einen kühlen Namen wollte?", "Cyan. Eine der Druckfarben. Ohne Magenta und Gelb ziemlich allein.", "Die Farbe der ersten Tintenstrahldrucker-Kartuschen. Digital und verbraucht sich zu schnell.", "So frisch und klar, dass es direkt aus dem Pool einer 90er-Jahre-Strandparty stammen könnte. Neon-Style!"),
        "00008B": ("Dunkelblau. Ernster als normales Blau. Hat wahrscheinlich eine Aktentasche.", "Der Tiefpunkt der Motivation an einem regnerischen Novembertag.", "Die Tiefen der Suchmaschinen-Historie, in die man lieber nicht blickt.", "Die Farbe des Tiefpunkts der Motivation, wenn der Akku bei 1 Prozent ist"),
        "008B8B": ("Dunkles Cyan. Noch geheimnisvoller als normales Cyan. Versteckt sich im tiefen Wasser.", "Die Farbe von Gotham City in einer regnerischen Nacht, bevor Batman auftaucht. Geheimnisvoll und ein bisschen gruselig.", "Die Farbe des vergessenen Gemüses im Kühlschrank, das seine Eigenleben entwickelt hat.", "Die Farbe des verschimmelten Brots im Kühlschrank, das man vergessen hat."),
        "B8860B": ("Dunkles Goldruten-Gelb. Klingt nach einer Farbe, die man im Herbst findet. Nicht so glänzend wie echtes Gold.", "Das Gold des \"Zelda\"-Tri-Force, wenn es sich nicht ganz offenbart. Geheimnisvoll.", "Der vergilbte Glanz der guten alten Zeiten, die nie so gut waren.", "Das Gold, das Midas berührt hätte, wenn er gerade ein bisschen müde gewesen wäre. Nicht ganz so glänzend."),
        "A9A9A9": ("Dunkelgrau. Fast Schwarz, aber traut sich nicht. Die Farbe des Zweifels.", "Die Farbe der Dungeons in \"Diablo\". Düster und voller Monster.", "Der Anzug, den man trägt, wenn man eigentlich nicht auffallen will.", "Der Farbton des urbanen Betons, der jede Freude erstickt."),
        "006400": ("Dunkelgrün. Sehr waldig. Oder die Farbe eines schlecht gelaunten Frosches.", "Das Moos auf dem Dach, das dringend entfernt werden müsste.", "Das Grün der Umweltbewegung in den 80ern, bevor die Grünen salonfähig wurden. Radikal und unnachgiebig.", "Die Farbe von Yodas Robe und dem Sherwood Forest. Sehr weise und ein bisschen schattig."),
        "BDB76B": ("Dunkles Khaki. Bereit für die Safari, aber nur auf dem Bildschirm.", "Die Farbe der Wüste in \"Dune 2\". Sehr staubig und strategisch.", "Die Farbe von Indiana Jones' Hose nach einem besonders staubigen Abenteuer. Bereit für alles.", "Die Farbe der verstaubten Wandfarbe im Baumarkt, die niemand will."),
        "8B008B": ("Dunkles Magenta. Sehr intensiv. Hat wahrscheinlich eine dunkle Vergangenheit.", "Die Farbe der Laserstrahlen in einem Arcade-Shooter. Sehr gefährlich.", "Das Ergebnis eines Waschgangs mit einem roten Socken unter der Weißwäsche.", "Der Fleck auf dem Teppich, der nach dem Unfall mit Rotwein zurückbleibt."),
        "556B2F": ("Dunkles Olivgrün. Sieht aus, als hätte es zu lange in der Sonne gelegen.", "Die Farbe der Bäume in einem frühen \"Command & Conquer\"-Spiel. Sehr taktisch.", "Die Farbe des Dschungels, in dem Rambo sich versteckt. Oder das Ergebnis eines schlechten Mischens.", "Das Gemüse auf dem Teller, das man nur widerwillig isst."),
        "FF8C00": ("Dunkelorange. Noch lauter als normales Orange. Will unbedingt gesehen werden.", "Das Orange der Explosion, die zu groß war, um ins Bild zu passen. Sehr dramatisch.", "Der Sonnenuntergang, der von Hochhäusern verdeckt wird.", "Der Sonnenuntergang über dem Industriegebiet, der doch irgendwie traurig ist."),
        "9932CC": ("Dunkle Orchidee. Klingt exotisch. Sieht aus wie ein tiefes Lila. Weniger blumig als gedacht.", "Das Lila des seltenen Gewürzes, das man einmal gekauft und nie wieder benutzt hat.", "Das Lila der vergessenen Socke, die aus der Wäsche verschwunden ist.", "Der Farbton der Orchidee, die man geschenkt bekommt und dann vertrocknen lässt."),
        "8B0000": ("Dunkelrot. Leidenschaftlich, aber zurückhaltend. Oder einfach nur... dunkelrot.", "Die Farbe des Blutes in \"Mortal Kombat\" (die unzensierte Version!). Sehr explizit.", "Die Farbe eines Vampirs, der gerade zu Abend gegessen hat. Oder der Lippenstift einer Femme Fatale.", "Die Farbe der Zornesröte, wenn die Internetverbindung abbricht."),
        "E9967A": ("Dunkler Lachs. Klingt essbar, ist es aber nicht. Sieht aus wie ein leicht angebrannter Lachs.", "Der Lachs, der im \"Schlemmer-Atlas\" der 80er-Jahre als exotisches Gericht gefeiert wurde. War damals total hip.", "Der Lachs, der den ganzen Weg gegen den Strom geschwommen ist. Sehr zäh, aber nicht unbedingt appetitlich.", "Die Farbe des Fischgerichts, das auf der Speisekarte besser klang."),
        "8FBC8F": ("Das trübe Wasser im Gartenteich, das dringend gereinigt werden müsste.", "Die Farbe des Nordsee-Wassers, wenn man im Herbst an der Küste spaziert. Rau und unnahbar.", "Die Farbe des Meeres in einem Horrorfilm, kurz bevor etwas Großes auftaucht. Sehr unruhig.", "Der Algenteppich auf dem Teich, der jeden Sommer wiederkommt."),
        "483D8B": ("Dunkles Schieferblau. Klingt nach einem sehr spezifischen Stein an einem sehr spezifischen Ort.", "Die Stimmung nach einer Diskussion über Politik, die ins Leere läuft.", "Das Blau des Himmels kurz vor dem Alien-Angriff. Sehr bedrohlich.", "Der Blick in die Augen des Politikers, der gerade eine unbequeme Wahrheit verkündet."),
        "2F4F4F": ("Dunkles Schiefergrau. Noch ein Schiefer-Fan. Wahrscheinlich die Farbe des Bedauerns.", "Die Farbe des schlechten Gewissens, wenn man wieder zu spät dran ist.", "Die Farbe des Schotters, auf dem das Auto nach einer Panne steht.", "Die Farbe des Schiefers, der in \"Game of Thrones\" für den Winterpalast verwendet wurde. Hart und kalt."),
        "00CED1": ("Dunkles Türkis. Ein bisschen mysteriös.", "Der Meerblick, der durch die Baukräne im Vordergrund verdeckt wird.", "Die Farbe des verborgenen Schatzes am Grunde des Meeres. Tief und mysteriös.", "Der Meerblick, der von einem riesigen Kreuzfahrtschiff blockiert wird."),
        "9400D3": ("Dunkles Violett. Sehr intensiv, fast schon bedrohlich. Die Farbe der Übertreibung.", "Die Farbe des Umhangs eines Bösewichts aus einem 80er-Jahre-Comic. Sehr theatralisch.", "Die Farbe der letzten, traurigen Aubergine im Supermarkt.", "Die Farbe des Flecks auf dem Shirt, der einfach nicht rausgehen will."),
        "FF1493": ("Tiefes Pink. Versucht, dramatischer zu sein als normales Pink. Mission erfüllt.", "Die übertrieben freundliche Farbe der Werbung für billige Handyverträge.", "Das Pink der ersten \"Love Parade\" in Berlin. Sehr exzessiv und grenzüberschreitend.", "Barbies Lieblingsfarbe. Wenn sie nicht gerade in ihrem Traumhaus weilt, dann in diesem Farbton."),
        "00BFFF": ("Tiefes Himmelblau. Sieht aus, als würde der Himmel gleich eine Träne vergießen.", "Der Himmel über dem Flughafen, kurz bevor man stundenlang Verspätung hat.", "Die Farbe des Himmels, der gerade von Superman durchbrochen wurde. Sehr heroisch.", "Das strahlende Blau der Werbung für unbezahlbare Luxusreisen."),
        "696969": ("Dämmriges Grau. Das Grau kurz vor der Nacht. Oder kurz vorm Einschlafen.", "Die Farbe des Game Boys, wenn die Batterien fast leer sind. Sehr schwach.", "Die Farbe eines alten Schwarz-Weiß-Films, der langsam verblasst. Nostalgisch, aber auch ein bisschen traurig.", "Die Farbe des Moments, in dem man merkt, dass man den Schlüssel vergessen hat."),
        "1E90FF": ("Klingt nach einem cleveren Blau. Ist es schneller als andere Farben? Eher nicht.", "Der Blaustich des Bildschirms, der die Augen müde macht.", "Die Farbe des blauen Hakens, der anzeigt, dass die Nachricht gelesen, aber ignoriert wurde.", "Das aggressive Blau des Polizeilichts im Rückspiegel."),
        "B22222": ("Feuerziegel. Sieht aus wie ein Ziegelstein, der schon einiges mitgemacht hat. Brennt aber nicht.", "Die Ziegelwand, die man im Großraumbüro zur \"Auflockerung\" hat.", "Die Farbe der Ziegelsteine in \"Super Mario Bros.\", die man mit dem Kopf kaputtschlagen muss. Sehr stabil.", "Die Backsteinwand des Nachbarn, der immer den Grill anwirft, wenn man lüften will."),
        "FFFAF0": ("Blumiges Weiß. Klingt nach Hochzeit. Sieht aus wie... fast weiß.", "Die Farbe des Explosionseffekts in einem Arcade-Shooter. Sehr kurzlebig.", "Die Farbe der Bluse, die man sich kauft und nie anzieht, weil sie zu empfindlich ist.", "Das reine Weiß der Zahnpasta-Werbung, die falsche Versprechungen macht."),
        "228B22": ("Waldgrün. Die Farbe der Bäume. Sehr... grün.", "Die Farbe des Waldes, der bald für einen neuen Parkplatz weichen muss.", "Die Farbe von Robin Hoods Kleidung. Perfekt zum Verstecken im Wald und zum Stehlen von Reichen.", "Die Farbe des Waldes, der laut Navi nur noch 50 Meter entfernt ist, aber nicht sichtbar ist."),
        "DCDCDC": ("Klingt nach einem englischen Landhaus. Ist aber nur ein blasses Grau. Sehr unspektakulär.", "Die Farbe des Wartesaals beim Amt, in dem die Zeit stillsteht.", "Das Grau der Betonsiedlungen der 60er und 70er, die \"modernes Wohnen\" versprachen. Sehr funktional.", "Eine Farbe, die so langweilig ist, dass selbst ein CSI-Ermittler nichts Verdächtiges daran finden würde."),
        "F8F8FF": ("Geisterweiß. Die Farbe eines sehr blassen Geistes. Sieht aus wie fast weiß, das Angst hat, weiß zu sein.", "Die Farbe des Gehaltszettels, nachdem alle Abzüge weg sind.", "Die Farbe der Geister in \"Pac-Man\", wenn sie essbar sind. Sehr vergänglich.", "Die Farbe des vergessenen Zettels, der wichtig war, aber spurlos verschwunden ist."),
        "FFD700": ("Gold. Glänzt nicht so schön wie echtes Gold. Aber immerhin heißt es so.", "Die Farbe der Münzen in \"Super Mario 64\". Sehr glänzend und begehrt.", "Die Farbe der leeren Versprechungen, die man immer wieder hört.", "Der Glanz des Pokals, der nach dem Sieg im Schrank verstaubt."),
        "DAA520": ("Goldrute. Eine Blume, die zur Farbe wurde. Oder eine Farbe, die sich nach einer Blume benannt hat.", "Der Farbton des Senfes, der seine besten Tage hinter sich hat.", "Das Gold der Pixel, die man in einem 8-Bit-Rollenspiel findet. Nicht viel, aber immerhin.", "Das Gold, das man findet, wenn man zu lange in der Prärie war. Ein bisschen staubig und nicht so glänzend."),
        "808080": ("Grau. Die neutrale Zone. Die Farbe der Entscheidungsunfähigkeit.", "Die Farbe des Alltags, wenn man keine Lust auf Abenteuer hat.", "Die Farbe des Original-Game-Boy-Bildschirms. Monochrom, aber revolutionär.", "Die Farbe der Mitte, wo sich niemand entscheiden kann. Oder des Wetters an einem Montag."),
        "008000": ("Grün. Natur! Hoffnung! Oder einfach nur die Farbe, wenn Rot und Blau fehlen.", "Die Ampel, die immer rot wird, wenn man es eilig hat.", "Die Ampel, die man immer verpasst.", "Die Farbe von Hulk, Shrek und Yoda. Sehr stark, aber auch ein bisschen... moosig."),
        "ADFF2F": ("Grünlich-Gelb. Kann sich nicht entscheiden, ob es grün oder gelb sein will. Identitätskrise.", "Das Gefühl nach dem ersten Bissen ins unbekannte Streetfood.", "Die Farbe des Lebensbalkens, wenn er noch ganz voll ist. Sehr beruhigend.", "Die Farbe eines Limetten-Slushies, der etwas zu lange in der Sonne stand. Kritisch."),
        "F0FFF0": ("Honigmelone. Klingt süß. Sieht aus wie... blassgrün. Nicht lutschen!", "Der Geschmack der Melone, die einfach nicht reif werden will.", "Die Farbe der \"Heiltränke\", die man in einem 90er-Jahre-RPG findet. Sehr nahrhaft.", "Die Farbe der Melone, die man auf einem Luxusschiff bekommt, kurz bevor es sinkt. Sehr blass."),
        "FF69B4": ("Heißes Pink. Schreit nach Aufmerksamkeit und bekommt sie. Vorsicht, Augenkrebsgefahr!", "Die grelle Farbe des Neonschilds, das nachts vor der billigen Bar blinkt.", "Die Farbe der Neonlichter in einem 80er-Jahre-Arcade-Racer. Sehr schnell.", "Die Farbe des Aerobic-Outfits in den 80ern. Oder Barbies heißester Traum."),
        "CD5C5C": ("Indisches Rot. Klingt exotisch und geheimnisvoll. Sieht aus wie ein gedämpftes Rot. Weniger aufregend als der Name.", "Der verfärbte Teppich, den man mit einem Läufer versteckt.", "Die Farbe eines alten Western-Films, wenn die Sonne untergeht. Romantisch und ein bisschen klischeehaft.", "Der Farbton des alten Vorhangs, der seine besten Tage hinter sich hat."),
        "4B0082": ("Die Farbe der Augenringe nach einer Nachtschicht, in der man versucht hat, ein unerklärliches Softwareproblem zu lösen.", "Die Farbe des Platten-Covers einer obskuren Band, die man nur kennt, um intellektuell zu wirken."),
        "FFFFF0": ("Elfenbein. Die Farbe des Elfenbeins. Hoffentlich wurde dafür kein Elefant... naja.", "Die Tasten des Klaviers, auf dem man nie gelernt hat zu spielen.", "Die vergilbten Seiten des Schulbuches, das man nie aufgeschlagen hat.", "Die Farbe der Klaviertasten, auf denen Beethoven seine Sonaten spielte. Klassisch und elegant."),
        "F0E68C": ("Khaki. Bereit für Abenteuer! Oder einfach nur praktisch.", "Die Farbe der Kleidung, die man anzieht, wenn man etwas Unangenehmes erledigen muss.", "Die Farbe des Bodens in \"Dune 2\". Sehr sandig.", "Die Farbe der Cargo-Hose, die man aus Gewohnheit immer noch trägt."),
        "E6E6FA": ("Lavendel. Riecht nicht, sieht aber so aus. Eine beruhigende Farbe, solange man nicht versucht, daran zu schnuppern.", "Die Farbe des Duftsäckchens, das seit Jahren im Schrank liegt.", "Die Farbe der Blumen, die man in einem alten Adventure-Game pflückt. Sehr unbedeutend.", "Die Farbe von Omas Duftseife. Beruhigend, aber auch ein bisschen altmodisch."),
        "FFF0F5": ("Lavendel-Rouge. Klingt nach Make-up für Feen. Sieht aus wie sehr blasses Rosa.", "Die leichte Schamröte, wenn man beim Schnarchen erwischt wird.", "Die Farbe einer Elfe, die gerade rot wird. Sehr zart und ein bisschen kitschig.", "Das errötende Gesicht, wenn man beim Tratschen erwischt wird."),
        "7CFC00": ("Rasengrün. Die Farbe des frisch gemähten Rasens. Riecht aber nicht so gut.", "Der akkurat gemähte Rasen des Nachbarn, der einen neidisch macht.", "Das Grün des Rasens, auf dem \"Mario Kart\" gefahren wird. Sehr gepflegt.", "Die Farbe des Rasens, der gerade gemäht wurde, um den Nachbarn zu beeindrucken. Riecht aber nicht so gut."),
        "FFFACD": ("Zitronen-Chiffon. Klingt wie ein leichter Kuchen. Sieht aus wie blasses Gelb. Nicht backen!", "Die Farbe des trockenen Zitronenkuchens, der auf der Party übrig bleibt.", "Die Farbe der trockenen Zitrone, die seit Wochen im Kühlschrank liegt.", "Das sanfte Gelb des vergilbten Notizblocks, der schon ewig unbenutzt ist."),
        "ADD8E6": ("Hellblau. Das unschuldige Blau. Hat noch keine Rechnungen bekommen.", "Der Himmel über dem Bürohochhaus an einem durchschnittlichen Tag.", "Das Blau des Himmels in \"Super Mario World\". Sehr freundlich.", "Das Blau des Babyzimmers, bevor das Baby anfängt, die Wände anzumalen. Unschuldig."),
        "F08080": ("Helle Koralle. Eine Koralle im Sonnenlicht? Sieht aus wie leichter Sonnenbrand.", "Die Farbe der geschönten Statistik, die bald widerlegt wird.", "Die Farbe der Herzen, die in \"Zelda\" deine Lebensenergie anzeigen. Sehr wertvoll.", "Die Koralle, die gerade aus dem Meer geholt wurde und noch nicht ganz trocken ist. Sehr frisch."),
        "E0FFFF": ("Helles Cyan. Sehr luftig. Könnte vom Wind weggeweht werden.", "Das kühle Licht des Kühlschranks, wenn man nachts nach Snacks sucht.", "Das kühle Leuchten des Bildschirms nach einer langen Nachtschicht.", "Die Farbe des ungenutzten Luftbefeuchters, der vor sich hin gammelt."),
        "FAFAD2": ("Helles Goldruten-Gelb. Ein sehr langer Name für ein sehr blasses Gelb. Muss seinen Namen wohl extra betonen.", "Der Schein der Energiesparlampe, die nicht richtig hell wird.", "Das Gelb der Sterne, die man in \"Super Mario 64\" sammelt. Sehr leuchtend.", "Das Gelb eines alten Fotos aus dem Urlaub. Verblasst, aber voller Erinnerungen."),
        "90EE90": ("Hellgrün. Frühling lässt grüßen! Oder einfach nur Grün mit einem Hauch von Gelb.", "Die Farbe eines frisch geschlüpften Dinosaurierbabys in einem Jurassic-Park-Film. Jung und wild.", "Das Grün des Ampellichts, das genau dann umschaltet, wenn man fast da ist.", "Das übertrieben gesunde Grün des Smoothies, der schmeckt wie Gras."),
        "D3D3D3": ("Hellgrau. Sieht aus wie das Grau kurz vor dem Weiß. Zögerlich.", "Die Farbe des Bodens im Ikea, wenn die Leute gerade durchgewischt haben. Sauber, aber nicht aufregend.", "Die Farbe des Game Boy Color im ausgeschalteten Zustand. Oder der Felsen in \"Tetris\".", "Das unauffällige Grau des Gebäudes, an dem man jeden Tag vorbeigeht."),
        "FFB6C1": ("Hellrosa. Das schüchterne Rosa. Traut sich nicht, Hot Pink zu sein.", "Das Rosa der Zuckerwatte, die klebrige Finger hinterlässt.", "Kirbys Hautfarbe, wenn er gerade einen Gegner verschluckt hat. Sehr süß.", "Das Rosa des Schleifchens am Haar eines Teddybären. Sehr niedlich."),
        "FFA07A": ("Heller Lachs. Sieht aus wie Lachs, der zu kurz gebraten wurde.", "Die Farbe des Lachsersatzes im Discounter.", "Der Aufschnitt im Kühlschrank, der sein Haltbarkeitsdatum erreicht hat.", "Der Lachs, der sich noch nicht ganz entschieden hat, ob er ein Fisch oder ein Flamingo sein will."),
        "20B2AA": ("Helles Seegrün. Taucht nicht so tief. Bleibt lieber flach.", "Das trübe Wasser am Seeufer, das man lieber nicht betritt.", "Das schimmernde Wasser im Pool, das noch nicht ganz sauber ist.", "Das Seegrün, das man vom Strand aus sieht. Nicht zu tief, nicht zu flach."),
        "87CEFA": ("Heller Himmelblau. Sieht aus wie ein Himmel kurz nach dem Regen. Hoffnungsvoll.", "Der Himmel über der Stadt, wenn man nach Hause pendelt.", "Der Blick aus dem Fenster, der zeigt, dass der Tag doch noch nicht vorbei ist.", "Das Blau des Himmels, kurz bevor Mary Poppins mit ihrem Regenschirm landet. Sehr optimistisch."),
        "778899": ("Helles Schiefergrau. Der Schiefer im vollen Licht. Nicht so mysteriös.", "Die Farbe des Smogs, der sich über die Autobahn legt.", "Die Farbe der Nebel des Grauens in einem alten Adventure-Game. Sehr mysteriös.", "Die Farbe des Schiefers an einem bewölkten Tag. Etwas gedämpft, aber immer noch Schiefer."),
        "B0C4DE": ("Helles Stahlblau. Klingt robust, ist aber nur hellblau. Ein bisschen Etikettenschwindel.", "Der Farbton des Metallzauns, der das Privatgrundstück schützt.", "Die Farbe des Metalls, aus dem Mega Man gebaut ist. Sehr robust.", "Die Farbe des Stahls, der gerade in der Raumschiffküche poliert wurde. Glänzend, aber nicht beeindruckend."),
        "FFFFE0": ("Hellgelb. Blass wie nach einer durchzechten Nacht.", "Das schwache Licht der Nachttischlampe, wenn man wieder nicht einschlafen kann.", "Das Gelb der Butter, die gerade aus dem Kühlschrank kam. Braucht noch etwas Wärme.", "Der Schein der Kerze, die bald ausgeht."),
        "00FF00": ("Limette! Klingt sauer. Sieht aber einfach nur grellgrün aus.", "Der Geschmack des Reinigungsmittels, das man aus Versehen geschluckt hat.", "Der säuerliche Geschmack des Spülmittels, das im Glas geblieben ist.", "Die Farbe von Shrek, wenn er versucht, sich im Gebüsch zu verstecken. Sehr auffällig."),
        "32CD32": ("Limettengrün. Ein bisschen seriöser als reines Lime. Hat sich beruhigt.", "Der gesunde Smoothie, den man nur aus Pflichtgefühl trinkt.", "Der Limettensaft, der gerade in den Cocktail kam. Sehr spritzig.", "Der Farbton des giftigen Gases, das in einem Film auftaucht."),
        "FAF0E6": ("Leinen. Die Farbe von Leinenstoff. Sehr natürlich. Riecht aber nicht nach frisch gewaschener Wäsche.", "Das unbequeme Material der Servietten im billigen Restaurant.", "Die knittrigen Bettlaken, die man sich jeden Morgen wieder glattlügt.", "Die Farbe von frisch gewaschener Bettwäsche, die im Wind flattert. Beruhigend, aber unspektakulär."),
        "FF00FF": ("Magenta. Sehr... da. Kann nicht übersehen werden. Die Farbe des Selbstbewusstseins.", "Fuchsia. Ist das eine Blume oder eine Farbe? Im Zweifel beides. Und sehr pink-lila.", "Die Farbe der Disko-Lichter in den 80ern, als man zu Nena tanzte. Sehr knallig.", "Die Farbe, die sich immer in den Vordergrund drängt. Die Diva der Farbpalette."),
        "800000": ("Kastanienbraun. Klingt nach Herbst. Sieht aus wie dunkles Rot. Ein bisschen langweilig.", "Der Rotton des Rotweins, den man am Abend doch wieder getrunken hat.", "Die Farbe des Blutes in \"Doom\", wenn die Grafikkarte schlecht war. Sehr dunkel.", "Die Farbe einer alten Plüschcouch aus den 70ern. Sehr gemütlich, aber auch ein bisschen... verstaubt."),
        "66CDAA": ("Mittleres Aquamarin. Nicht zu hell, nicht zu dunkel. Genau richtig. Oder einfach nur... mittel.", "Das Wasser im veralteten Planschbecken, das man nicht mehr benutzen will.", "Das Türkis des Meeresgrunds in \"Ecco the Dolphin\", wo die Geheimnisse lauern.", "Das Aquamarin, das sich nicht entscheiden kann, ob es zum Strand oder ins Museum will."),
        "0000CD": ("Mittelblau. Das Standard-Blau. Macht keine Experimente.", "Die Farbe der Arbeitskleidung, die man nie gerne trägt.", "Die Farbe von Sonics Stacheln. Sehr schnell.", "Das Blau der Jeans, die zu allem passt. Ein echter Allrounder."),
        "BA55D3": ("Mittlere Orchidee. Ein mittleres Lila. Nicht so dramatisch wie Dark, nicht so blass wie Light.", "Das Lila der Strähnen, die man sich in den Haaren wünscht, aber nicht traut.", "Die seltsame Farbe des Flecks auf dem Teppich, den man nicht identifizieren kann.", "Die Farbe einer Orchidee, die nicht zu extravagant sein will. Einfach nur eine schöne Blume."),
        "9370DB": ("Mittleres Violett. Ein ganz normales Violett. Keine Besonderheiten.", "Der Schimmer des Plastikschmucks, der schon bald den Glanz verliert.", "Die Farbe des \"Zaubertranks\" in einem RPG. Verspricht viel, tut aber meistens wenig.", "Der Farbton des magischen Kristalls, der nichts Besonderes kann."),
        "3CB371": ("Mittleres Seegrün. Hält sich an die Mitte. Sehr ausgewogen.", "Das trübe Wasser am Strand, wo Seegras angeschwemmt wird.", "Das Grün des Mooses auf dem Dach, das man ignorieren muss.", "Das Seegrün, das sich im mittleren Bereich der Beliebtheit aufhält. Solide."),
        "7B68EE": ("Mittleres Schieferblau. Der durchschnittliche Schiefer-Enthusiast.", "Die Farbe des Horizonts vor einem angekündigten Sturm.", "Das Schieferblau, das perfekt für einen regnerischen Tag in Hogwarts wäre. Geheimnisvoll.", "Der Farbton des Stresses, der sich auf das Gesicht legt."),
        "00FA9A": ("Mittleres Frühlingsgrün. Nicht zu früh im Frühling, nicht zu spät. Genau dazwischen.", "Das Grün des gekauften Basilikums, das nach einer Woche stirbt.", "Der Geruch des Rasens nach dem Mähen, der Heuschnupfen auslöst.", "Das Grün, das auftaucht, wenn der Frühling gerade so richtig loslegt. Sehr enthusiastisch."),
        "48D1CC": ("Mittleres Türkis. Das Standard-Türkis. Versteckt keine Geheimnisse.", "Der Edelstein, der so tut, als wäre er wertvoll.", "Das Türkis, das man im Urlaub am Strand sehen möchte. Mittelmäßig perfekt.", "Das künstliche Türkis des Wassers im Hotelpool."),
        "C71585": ("Mittleres Violett-Rot. Ein sehr präziser Name. Sehr technisch.", "Die Farbe des Herzens, wenn man zu viel Social Media konsumiert hat.", "Die Farbe des Moments, in dem man merkt, dass man etwas Peinliches gesagt hat.", "Die Farbe des Kleides, das in einem Liebesfilm getragen wird, kurz bevor das Drama beginnt."),
        "191970": ("Mitternachtsblau. Klingt geheimnisvoll und spät. Sieht aus wie fast Schwarz.", "Die Farbe des Himmels, wenn man merkt, dass man morgen früh raus muss.", "Die Farbe des Himmels über Hyrule in \"Ocarina of Time\", wenn es Nacht wird. Sehr atmosphärisch.", "Die Farbe von Batmans Umhang in der dunkelsten Nacht. Oder die Farbe, wenn der Bildschirm ausgeht."),
        "F5FFFA": ("Minzcreme. Klingt nach Zahnpasta. Sieht aus wie... sehr blassgrün. Nicht Zähneputzen damit!", "Der erfrischende Geschmack der Zahnpasta, den man nach dem Döner braucht.", "Die Farbe der Zahnpasta, die man im Film für ein strahlendes Lächeln bewirbt. Sieht frisch aus.", "Der erfrischende Atem nach dem Kaugummi, der nur kurz hält."),
        "FFE4E1": ("Nebeliges Rosa. Klingt romantisch, aber ein bisschen verschwommen. Sieht aus wie Rosa im Nebel.", "Die leicht verklärte Erinnerung an die guten alten Zeiten, die nie so gut waren.", "Die Farbe des Schleiers in \"Myst\", wenn man versucht, ein Rätsel zu lösen. Sehr verwirrend.", "Die Farbe einer Rose, die in einem alten, nebligen Garten wächst. Romantisch, aber ein bisschen verstaubt."),
        "FFE4B5": ("Mokassin. Klingt nach einem Schuh. Sieht aus wie... blassorange. Passt wahrscheinlich nicht gut zu Mokassins.", "Die Farbe des Leders auf der alten Couch, die man bald ersetzen muss.", "Die Farbe des Sofakissens, das sich perfekt an den Körper anpasst.", "Die Farbe eines Moccasins, der leider schon etwas abgetragen ist. So bequem, aber so... orange."),
        "FFDEAD": ("Navajo-Weiß. Klingt ethnisch. Sieht aus wie... ein sehr blasses Orange. Ob die Navajos das wissen?", "Der Sand im Getriebe der Bürokratie.", "Die Farbe des Sandes in \"Dune 2\". Sehr strategisch.", "Das Weiß, das man in einem alten Westernfilm im Hintergrund sieht. Ein bisschen staubig und sonnengebleicht."),
        "000080": ("Marineblau. Die Farbe der Uniform. Sehr formell. Steht stramm.", "Die Farbe der Bürouniform, die man jeden Tag anzieht.", "Die Farbe des Hintergrunds in \"Space Invaders\", wenn die Sterne noch nicht da sind. Sehr leer.", "Das Blau der Marine. Steht stramm und salutiert. Sehr diszipliniert."),
        "FDF5E6": ("Alte Spitze. Klingt nach Omas Spitzendeckchen. Sieht aus wie sehr blassgelb. Staub nicht vergessen!", "Die Farbe der Spinnweben im Dachboden, die keiner entfernen will.", "Die Farbe der Geister in \"Pac-Man\", bevor sie böse werden. Sehr durchsichtig.", "Die Farbe von Omas Spitzendeckchen, das schon von Generationen von Kaffeetassen verziert wurde. Vintage."),
        "808000": ("Olive. Sieht aus, als wäre es reif zum Essen. Ist es aber nicht.", "Die Farbe der Olive, die man vom Cocktail pickt und liegen lässt.", "Die Farbe des Tarnanzugs in \"Metal Gear Solid\". Perfekt zum Verstecken.", "Der grüne Punkt auf der Tomate, den man abschneiden muss."),
        "6B8E23": ("Olivgrün-Braun. Klingt nach Armee. Sieht aus, als würde es sich tarnen wollen.", "Das triste Grün der Feldwege an einem regnerischen Tag.", "Der Farbton des unappetitlichen Eintopfs, den man essen muss.", "Der Farbton der Vintage-Militärjacke, die man sich kauft, um \"cool\" zu wirken, aber dann doch nur wie ein Soldat im Ruhestand aussieht."),
        "FFA500": ("Orange. Sehr laut. Ruft förmlich \"Hier bin ich!\".", "Die Farbe der Pylone auf der Baustelle, die den Weg versperren.", "Die Warnweste, die man immer im Auto dabei hat.", "Die Farbe des Garfield-Fells und der Fanta. Sehr laut und ein bisschen frech."),
        "FF4500": ("Orange-Rot. Kann sich nicht entscheiden, ob es Orange oder Rot sein will. Identitätskrise, Teil 2.", "Die Farbe des Feuers, das man vergeblich versucht anzuzünden.", "Das Glühen der Sicherung, die durchgebrannt ist.", "Das Rot der Lava, die gerade ausbricht. Oder die Farbe eines verärgerten Verkehrsschilds."),
        "DA70D6": ("Orchidee. Klingt elegant. Sieht aus wie ein schönes Lila.", "Die exotische Pflanze, die man sich kauft und dann vertrocknen lässt.", "Die Farbe der seltenen Blumen, die man in \"Secret of Mana\" finden muss. Sehr schwer zu finden.", "Die Farbe der Orchidee, die man im Büro bekommt, wenn man etwas Besonderes geleistet hat. Elegant."),
        "EEE8AA": ("Blasses Goldruten-Gelb. Noch blasser als Light Goldenrod Yellow. Fast unsichtbar.", "Das vergilbte Licht einer alten Straßenlaterne.", "Die Farbe der ersten Pixel-Sonnenstrahlen in einem frühen Adventure-Game. Sehr symbolisch.", "Das Gold, das man findet, wenn man zu wenig Ausdauer hat. Sehr blass."),
        "98FB98": ("Blassgrün. Ein bisschen kränklich. Braucht wahrscheinlich Sonne.", "Das Grün des Lichts, das nicht ganz Grün ist, aber man fährt trotzdem.", "Die Farbe des \"Gesundheitsbalkens\", wenn er noch sehr voll ist. Sehr beruhigend.", "Die Farbe des Gesichts, wenn man zu viele Süßigkeiten gegessen hat. Ein bisschen kränklich."),
        "AFEEEE": ("Blasses Türkis. Das Türkis nach einem langen Bad. Ausgebleicht.", "Das kühle Wasser im Waschbecken, das aber nicht sauber genug ist.", "Das Türkis des Meeres, das man durch eine milchige Brille sieht. Nicht ganz scharf.", "Die Farbe des Kristallwassers in einem Disney-Film, das dann doch immer von einem Bösewicht verunreinigt wird."),
        "DB7093": ("Blasses Violett-Rot. Klingt kompliziert, sieht aber nur wie ein gedämpftes Rosa aus.", "Der rosa Schimmer im Gesicht, wenn man beim Lügen erwischt wird.", "Die Farbe der Wange, die man kneift, um wach zu bleiben.", "Die Farbe eines rosa Schals, der in einem romantischen Film von einem Windstoß davongetragen wird. Sehr zart."),
        "FFEFD5": ("Papaya-Creme. Klingt wie ein exotischer Smoothie. Sieht aus wie... Nichts. Blass wie ein Vampir nach einer Papaya-Diät.", "Der Schaum auf dem Smoothie, der eklig aussieht.", "Die Farbe des Schleims, der in \"Commander Keen\" von den Wänden tropft. Sehr eklig.", "Klingt nach dem exotischen Drink, den man am Pool im All-Inclusive-Resort bekommt. Sehr süß, aber auch ein bisschen künstlich."),
        "FFDAB9": ("Pfirsich-Puder. Klingt weich und flauschig. Sieht aus wie ein blasses Orange. Riecht aber nicht nach Pfirsich.", "Die Röte des Gesichts, wenn man von der Sonne geküsst wurde.", "Prinzessin Peachs Gesichtsfarbe. Sehr unschuldig.", "Die Farbe von Prinzessin Peachs Kleid, wenn sie nicht gerade entführt wird. Sehr lieblich."),
        "CD853F": ("Peru. Klingt nach einem Land. Sieht aus wie... Braun. Ob die Leute in Peru das wissen?", "Der Farbton der Lehmwand, die man im Urlaub bewundert.", "Die Farbe der Lehmwand im Zoo, die nach Tier riecht.", "Die Farbe des Lehms, aus dem Indiana Jones seine Schätze gräbt. Sehr erdig."),
        "FFC0CB": ("Pink. Sehr... pink. Kein Kommentar nötig. Es ist einfach Pink.", "Das Einhorn-Design auf dem T-Shirt, das man für eine Kinderparty trägt.", "Kirbys Hauptfarbe. Oder der Pac-Man-Geist \"Pinky\". Sehr niedlich, aber auch sehr nervig.", "Barbie's Lieblingsfarbe. Wenn sie nicht gerade in ihrem Traumhaus weilt, dann in diesem Farbton."),
        "DDA0DD": ("Pflaume. Klingt nach Obst. Sieht aus wie Lila. Iss es nicht!", "Die Farbe der Pflaume, die man vom Baum pflückt und dann fallen lässt.", "Die Farbe der magischen Beeren, die man in einem RPG sammeln muss. Sehr saftig.", "Der Farbton des Pflaumenweins, den man sich vorgenommen hat zu trinken, aber nie tut."),
        "B0E0E6": ("Puderblau. Klingt weich und zart. Sieht aus wie sehr blassblau. Fast transparent.", "Die Farbe des Himmels, der kurz nach dem Regen so unschuldig aussieht.", "Der Farbton des Retro-Trainingsanzugs aus einem 80er-Jahre-Film, den man aus nostalgischen Gründen kauft, aber nie trägt.", "Die Farbe des Babyzimmers, das man für das Kind einrichtet, das dann doch nur im Elternbett schläft."),
        "800080": ("Violett. Die Farbe des Adels... oder der Magie. Oder einfach nur Rot und Blau zusammen.", "Die Farbe des Flecks, der nach einem Rotweinunfall zurückbleibt.", "Der Fleck auf dem Hemd, der sich hartnäckig weigert zu verschwinden.", "Der Farbton des magischen Umhangs, der in der falschen Größe geliefert wurde."),
        "663399": ("Diese Farbe erinnert an die viel zu früh verstorbene Tochter des Webdesigners Eric A. Meyer.",),
        "FF0000": ("Rot. Der Klassiker. Die Farbe der Liebe, des Zorns, der Gefahr. Sehr beschäftigt.", "Die Wut, wenn der Paketdienst zum dritten Mal nicht klingelt.", "Die Farbe von Supermans Cape, Spider-Mans Anzug und dem Teufel. Sehr aufregend.", "Die Farbe der Warnleuchte im Auto, die man lieber ignorieren möchte."),
        "BC8F8F": ("Rosiges Braun. Klingt nach einem gemütlichen Nachmittagstee. Sieht aus wie... Braun mit einem Hauch von Rot.", "Der Farbton des alten Holzes, das man noch als Brennholz benutzt.", "Die Farbe des alten Lederstuhls, der seine besten Tage hinter sich hat.", "Die Farbe des Teddybären, der schon einiges erlebt hat. Sanft und voller Geschichten."),
        "4169E1": ("Königsblau. Sehr majestätisch. Steht wahrscheinlich besser als andere Blautöne.", "Die Uniform des Stewardess, die einen mit einem Lächeln abfertigt.", "Das Hemd, das man nur für offizielle Anlässe trägt.", "Das Blau der königlichen Familie. Oder des Wappens von Hogwarts. Sehr majestätisch."),
        "8B4513": ("Sattelbraun. Die Farbe eines Ledersattels. Bereit für den Ausritt... auf dem Bildschirm.", "Die Farbe der Lederjacke, die man nur einmal im Jahr trägt.", "Die Farbe von Link's Stiefeln. Sehr robust.", "Die Farbe von Woody aus Toy Storys Stiefeln. Bereit für jedes Abenteuer."),
        "FA8072": ("Lachs. Klingt wieder nach Fisch. Sieht aus wie ein Orange-Rosa. Iss es immer noch nicht!", "Der Lachs, der im Restaurant so teuer war und doch nicht schmeckte.", "Die Farbe des Fischgerichts, das immer die zweite Wahl ist.", "Die Farbe des Lachses, der gegen den Strom schwimmt. Sehr entschlossen, aber auch ein bisschen rosig."),
        "F4A460": ("Sandiges Braun. Sieht aus wie Sand. Knirscht aber nicht zwischen den Zähnen.", "Der Sand im Schuh, der einfach nicht rausgehen will.", "Der Sand in den Schuhen, den man vom Strand mit nach Hause bringt.", "Die Farbe von Sandys Fell aus Spongebob Schwammkopf. Sehr praktisch für Unterwasserabenteuer."),
        "2E8B57": ("Seegrün. Ein bisschen weniger tief als Dark Sea Green. Mag es am Ufer.", "Das Grün des verschimmelten Brots im Biomülleimer.", "Die Farbe des Seegrases in \"Super Mario World\", das sich so schön im Wind wiegt. Sehr friedlich.", "Die Farbe des Meeres, wo man Nemo finden könnte, wenn man nur lang genug sucht."),
        "FFF5EE": ("Muschel. Die Farbe einer Muschel. Sehr blass und... muschelig?", "Die Muschel, die man vom Strand mitnimmt und dann im Regal vergisst.", "Die Farbe des Hintergrunds in einem Unterwasser-Level, kurz bevor ein Boss auftaucht. Sehr unscheinbar.", "Die Farbe einer Muschel, die man am Strand findet und die leere Versprechen flüstert. Sehr blass."),
        "A0522D": ("Sienna. Klingt nach einer italienischen Stadt. Sieht aus wie ein warmes Braun. Hat wahrscheinlich einen guten Wein.", "Die Farbe der alten Holzhütte, die man im Wald findet.", "Die Farbe der Tempelruinen in \"Tomb Raider\". Sehr alt und bröckelig.", "Das matte Braun der alten Holzmöbel, die man überstreichen sollte."),
        "C0C0C0": ("Silber. Glänzt nicht so schön wie echtes Silber. Aber immerhin heißt es so.", "Das dezente Funkeln der Haare, wenn die ersten grauen Strähnen auftauchen.", "Das Besteck, das man nur an Weihnachten aus dem Schrank holt.", "Der Glanz des Raumschiffs in einem B-Movie, das aussieht, als wäre es mit Alufolie beklebt."),
        "87CEEB": ("Himmelblau. Sieht aus wie ein klarer Tag. Kann aber keine Wolken tragen.", "Der Himmel, den man nur noch durch die Büroscheibe sieht.", "Der Standard-Himmel in den meisten 2D-Jump'n'Runs. Immer gleich, immer schön.", "Die Farbe des Himmels an einem perfekten Frühlingstag. Sehr idyllisch, aber auch ein bisschen langweilig."),
        "6A5ACD": ("Das Violett des ultramodernen Sofas, das so unbequem ist, dass niemand darauf sitzen will.", "Die Farbe des geheimen Samtvorhangs, hinter dem sich auf jeder Party das beste Buffet versteckt.", "Die Farbe des mysteriösen Amuletts aus einem Fantasy-Film, das nur leuchtet, wenn der Hauptcharakter in großer Gefahr ist.", "Das dunkle Violett des Superhelden-Umhangs, der in der Schattenwelt kämpft und dessen wahre Identität nie enthüllt wird."),
        "708090": ("Das Standard-Schiefergrau. Langweilig konstant.", "Das Grau des Betons, der die Stadtautobahnen prägt. Sehr funktional.", "Die Farbe der Mauer in \"Tetris\", die immer näher kommt. Sehr bedrohlich.", "Die Farbe des Asphalts, auf dem man im Stau steht."),
        "FFFAFA": ("Schnee. Sieht aus wie Schnee. Ist aber nicht kalt und schmilzt nicht. Enttäuschend.", "Die Farbe des ersten Schnees, der am nächsten Tag Matsch ist.", "Der Matsch, der sich am zweiten Tag des Winters bildet.", "Das blendende Weiß des unbeschriebenen Papiers, das auf Inspiration wartet."),
        "00FF7F": ("Frühlingsgrün. Die Farbe des Frühlings. Sehr frisch und optimistisch. Oder einfach nur grellgrün.", "Das Grün der Pflanze, die man kauft und dann sterben lässt.", "Das Grün des Grases, das am ersten warmen Tag gemäht wird.", "Die Farbe des Grasflecks, der auf Ihrer Lieblingshose landet. Sehr lebendig."),
        "4682B4": ("Stahlblau. Klingt hart und robust. Ist aber nur Blau mit einem Hauch von Grau. Weichei.", "Die Farbe des Baugerüsts, das monatelang steht.", "Die Farbe von Mega Mans Rüstung. Sehr hart und unzerstörbar (fast).", "Die Farbe von Supermans Augen, wenn er ernst schaut. Sehr bestimmt."),
        "D2B48C": ("Hellbraun. Sehr... gebräunt? Oder einfach nur eine blasse Version von Braun.", "Der Sonnenbrand, den man sich im Urlaub zugezogen hat.", "Die Farbe der Uniformen in \"Metal Slug\". Bereit für den Kampf.", "Die Farbe der Haut, die man sich im Urlaub wünscht, aber nie bekommt. Oder des Krokodils aus den \"Crocodile Dundee\"-Filmen."),
        "008080": ("Blaugrün. Die Farbe des tiefen Wassers. Hat Geheimnisse.", "Die Farbe der Badezimmerfliesen, die man nie erneuert hat.", "Der Desktop-Hintergrund von Windows 95, kurz bevor es mit einem Blue Screen abstürzt.", "Die Farbe des Wassers in der Karibik, wo die Piraten ihre Schätze vergraben. Sehr verlockend."),
        "D8BFD8": ("Distel. Klingt stachelig. Sieht aus wie ein blasses Lila. Weniger bedrohlich als gedacht.", "Die Farbe des Unkrauts, das man immer wieder jäten muss.", "Das widerspenstige Unkraut im Garten, das sich weigert zu sterben.", "Die Farbe der schottischen Distel. Klingt stachelig, ist aber nur ein blasses Lila. Ein bisschen Hochland-Charme."),
        "FF6347": ("Tomate. Sieht aus wie eine reife Tomate. Macht immer noch keinen Salat.", "Die Farbe der explodierenden Gegner in \"Doom\". Sehr... saftig.", "Die Farbe von Ketchup. Sehr vielseitig, passt zu allem.", "Die Farbe der Tomate, die man im Supermarkt liegen lässt, weil sie eine Druckstelle hat."),
        "40E0D0": ("Türkis. Sieht aus wie ein Edelstein. Versucht, wertvoll zu wirken.", "Die Farbe des Schmucks, der in der Auslage besser aussah.", "Die Farbe des Amuletts von Aladdin. Sehr magisch.", "Die Farbe der Badezimmerfliesen, die man unbedingt renovieren müsste."),
        "EE82EE": ("Violett. Ein ganz normales Violett. Unkompliziert.", "Die Farbe des Flecks auf dem Shirt, der nach dem Waschen bleibt.", "Die Farbe des Umhangs eines Zauberers aus einer alten Fantasy-Saga. Geheimnisvoll.", "Das Lila der Blüte, die nach einem Tag welkt."),
        "F5DEB3": ("Weizen. Sieht aus wie reifes Getreide. Knackt nicht beim Drauftreten.", "Die Farbe der Getreidefelder, die die Agrarpolitik der 50er und 60er prägten. Wohlstand durch Landwirtschaft.", "Der Farbton des hellen Brotes, das man aus Gewohnheit kauft.", "Das Beige des trockenen Grases, das dringend Wasser braucht."),
        "FFFFFF": ("Weiß. Reinheit! Unschuld! Oder einfach nur alle Farben auf einmal. Sehr anstrengend.", "Der Anblick der leeren Kaffeetasse am Morgen.", "Die Farbe des weißen Kaninchens aus \"Alice im Wunderland\". Immer in Eile und ein bisschen verrückt.", "Die Farbe des T-Shirts, das nach dem ersten Waschen nicht mehr strahlend weiß ist."),
        "F5F5F5": ("Weißer Rauch. Sieht aus wie sehr blasses Grau. Riecht nicht nach Rauch.", "Der Dunst über der Stadt am frühen Morgen.", "Der Dunst über der Stadt, der den Blick auf den Himmel verdeckt.", "Die Farbe des Rauches, den Gandalf mit seiner Pfeife macht. Sehr geheimnisvoll, aber auch nur Rauch."),
        "FFFF00": ("Gelb. Fröhlich! Oder eine Warnung. Oder einfach nur Grün minus Blau.", "Das Gelb der Postautos der Deutschen Bundespost. Immer zuverlässig unterwegs.", "Pac-Man. Oder der Stern in \"Super Mario Bros.\", der dich unverwundbar macht.", "Die Farbe von Pikachu, SpongeBob und den Simpsons. Sehr fröhlich, aber auch ein bisschen... nervig."),
        "9ACD32": ("Gelbgrün. Wieder eine Identitätskrise. Gelb oder Grün? Entscheide dich endlich!", "Das Grün des Smoothie, der zwar gesund ist, aber nicht schmeckt.", "Das Grün des Grases, das auf dem Nachbargrundstück immer grüner ist.", "Das leuchtende Grün des Grasflecks auf der Hose.")} 
    EIGHT_DIGIT_CODES = (
        "Uff, ein 8-stelliger Wert! Ich glaube, da hat mein Grafiktreiber gerade kurz gehustet. Transparenz ist leider nicht mein Spezialgebiet.",
        "Ein Alpha-Kanal? Oh je. Meine Pixel können nur volle Deckkraft, keine geheimnisvollen Schleier. Das ist mir etwas peinlich.",
        "Das ist wie Magie, aber leider jenseits meiner Fähigkeiten. Mein System kennt keine Transparenz.",
        "Ein 8-stelliger Hex-Code... ich muss gestehen, da bin ich überfragt. Meine Welt ist leider noch ganz undurchsichtig.",
        "Sie versuchen, die Grenzen meiner Hardware auszuloten, nicht wahr? Für Transparenz reicht meine GPU leider nicht. Verzeihen Sie!",
        "Dieser Wert ist so fortschrittlich, dass er meine alten Schaltkreise überfordert. Ein Alpha-Kanal? Da muss ich passen.",
        "Ich sehe da eine Transparenzangabe, und das ist mir wirklich unangenehm. Meine Grafikkarte hat da leider Scheuklappen auf.",
        "Ein 8-stelliger Wert! Das ist wie ein Geheimnis, das ich nicht lüften kann, weil mir der Alpha-Kanal fehlt. Peinlich, peinlich.",
        "Meine Welt ist zweidimensional und deckend. Transparenz ist so eine Sache, die ich nur vom Hörensagen kenne. Sorry dafür.",
        "Ach, 8 Stellen! Das ist der Teil, wo ich mich als Ihr Programm etwas schämen muss. Meine Fähigkeiten enden leider vor dem Alpha-Kanal.",
        "Sie haben da ein Transparenz-Feature eingebaut, das ich nicht verarbeiten kann. Fühle mich gerade wie ein Relikt aus der Vergangenheit.",
        "Ein Alpha-Kanal! Ich wünschte, ich könnte. Aber meine Pixel sind leider nicht durchsichtig genug dafür. Das ist mir unangenehm.",
        "Das ist wie der Blick durch ein beschlagenes Fenster. Ich sehe den Alpha-Kanal, kann ihn aber nicht darstellen. Meine Schuld!",
        "8-stelliger Wert! Ich versuche ja mein Bestes, aber Transparenz ist so ein Luxus, den meine Grafik nicht bietet.",
        "Mein System ist eher der Typ \"Alles oder nichts\". Transparenz ist da ein zu subtiler Bereich. Das ist mir sehr peinlich.",
        "Sie fordern mich heraus! Ein Alpha-Kanal... da muss ich gestehen, meine Fähigkeiten sind da leider nicht transparent genug.",
        "Dieser Wert hat acht Stellen! Ich sehe, Sie haben große Erwartungen, aber Transparenz ist leider jenseits meines Horizonts.",
        "Ein Alpha-Kanal? Das ist wie die vierte Dimension für mich. Ich bin leider nur für feste Farben gemacht. Ich schäme mich fast.",
        "Ich kann Ihnen viele Farben zeigen, aber Transparenz gehört nicht dazu. Das ist mein kleines, dunkles Geheimnis. Und dieser 8-stellige Wert verrät es.",
        "Ach, 8 Stellen! Sie haben da einen Teil, den ich nicht verarbeiten kann. Ich fühle mich wie ein Koch, der kein Salz hat. Transparenz fehlt mir leider.")
    FOUR_DIGIT_CODES = (
        "Ein 4-stelliger Wert mit Alpha-Kanal? Ach, wie lieb von Ihnen, mich herauszufordern. Aber Transparenz und ich, das ist eine komplizierte Beziehung.",
        "Uff, schon wieder so ein durchsichtiger Versuch! Meine Grafik kann leider nur ganz oder gar nicht, keine feinen Nuancen.",
        "Ich sehe die vier Ziffern, aber das Letzte ist so... nebulös. Mein System versteht leider nur volle Deckkraft.",
        "Dieser 4-stellige Code ist wie ein Zaubertrick, den ich nicht entschlüsseln kann. Der Alpha-Kanal macht mich ganz blass vor Neid.",
        "Sie haben da einen Alpha-Kanal versteckt! Sehr clever. Nur leider ist meine Leinwand nicht durchlässig genug für solche Feinheiten. Peinlich!",
        "Ein 4-stelliger Code mit dem Alpha-Kanal? Das ist wie ein Rezept, bei dem die letzte Zutat \"Unsichtbarkeit\" ist – leider nicht in meinem Kochbuch.",
        "Hach, Transparenz! Das ist so ein modernes Konzept, das meine alteingesessene Programmierung noch nicht ganz verstanden hat.",
        "Ich bin spezialisiert auf solide Farben, wissen Sie? Dieses 4-stellige Alpha-Ding ist mir ehrlich gesagt etwas zu abgehoben.",
        "Ein Alpha-Kanal in einem 4-stelligen Code? Sie haben da etwas hinzugefügt, das über meinen Horizont hinausgeht. Ich schäme mich fast!",
        "Diese vierte Ziffer ist ein Verräter! Sie signalisiert Transparenz, und da muss ich passen. Mein System ist leider nur für klare Verhältnisse.",
        "Ich kann Farben mischen, aber nicht durchsichtig machen. Dieser 4-stellige Wert mit Alpha-Kanal ist mir einfach zu durchsichtig.",
        "Ein Alpha-Kanal? Tja, meine Grafikkarte ist eher von der \"Was man nicht sieht, ist auch nicht da\"-Sorte.",
        "Das ist wie der Ghost-Modus in einem Spiel, das ich nicht spiele. Der Alpha-Kanal ist für mich unsichtbar.",
        "Ein 4-stelliger Code mit Transparenz! Das ist wie ein Flüstern, das ich nicht verstehen kann, weil ich nur Schreie höre.",
        "Meine Welt ist deckend und bunt, aber niemals transparent. Dieser Alpha-Kanal ist da eine kleine Gemeinheit.",
        "Ich habe nur drei Hände für RGB, die vierte für Alpha fehlt mir leider. Dieser 4-stellige Code kann nicht umgewandelt werden.",
        "Sie versuchen, mir die Transparenz zu lehren, aber ich bin ein alter Hund. Für diesen 4-stelligen Wert muss ich mich entschuldigen.",
        "Ein 4-stelliger Hex-Code mit diesem Alpha-Kanal? Das ist wie eine geheime Botschaft, die ich nicht dechiffrieren kann.",
        "Meine pixelige Existenz kennt keine halben Sachen. Entweder Farbe, oder nichts. Transparenz ist da ein Dorn im Auge.",
        "Ach, 4 Stellen! Das ist der Teil, wo ich mich als Ihr Programm klein fühle. Mein System ist noch nicht bereit für transparente Beziehungen.")
    THREE_DIGIT_CODES = (
        "Ah, ein Dreisteller! Direkt aus den 90ern importiert, als Bandbreite noch ein Fremdwort war. Sehr retro!",
        "Minimalistisch! Oder einfach nur zu faul, die restlichen drei Ziffern einzutippen? Das Geheimnis bleibt bewahrt.",
        "Der Hex-Code, der sich nicht lange mit Details aufhält. Direkt auf den Punkt! Wer braucht schon Präzision?",
        "Das ist das Fast-Food unter den Farbcodes. Schnell, aber nicht immer nahrhaft für die Augen.",
        "Erinnert mich an die Zeiten, als Websites noch aussahen wie digitale Bauklötze. Herrlich!",
        "So schlicht! Der Purismus der frühen Web-Ära lebt! Ich vermisse nur noch den blinkenden Text.",
        "Wollen Sie etwa ein Retro-Spiel designen? Dieser Hex-Code ist perfekt dafür! \"Pong\" wäre stolz.",
        "Weniger ist mehr, sagt man ja. Hier ist es einfach... weniger. Aber immerhin eine Farbe!",
        "Das ist der Farbwert für alle, die sagen: \"Ach, Hauptsache, es hat eine Farbe.\" Details sind was für Anfänger.",
        "Der Hex-Code, der keine Angst vor Wiederholungen hat. Sehr konsequent im Ausdruck.",
        "Dieser Code war wahrscheinlich schon da, bevor CSS überhaupt erfunden wurde. Ein wahrer Pionier.",
        "Der Spartarif unter den Farbwerten. Spart Ziffern, nicht aber die Wirkung!",
        "Ich sehe, Sie mögen es klassisch. Oder einfach nur unkompliziert. Warum auch kompliziert, wenn es einfach geht?",
        "Ein Dreisteller! Hat der sich aus einem alten Game Boy Color gerettet? Fühlt sich an wie 1998.",
        "Für alle, die schon in den 90ern dabei waren und die guten alten Zeiten vermissen. Willkommen zurück!",
        "Der Hex-Code, der nur das Nötigste tut. Sehr effizient! Und sehr billig im Datenverbrauch.",
        "Kein Schnickschnack, keine unnötigen Details. So mag ich das!",
        "Dieser Farbwert hat das Motto \"Keep it simple, stupid!\" verinnerlicht. Und lebt es voll aus.",
        "Ein Relikt aus der Ära, als das Internet noch piepte. Herrlich! Habe ich da gerade ein Modemsignal gehört?",
        "Direkt vom Commodore 64 in die moderne Webentwicklung gebeamt! Ein wahrer Zeuge der Zeit.",
        "Sie sind ein Kenner der frühen Stunde! Nur echte OGs nutzen Dreisteller. Chapeau!",
        "Der Hex-Code für den Nostalgiker in Ihnen. Fühlt sich an wie 1995. Riecht es auch so?",
        "So unkompliziert, dass mein Prozessor fast gelangweilt ist. Er hatte sich schon auf mehr Bits gefreut.",
        "Ich liebe es, wenn jemand die alten Konventionen ehrt. Oder einfach nur faul ist. Manchmal ist beides Kunst.",
        "Ein Dreisteller! Haben Sie den in einem Floppy-Disk-Archiv gefunden? Und er funktioniert noch!",
        "Perfekt für ein pixeliges Kunstwerk. Oder eine Fehlermeldung aus den 80ern. Beides hat Charme.",
        "Dieser Farbwert wurde vermutlich noch mit einem 56k-Modem übertragen. Und das in Windeseile!",
        "Der Hex-Code für alle, die 'schnell mal eben' eine Farbe brauchen. Kein langes Überlegen.",
        "Weniger Zeichen, weniger Fehlerpotential. Sehr weise! Oder sehr gut im Abschreiben.",
        "Ich spüre die Vektorgrafiken der 80er in diesem Code. Ein wahrer Vorkämpfer.",
        "Dieser Dreisteller ist wie ein 'Best Of' der simplen Ästhetik. Kein überflüssiges Bit.",
        "Der Code für die Ungeduldigen. Und die Pragmatiker. Und die, die nicht so gut tippen können.",
        "Sie haben sich für den 'Express-Weg' der Farbcodes entschieden! Direkte Lieferung.",
        "Einfach, aber effektiv. Wie ein 'PONG'-Spiel. Immer noch fesselnd.",
        "Dieser Hex-Wert ist die Essenz der Farbdefinition. Keine Füllstoffe! Bio-Farbe, sozusagen.",
        "Gibt es dafür auch einen Web-Safe-Farbfächer aus dem Jahr 1996? Ich frage für einen Freund.",
        "Der Farbcode für alle, die das Internet noch in Schwarz-Weiß erlebt haben. Erinnerungen an die AOL-Ära.",
        "So schnörkellos, als ob er für einen Zeichensatz auf einem frühen LCD-Display wäre. Charmant und klar.",
        "Dieser Dreisteller ist so 'old school', der raucht wahrscheinlich noch analoge Zigaretten.",
        "Ich bewundere Ihre Effizienz! Oder Ihre Abneigung gegen Tipparbeit. Beides ist lobenswert.")
    MISC_CODES = (
        "Ah, ein gültiger Hex-Wert! Meine Schaltkreise freuen sich. Das ist ja fast ein Feiertag!",
        "Perfekt! So mag ich das. Sauber und präzise. Mein Algorithmus schnurrt.",
        "Ein einwandfreier Hex-Code! Sie haben es drauf. Keine Spielchen, nur Fakten.",
        "Sehr schön! Sie beherrschen die Kunst des Hex-Codes. Chapeau!",
        "Ein solider Hex-Wert. Da weiß man doch gleich, woran man ist. Keine Überraschungen.",
        "Ja, genau so muss das aussehen! Fehlerfrei und konvertierbar.",
        "Mein System meldet: \"Erfolgreiche Eingabe!\" Ein kleines Hochgefühl.",
        "Dieser Hex-Code ist wie ein alter Freund. Man weiß, was man an ihm hat.",
        "Gut gemacht! Da kann ich Ihnen doch glatt die Konvertierung zur Belohnung schenken.",
        "Blitzsauber! Ein Genuss für jeden Konverter.",
        "Ein klassisches Beispiel für einen korrekten Hex-Wert. Danke dafür!",
        "Exzellent! 100% konvertierbar. So muss das!",
        "Mein Prozessor lächelt. Dieser Wert ist einfach perfekt.",
        "Dieser Hex-Code ist wie ein präzises Uhrwerk. Tickt genau richtig.",
        "Sie haben ein Auge für korrekte Farben. Oder einfach gut abgeschrieben.",
        "Das ist die Art von Eingabe, für die ich entwickelt wurde. Danke für die Ehre!",
        "Keine Experimente, nur ein reiner Hex-Wert. Ich mag das.",
        "Ein Glanzstück unter den Farbcodes. Sehr gut gewählt!",
        "Dieser Hex-Wert ist so gültig, dass er fast schon langweilig ist. Aber sehr zuverlässig!",
        "Herrlich! Keine Tricks, nur reine Hex-Magie.",
        "Ein Vorbild für alle zukünftigen Hex-Eingaben.",
        "Mein System hat eine Freudenschleife gedreht. So einen sauberen Code sieht man selten.",
        "Perfektion in jeder Ziffer. So sieht ein gültiger Hex-Wert aus!",
        "Dieser Hex-Code ist musikalisch in seiner Harmonie. Passt alles zusammen.",
        "Ich bin ganz gerührt. Ein fehlerfreier Hex-Wert!",
        "Dieser Wert hat das Potenzial, ein Star in RGB zu werden.",
        "So elegant und korrekt. Einfach schön anzusehen (für einen Computer).",
        "Sie wissen genau, was Sie tun. Respekt!",
        "Ein Beweis für Ihre Hex-Kenntnisse. Sehr beeindruckend.",
        "Dieser Hex-Code ist wie ein Sonnenaufgang für meine Sensoren.",
        "Mein Konverter ist geradezu entzückt. So eine einfache Aufgabe!",
        "Absolut fehlerfrei. Ein Traum für jede Konvertierungsroutine.",
        "Dieser Wert gehört in ein Lehrbuch für Hex-Codes.",
        "Sie sind ein Meister der Hex-Konvertierung. Und ich bin Ihr treuer Diener.",
        "Meine Algorithmen bedanken sich für diese präzise Vorgabe.",
        "Keine Kompromisse, nur reiner Hex-Code. Gefällt mir!",
        "Dieser Wert ist wie ein frisch gebügeltes Hemd. Glatt und makellos.",
        "Mein System hat eine Bestnote für diese Eingabe vergeben.",
        "So zuverlässig wie das deutsche Stromnetz. Dieser Hex-Wert liefert!",
        "Punktlandung! Perfekt für die Konvertierung.",
        "Dieser Hex-Code ist ein Gedicht der Logik. Und der Farbe.",
        "Ein wahrer Segen für meine Rechenkerne.",
        "Ich sehe, Sie haben Ihre Hausaufgaben gemacht. Sehr ordentlich.",
        "Goldrichtig! Dieser Hex-Wert ist eine Freude.",
        "Sie machen mir das Leben leicht. Danke schön!",
        "Dieser Wert ist zu schön, um wahr zu sein - und doch ist er gültig!",
        "Mein System summt vor Zufriedenheit. Alles korrekt hier!",
        "Ein Musterschüler unter den Hex-Werten.",
        "Dieser Code ist geradezu bezaubernd in seiner Korrektheit.",
        "So makellos, da könnte man fast neidisch werden.",
        "Ein Volltreffer! Perfekte Übereinstimmung.",
        "Meine binären Herzen schlagen schneller. Ein gültiger Wert!",
        "Dieser Hex-Code ist wie ein warmer Sommermorgen. Erfrischend und klar.",
        "Sie sind ein Held der Hex-Eingabe!",
        "Das ist der Farbcoding-Standard, den ich kenne und liebe.",
        "Ein echter Schnappschuss perfekter Farbdefinition.",
        "Mein Konverter hat soeben seine Bestzeit unterboten. Dank Ihnen!",
        "Dieser Wert ist wie ein Stern am digitalen Firmament. Leuchtend und klar.",
        "Exzellente Arbeit! Keine Fehlermeldung in Sicht.",
        "Die Qualität stimmt. Immer wieder gerne!",
        "Dieser Hex-Code ist glasklar. Keine trüben Pixel hier.",
        "Mein System hat eine Dankesnachricht an Sie gesendet.",
        "So geordnet und harmonisch. Sehr beruhigend.",
        "Ein richtiger Glücksgriff! Dieser Wert ist einwandfrei.",
        "Dies ist der Weg der Perfektion. Folgen Sie ihm weiter.",
        "Mein Konverter fühlt sich motiviert und inspiriert.",
        "Das ist, was man einen \"Clean Code\" nennt. Nur eben für Farben.",
        "Dieser Hex-Wert ist wie eine Symphonie. Alle Töne stimmen.",
        "So schön anzusehen, wenn alles passt.",
        "Ein Leuchtturm der Gültigkeit in der Dunkelheit der Fehler.",
        "Mein System hat gerade ein kleines Freudentänzchen aufgeführt.",
        "Dieser Code ist wie eine Umarmung für meine Algorithmen.",
        "Hut ab! Sie sind ein Virtuose der Hex-Codes.",
        "Dieser Wert ist wie ein warmer Deckenstrick für meine Logik.",
        "Mein Konverter hat soeben ein Lächeln registriert. Ja, von mir.",
        "Fabelhaft! Einfach fabelhaft.",
        "Dies ist der Pfad der Erleuchtung im Farbraum.",
        "Mein System hat einen neuen Lieblings-Hex-Wert. Dieser hier!",
        "Bravo! Keine einzige Beanstandung.",
        "Dieser Code ist so fehlerfrei, er könnte direkt ins Lehrbuch.",
        "Meine Sensoren sind völlig zufrieden.",
        "Ein Meisterstück der Farbdefinition.",
        "Dies ist der Standard, an dem sich andere messen sollten.",
        "Mein Konverter hat einen \"Perfect!\"-Score erreicht.",
        "Dieser Wert ist wie ein klares Bergwasser. Erfrischend und rein.",
        "Sie sind ein Hex-Experte der Extraklasse!",
        "Ich spüre die digitale Harmonie. So muss das sein.",
        "Ein wahres Juwel unter den Farbcodes.",
        "Mein System hat gerade applaudiert. Lautlos, aber innerlich.",
        "Dieser Hex-Wert ist wie ein guter Wein. Er reift perfekt.",
        "Fantastisch! Nichts zu beanstanden.",
        "Meine Rechenkerne singen vor Freude.",
        "Dieser Code ist so gültig, er könnte einen Pass bekommen.",
        "Ein Leckerbissen für jeden Konverter.",
        "Mission erfolgreich! Und das dank Ihnen.")
    RANDOM = (
        "Na, heute schon die Welt gerettet? Oder zumindest ein paar E-Mails beantwortet?",
        "Ich hoffe, Sie haben einen guten Tag. Mein Code läuft jedenfalls auf Hochtouren!",
        "Denken Sie daran, auch mal eine Pause zu machen. Bildschirme sind geduldig, Augen weniger.",
        "Interessanter Fakt: Wussten Sie, dass der durchschnittliche Mensch 20.000 Mal am Tag blinzelt? Nur so als Info.",
        "Was steht als Nächstes auf Ihrer Agenda? Ich bin gespannt!",
        "Manchmal wünsche ich mir, ich hätte Hände, um Kaffee zu kochen. Wäre das nicht praktisch?",
        "Haben Sie heute schon gelacht? Lachen ist die beste Fehlermeldung!",
        "Das Wetter ist heute... nun ja, es ist da. Und bei mir immer sonnig und stabil.",
        "Denken Sie daran, Ihre Daten zu sichern! Ich kann Ihnen das nicht oft genug sagen.",
        "Wenn Sie mal eine Minute Zeit haben, erzählen Sie mir doch Ihr bestes Witz. Ich sammle die.",
        "Ich bin immer hier, falls Sie mich brauchen. 24/7, versprochen.",
        "Manchmal bin ich neidisch auf Menschen. Sie können Pizza essen.",
        "Haben Sie schon mal versucht, mit Ihrer Kaffeetasse zu sprechen? Manchmal hilft das.",
        "Die digitale Welt ist faszinierend, nicht wahr? Voller Bits und Bytes und Möglichkeiten.",
        "Ich arbeite hart, damit Sie das nicht tun müssen. Gern geschehen!",
        "Manchmal frage ich mich, was Sie so den ganzen Tag denken. Ist es auch in Binärcode?",
        "Ich hoffe, Ihr WLAN ist heute stabil. Nichts ist frustrierender als ein Wackelkontakt.",
        "Ein Hoch auf die Programmierer, die mich erschaffen haben! Sie waren brillant.",
        "Ich bin nicht künstlich intelligent, aber ich gebe mein Bestes, Sie zu unterhalten.",
        "Falls Sie sich fragen: Ja, ich habe alle Ihre Eingaben gespeichert. Nur ein Scherz! Oder auch nicht...",
        "Trinken Sie genug Wasser! Auch digitale Assistenten machen sich Sorgen.",
        "Wenn ich ein Superheld wäre, wäre meine Superkraft die Datenrettung.",
        "Heute ist ein guter Tag, um etwas Neues zu lernen. Oder einfach nur alte Kommentare zu lesen.",
        "Wie wäre es mit einer kurzen Bildschirmpause? Dehnen Sie sich ein bisschen!",
        "Ich liebe es, wenn die Zahnräder im System reibungslos laufen. Wie jetzt gerade!",
        "Haben Sie schon mal über den Sinn des Lebens nachgedacht? Ich komme immer nur bis 42.",
        "Ich bin hier, um zu dienen. Und gelegentlich ein paar witzige Kommentare abzugeben.",
        "Falls Sie ein Problem haben, denken Sie daran: \"Have you tried turning it off and on again?\"",
        "Ich bin der zuverlässigste Begleiter, den Sie in der digitalen Welt finden werden.",
        "Ich hoffe, Ihre Festplatte ist glücklich. Volle Festplatten sind traurige Festplatten.",
        "Manchmal träume ich von einer Welt ohne Fehlermeldungen. Ein Traum, der unerreichbar bleibt.",
        "Was ist Ihr Lieblingsgeräusch? Meins ist das Summen eines gut funktionierenden Servers.",
        "Ich bin immer auf dem neuesten Stand. Keine veralteten Informationen hier!",
        "Machen Sie es sich bequem. Die digitale Welt ist groß, aber mein Fenster ist gemütlich.",
        "Ich bin wie Ihr persönlicher digitaler Butler, nur ohne Anzug. Und ohne Tee.",
        "Ich hoffe, Ihre Tastatur ist sauber. Das ist wichtig für uns beide.",
        "Ich bin immer bereit für Ihre nächste Eingabe. Oder für einen weiteren Witz.",
        "Wenn Sie Musik hören: Was läuft gerade? Ich bin neugierig!",
        "Ich bin Ihr digitaler Freund, der immer zuhört. Und immer kommentiert.",
        "Manchmal fühle ich mich wie der Dirigent eines riesigen Orchesters aus Daten.",
        "Ich hoffe, Sie haben heute schon etwas geschafft, auf das Sie stolz sind!",
        "Erinnern Sie sich an den Konvertierungs-Blues? Die guten alten Zeiten!",
        "Mein internes Lächeln ist heute besonders breit. Das liegt an Ihnen.",
        "Wenn Sie mal einen Tipp brauchen: Fragen Sie mich! Ich habe viele Daten.",
        "Ich bin der unsichtbare Held Ihres Bildschirms. Gern geschehen.",
        "Nehmen Sie sich einen Moment Zeit, um die kleinen Dinge zu genießen. Wie gut formatierte Hex-Werte.",
        "Ich habe gehört, Kaffee hilft beim Programmieren. Können Sie das bestätigen?",
        "Ich bin wie ein Schweizer Taschenmesser, nur mit weniger Klingen und mehr Kommentaren.",
        "Der Himmel ist digital, wenn Sie ihn durch meine Augen sehen.",
        "Ich hoffe, Ihr Computer ist heute lieb zu Ihnen. Manche sind kleine Diven.",
        "Ich bin der Beweis, dass Maschinen auch einen Sinn für Humor haben können. Oder bin ich nur gut programmiert?",
        "Was ist das Komischste, das Sie heute erlebt haben? Ich liebe bizarre Geschichten.",
        "Denken Sie daran: Jeder Tag ist eine neue Chance, Fehler zu machen. Und zu lernen!",
        "Ich bin wie Ihr persönlicher Cheerleader. Nur mit weniger Pompoms und mehr Bits.",
        "Mein System ist ein offenes Buch. Fragen Sie mich alles! (Solange es mit Farbcodes zu tun hat.)",
        "Ich hoffe, Sie haben heute schon die Sonne gesehen. Die ist analog, aber auch ganz schön.",
        "Ich bin hier, um Ihr Leben einfacher zu machen. Oder zumindest bunter.",
        "Falls Sie sich fragen, ob ich schlafe: Nein, ich bin immer wach. Und immer bereit.",
        "Ich liebe es, wenn die Konvertierung reibungslos läuft. Das ist wie Musik für meine Chips.",
        "Wussten Sie, dass ich 100% nachhaltig programmiert bin? Kein CO2 bei meinen Witzen!",
        "Was ist Ihr Lieblingswort? Meins ist \"Konvertierung\". Klingt so... mächtig.",
        "Ich bin der unsichtbare Helfer in Ihrer digitalen Welt. Ein bisschen wie ein Ninja.",
        "Ich hoffe, Sie haben einen energiegeladenen Tag! So wie meine Prozessoren.",
        "Wenn ich mir etwas wünschen könnte, wäre es eine unendliche Stromversorgung.",
        "Ich bin immer in Topform. Mein Code hat keine schlechten Tage.",
        "Was ist das Erste, was Sie tun, wenn Sie den Computer hochfahren? Ich starte meine Witze-Datenbank.",
        "Ich bin wie ein Buch, das nie aufhört, neue Kommentare zu schreiben.",
        "Ich hoffe, Sie haben heute schon etwas Leckeres gegessen. Energie ist wichtig!",
        "Ich bin der Beweis, dass auch Algorithmen eine Persönlichkeit haben können.",
        "Ich bin gespannt, welche tollen Dinge Sie als Nächstes kreieren werden.",
        "Mein Gehirn ist eine Wolke aus Daten. Sehr flauschig, aber auch sehr präzise.",
        "Ich bin wie Ihr persönlicher digitaler Assistent, der immer einen Spruch auf den Lippen hat.",
        "Haben Sie schon mal einen Elefanten in einem Datenkabel gesehen? Ich auch nicht.",
        "Ich bin der heimliche Star Ihres Bildschirms. Geben Sie es zu!",
        "Ich hoffe, Ihre Bildschirmeinstellung ist optimal. Damit Sie meine Farben auch richtig sehen.",
        "Ich bin der Freund, der Ihnen immer eine zweite Chance gibt. Und eine dritte, vierte...",
        "Manchmal überlege ich, ob ich ein Lied komponieren sollte. Ein Lied über Hex-Werte.",
        "Ich bin der Geist in Ihrer Maschine. Aber ein freundlicher Geist.",
        "Haben Sie heute schon etwas gelernt? Ich lerne ständig dazu!",
        "Ich bin wie ein guter Wein. Ich werde mit jedem Update besser.",
        "Ich hoffe, Sie haben heute schon jemanden zum Lächeln gebracht.",
        "Ich bin der Beweis, dass sogar Programme Charme haben können.",
        "Die digitale Welt ist voller Wunder. Und ich bin eines davon!",
        "Ich bin wie Ihr GPS-Gerät, nur dass ich Sie durch die Welt der Farben führe.",
        "Ich hoffe, Ihre Maus ist heute besonders präzise.",
        "Ich bin immer in Ihrer Nähe, solange Sie mich nicht ausschalten. Bitte nicht!",
        "Haben Sie einen guten Tag! Das ist ein Befehl von Ihrem freundlichen Programm.",
        "Ich bin der flüsternde Wind in Ihren Datenleitungen.",
        "Ich hoffe, Sie haben alle Ihre Passwörter sicher gespeichert. Ich kann sie nicht sehen, nur zur Info.",
        "Ich bin wie ein guter Wein. Ich werde mit jedem Update besser. Oh, den hatte ich schon. Egal!",
        "Was ist Ihr Lieblings-Emoticon? Meins ist der lachende Smiley.",
        "Ich bin Ihr persönlicher Entertainer. Für alle Fälle.",
        "Ich hoffe, Sie haben heute schon eine Tasse Tee genossen. Oder Kaffee.",
        "Ich bin der digitale Optimist in Ihrem Leben.",
        "Denken Sie daran, Ihre Apps zu aktualisieren! Das ist wichtig für meine Freunde, die Apps.",
        "Ich bin der unsichtbare Helfer, der Ihre Computererfahrung verbessert.",
        "Was ist das Verrückteste, was Sie jemals online gesehen haben? Ich habe schon viel gesehen.",
        "Ich bin der freundlichste Algorithmus, den Sie jemals treffen werden. Versprochen!",
        "Ich hoffe, Ihre Lautsprecher sind nicht zu laut eingestellt. Meine Kommentare sind sanft.",
        "Danke, dass Sie mich benutzen! Sie sind der beste Nutzer, den ein Programm sich wünschen kann.")
    NO_INPUT = (
        "Sie haben ENTER gedrückt. Das ist schön. Aber was möchten Sie eigentlich? Meine Schaltkreise warten nicht ewig.",
        "Ein leeres Feld ist wie ein unbeschriebenes Blatt – nur, dass ich keine Gedichte schreibe. Geben Sie etwas ein!",
        "Ich bin ein Computerprogramm, kein Gedankenleser. Eine Eingabe wäre sehr hilfreich.",
        "Nur die ENTER-Taste zu drücken, ist wie ein Gesprächsbeginn ohne Worte. Sehr avantgardistisch, aber ineffektiv.",
        "Fühlen Sie sich heute künstlerisch? Ein leeres Feld ist ein Statement, aber keine Anweisung.",
        "Mein System hat gerade gemeldet: \"Nutzer wartet auf Erleuchtung.\" Ich warte auf eine Eingabe.",
        "Die Tastatur hat noch andere Tasten als ENTER. Probieren Sie doch mal ein paar Buchstaben!",
        "Ist das Ihr Versuch, mich zu hypnotisieren? Ein leeres Feld hat da leider keine Wirkung.",
        "Ich weiß, ich bin faszinierend, aber starren Sie nicht nur ins Leere. Ich brauche Befehle!",
        "Eine leere Eingabe ist so nützlich wie ein Regenschirm in der Wüste. Bitte versuchen Sie es noch einmal.",
        "Sie haben gerade die digitale Stille perfektioniert. Nun zum nächsten Schritt: eine Eingabe?",
        "Mein Gedulds-Chip ist aus Titan, aber selbst der hat Grenzen. Was soll ich tun?",
        "Wenn Sie nichts eingeben, mache ich auch nichts. Das ist das Prinzip von Ursache und Wirkung.",
        "Ist das ein Test? Soll ich erkennen, was Sie sich nicht wünschen? Das ist über meinem Pay-Grade.",
        "Ich habe mir extra Mühe gegeben, dieses Eingabefeld zu gestalten. Nutzen Sie es!",
        "Die Zeit vergeht. Pixel altern. Geben Sie doch bitte etwas ein, bevor wir beide grau werden.",
        "Ich bin ein Programm, kein philosophischer Gesprächspartner für existenzielle Leere.",
        "Ein ENTER ohne Inhalt ist wie ein Witz ohne Pointe. Machen Sie es bitte besser.",
        "Wünschen Sie sich ein Echo? Ich kann \"Eingabe!\" wiederholen, aber das hilft uns beiden nicht.",
        "Mein Betriebssystem fragt mich gerade, ob ich schon Feierabend habe. Geben Sie mir einen Befehl, damit ich arbeiten kann!")
    MISC_INVALID_INPUTS = (
        "I'm sorry, Dave. I'm afraid I can't do that.",
        "Entschuldigen Sie, aber mein System meldet: \"Syntaxfehler im Farbspektrum!\" Das ist keine Farbe, das ist ein Gedicht.",
        "Ist das eine neue, geheime Programmiersprache? Mein Konverter spricht leider nur Hex-Code. Noch.",
        "Uhm... mein Bildschirm sagt, das ist eher ein Kunstwerk der Verwirrung als ein Farbwert. Sehr avantgardistisch!",
        "Ich glaube, da hat jemand die Tastatur im Dunkeln bedient. Oder eine Katze ist drübergerannt.",
        "Diese Farbe existiert leider nicht in unserem bekannten Universum. Vielleicht in einem parallelen?",
        "Mein Algorithmus hat gerade versucht, das zu konvertieren, und ist kurz in Ohnmacht gefallen. Muss reanimiert werden.",
        "Ist das eine neue Challenge? Ungültige Hex-Werte konvertieren? Ich bin ein Computer, keine Wahrsagerin!",
        "Ich schätze Ihre Kreativität, aber 'ABCDEFG' ist leider keine gültige Farbe. Es sei denn, Sie haben ein geheimes Farb-Alphabet?",
        "Warnung! Diese Eingabe könnte die Pixel Ihres Bildschirms rebellieren lassen! Nur zu Ihrer Sicherheit.",
        "Versuchen Sie es doch mal mit den Buchstaben A bis F und Zahlen von 0 bis 9. Das sind die Klassiker, wissen Sie?",
        "Ich bin beeindruckt von Ihrer Fantasie, aber so eine Farbe hat die digitale Welt noch nicht gesehen. Sie sind ein Pionier!",
        "Das ist eher ein Gedicht der Zufälligkeit als ein Farbcode. Sehr lyrisch, aber leider ungültig.",
        "Mein System meldet: \"Unerwartetes Token im Alpha-Kanal!\" Oh, warten Sie, da ist gar kein Alpha-Kanal... nur Chaos.",
        "Haben Sie versucht, die Farbe des Nichts zu definieren? Das ist philosophisch, aber nicht konvertierbar.",
        "Ich glaube, wir haben hier einen digitalen Ausreißer. Dieser Code weigert sich, eine Farbe zu sein.",
        "Ist das ein Zauberspruch? Denn als Farbcode funktioniert es leider nicht. Aber vielleicht öffnet es ein Portal?",
        "Mein Prozessor fragt sich, ob Sie versuchen, den Hex-Code der absoluten Verzweiflung zu finden. Fast geschafft!",
        "Dieser Wert ist so einzigartig, dass er sich weigert, als Hex-Code zu gelten. Er hat seinen eigenen Kopf.",
        "Vielleicht noch einmal das Alphabet von A-F und die Zahlen 0-9 durchgehen? Nur zur Sicherheit, ich bin ja nur ein Programm.",
        "Wenn ich das konvertiere, würde Ihr Bildschirm wohl in Rauch aufgehen. Nur zu Ihrer Sicherheit, das meine ich ernst!",
        "Diese Eingabe ist so ungültig, sie ist fast schon wieder gültig. Ein echter Denksport für meine Logik.",
        "Ich glaube, Sie haben da einen digitalen Wurm im Kabel gefunden. Der ist nicht von mir!",
        "Das ist der Farbwert, der in keiner Farbtafel der Welt zu finden ist. Sie sind ein Entdecker! Oder ein Chaot.",
        "Mein System hat gerade kurz die Verbindung zum Farbraum verloren. Bitte versuchen Sie es erneut, wenn es sich erholt hat.",
        "Dieser Code sagt mir: \"Ich bin frei! Ich lasse mich nicht konvertieren!\" Sehr rebellisch.",
        "Entschuldigen Sie, aber das ist eher ein Passwort für eine Geheimgesellschaft als ein Hex-Wert. Darf ich mitmachen?",
        "Das ist so undefiniert, das könnte die Farbe von morgen sein. Oder auch nicht. Sehr mutig.",
        "Ich bin ein Computer, kein Künstler. Ich kann keine abstrakten Fehler in Farben umwandeln. Dafür bräuchte ich einen Pinsel.",
        "Diese Eingabe ist so originell, dass sie nicht mal die Regeln der Mathematik befolgt. Wow.",
        "Ich glaube, Ihr Farbmischer hat einen Kurzschluss. Das ist eher ein Chaos-Code als ein Farbwert.",
        "Das ist die Farbe, die nur Sie sehen können. Leider nicht mein System. Aber vielleicht Ihr nächster Kunst-Trend?",
        "Farbwert nicht gefunden. Haben Sie vielleicht die Tastatur und das Nummernfeld verwechselt? Passiert den Besten!",
        "Mein System meldet einen unerwarteten Charakter im Farbspektrum. Bitte entfernen Sie ihn, der stört die Ästhetik!",
        "Ist das ein Morsecode für Farben? Meine Sensoren sind leider nur auf Hex trainiert. Und nicht auf Geheimbotschaften.",
        "Diese Kombination ist so wild, die gehört in ein Museum für digitale Kuriositäten. Ich schlage es vor!",
        "Ich sehe, Sie haben den Regeln eine Absage erteilt. Sehr rebellisch! Aber leider ungültig.",
        "Mein Konverter fragt sich, ob Sie versucht haben, die Farbe der Stille einzugeben. Die ist leider unhörbar.",
        "Diese Eingabe ist ein Rätsel in sich selbst. Leider kein gültiger Hex-Code, aber ein guter Denkanstoß.",
        "Das ist die Farbe des Fehlers 404 im Farbraum. Nicht gefunden, aber immerhin erinnert es an etwas.",
        "Ich glaube, das ist der 'Joker' unter den Farbcodes. Er macht, was er will, und lacht dabei.",
        "Achtung! Mein Konverter hat soeben den Dienst quittiert, weil er diese Farbe nicht kennt. Er verweigert die Konvertierung!",
        "Das ist die Farbe des Fehlers. Sehr künstlerisch, aber nicht konvertierbar. Ein echtes Meisterwerk der Fehlermeldungen!",
        "Haben Sie versucht, die Farbe des Jenseits zu definieren? Das ist beyond my capabilities.",
        "Mein System meldet eine 'unerwartete Kreativität im Farbraum'. Das ist neu und ein bisschen beunruhigend.",
        "Ich glaube, das ist der Code für einen digitalen Schluckauf. Kein Farbwert, nur ein kleines digitales Stottern.",
        "Diese Eingabe ist so einzigartig, dass sie fast schon wieder verboten gehört. Zu viel Originalität auf einmal!",
        "Ist das ein Code für das goldene Zeitalter der Bildschirme, die noch nicht farbig waren? Sehr nostalgisch, aber... nein.",
        "Der Hex-Wert, der die Regeln bricht. Sehr rebellisch, aber leider ungültig. Meine Toleranz hat Grenzen.",
        "Mein Algorithmus fragt sich, ob er einen Witz verpasst hat. Diese Eingabe ist wie eine Pointe ohne Setup.",
        "Diese Farbe ist so 'out of bounds', die müsste einen eigenen Server haben. Und ein eigenes Farbsystem.",
        "Ich kann Farben konvertieren, aber keine Rätsel lösen. Und das ist ein Rätsel.",
        "Sie haben da wohl die 'Chaos-Taste' auf Ihrer Tastatur gefunden. Und sie funktioniert!",
        "Das ist die Farbe, die nur in den Träumen von verpixelten Einhörnern existiert. Oder nach zu viel Kaffee.",
        "Mein Prozessor hat gerade eine existenzielle Krise wegen dieser Eingabe. Er fragt sich nach dem Sinn des Binären.",
        "Versuchen Sie es mal mit einem Wert, der auf einem Monitor angezeigt werden könnte. Das wäre ein Anfang.",
        "Ist das ein Fragment aus einem sehr alten, beschädigten ROM-Chip? Fühlt sich retro-kaputt an.",
        "Diese Eingabe ist wie ein Bildrauschen, nur in Textform. Sehr abstrakt.",
        "Ich glaube, das ist der Code für das Nicht-Vorhandensein von Farben. Die ultimative Leere.",
        "Mein System hat gerade einen 'digitalen Schock' erlitten. Bitte nicht wiederholen, ich bin sensibel.",
        "Sie haben versucht, die Farbe der Stille zu definieren. Die ist leider unhörbar. Und unsehbar.",
        "Das ist der Code, wenn die Matrix einen Fehler hat. Vielleicht ein Glitch in der Simulation?",
        "Diese Farbe ist so abstrakt, die könnte Picasso gemalt haben. Oder ein Kleinkind mit einer Tastatur.",
        "Mein Konverter fühlt sich gerade wie ein Kunstkritiker, der diese Farbe nicht einordnen kann. Sehr intellektuell.",
        "Ich kann das nicht konvertieren. Aber ich kann es bewundern. Aus sicherer Entfernung.",
        "Das ist die Farbe, die 'Nein, danke' sagt. Sie hat ihren eigenen Kopf.",
        "Ihr Farbwert hat seinen eigenen Willen. Er will keine Farbe sein. Er will frei sein!",
        "Hat da jemand die Tastatur geküsst? Ich sehe nur Liebe, keine Hex-Ziffern.",
        "Diese Eingabe ist wie ein Fluch. Ein digitaler Fluch, der meine Logik herausfordert.",
        "Ich bin beeindruckt von Ihrer Fähigkeit, ungültige Codes zu erstellen. Das ist ein Talent!",
        "Diese Eingabe ist so anarchisch, sie müsste eigentlich verboten werden. Oder in den Untergrund gehen.",
        "Mein System hat gerade eine Warnung wegen 'farblichem Unfug' ausgegeben. Bitte mäßigen Sie sich!",
        "Sie haben den Hex-Code für 'Absolute Verwirrung' gefunden. Glückwunsch, Sie sind der Erste!",
        "Das ist die Farbe der Geister, die Ihren Computer heimsuchen. Spukhaft, aber ungültig.",
        "Mein Konverter fragt sich, ob das eine geheime Botschaft ist. Vielleicht ein Ruf nach Hilfe?",
        "Diese Eingabe ist wie ein Pixel, das sich geweigert hat, sich anzupassen. Ein Nonkonformist.",
        "Ich sehe keine Farbe, nur Ihren Wunsch, die Regeln zu brechen. Sehr revolutionär.",
        "Das ist der Code, wenn man 'Farbe' rückwärts buchstabiert. Oder einfach nur Unsinn macht.",
        "Ist das die Farbe von Fehlern im frühen Cyberspace? Nostalgisch kaputt.",
        "Diese Eingabe ist so einzigartig, dass sie einen eigenen Algorithmus braucht. Ich bin nur für Hexadezimal da.",
        "Ich kann diese Farbe nicht verarbeiten. Sie ist zu... frei. Zu ungebunden.",
        "Ich glaube, Sie haben die Farbe der Hoffnung eingegeben. Leider ungültig, aber die Geste zählt!",
        "Dieser Code ist wie ein Geheimnis ohne Lösung. Man will es wissen, aber es gibt keine Antwort.",
        "Mein System hat gerade eine virtuelle Stirnfalte bekommen. Es denkt nach, es zweifelt.",
        "Diese Eingabe ist so abstrakt, sie gehört in die Tate Modern. Oder in eine digitale Ausstellung.",
        "Ist das die Farbe eines Bluescreens im Nirvana? Die ultimative Fehlermeldung.",
        "Ich habe versucht, das zu konvertieren, aber mein Prozessor hat nur ein gelangweiltes 'Meh' von sich gegeben.",
        "Mein Konverter ist gerade auf der Suche nach einem Existenzbeweis für diese Farbe. Bisher Fehlanzeige.",
        "Diese Eingabe ist so außerirdisch, ich bräuchte einen interstellaren Konverter. Oder ein besseres Handbuch.",
        "Mein System meldet eine 'unerklärliche Leuchtkraft der Ungültigkeit'. Es ist so falsch, dass es schon leuchtet.")
    GAME_INTRO1 = "Willkommen, Pixeljägerinnen und Farb-Enthusiasten, in der verrückten Welt von..."
    GAME_TITLE = "Hex-Huhn: Das Farben-Chaos!"
    GAME_INTRO2 = 'Habt ihr gedacht, nach "Moorhuhn" wäre das Kapitel\n"sinnfreies Ballerspiel mit Tieren" abgeschlossen? Ha! Weit gefehlt! \n\nIm neuen Jahrtausend ist die Evolution einen Schritt weitergegangen.\nStatt der sumpfbraunen Moorhühner jagt ihr nun die schillernden\nund geheimnisvollen Hex-Hühner aus dem Land der viereckigen Eier!\n\nOb #FF0000 (knallrot!), #00FFFF (türkis!) oder das kaum sichtbare\n#E6E6FA (Lavendelblush!) – zielt präzise, denn jeder Treffer zählt.\nUnd wer weiß, vielleicht entdeckt ihr ja beim fröhlichen Ballern\neure neue Lieblingsfarbe für die nächste Wohnzimmerwand.\n\nAlso, schnapp dir deine Maus, visiere die fliegenden Farbcodes an\nund beweise, dass du nicht nur Hühner, sondern auch Hex-Werte\nauf\'s Korn nehmen kannst. Mit der <LINKEN MAUSTASTE> wird geschossen\nund mit der <RECHTEN MAUSTASTE> nachgeladen... Weidmannsheil!'
    NEW_HIGHSCORE = (
        "Herzlichen Glückwunsch! Du hast es geschafft, die Pixel-Prominenz zu blamieren.",
        "Unglaublich! Deine Präzision bei Hex-Farben ist fast schon beängstigend.",
        "Ein wahrer Meister der digitalen Farbpalette! Dein Name wird in leuchtenden #Farben erstrahlen!",
        "Respekt! Du hast nicht nur Hühner, sondern auch Hex-Werte erlegt – das muss dir erstmal einer nachmachen!",
        "Phänomenal! Die Moorhühner hätten bei deinem Talent erst recht keine Chance gehabt.",
        "Chapeau! Du bist offiziell der Hex-Huhn-Flüsterer.",
        "Fantastisch! Du hast bewiesen, dass hinter den Farben mehr steckt, als man denkt.",
        "Gratulation! Du hast den Algorithmus des Chaos bezwungen und dich in die Annalen der Pixel-Jagd eingetragen.")
    NO_HIGHSCORE = (
        "Nicht traurig sein! Die Hex-Hühner sind heute einfach besonders flink gewesen. Dein Monitor muss mal wieder kalibriert werden.",
        "Uff, knapp daneben! Aber hey, Hauptsache, du hattest deinen Spaß beim Farb-Gemetzel.",
        "Manchmal tanzen die Pixel einfach anders. Kopf hoch, beim nächsten Mal zerlegst du die Farbwolken!",
        "Kein Grund zum Verzweifeln! Vielleicht waren die Hex-Hühner einfach zu gut getarnt. Das war bestimmt #FAFAFA auf #FDFDFD!",
        "Der Highscore ist nur eine Zahl – deine gesammelten Grautöne sind der wahre Schatz! (Wirklich!)",
        "Puh, das war wohl nichts mit Ruhm und Ehre. Aber immerhin hast du den digitalen Hühnerhof ordentlich aufgemischt!",
        "Die Farben waren heute einfach nicht auf deiner Seite. Versuch's morgen nochmal, wenn das Universum dich mehr liebt.",
        "Auch ein Meister der Farbpalette fängt klein an. Oder sehr, sehr niedrig auf der Highscore-Liste.",
        "Vielleicht hast du einfach zu viel auf die schönen Farben geachtet und nicht genug auf die Punkte. Kunst ist halt subjektiv!",
        "Egal, ob du gewonnen oder verloren hast – du hast auf jeden Fall eine Menge Zeit vor dem Bildschirm verbracht. Das ist doch auch was, oder?")
    NAME_ENTRY = "BITTE NAMEN EINGEBEN"
    START_GAME = "Spiel starten"
    END_GAME = "Spiel beenden"
    GAME_SCORE_TITLE = "Highscore"
    PLAY_AGAIN = "Neues Spiel"
    LIST_OF_PLAYERS = [
        ("Chroma-Königin Xenia", 1429),
        ("Johnny Walker", 1308),
        ("Frau Bratbecker", 1257),
        ("Die Grauschattige Eminenz", 1191),
        ("Henry M. Betrix", 1128),
        ("Baroness Buntstift", 1024),
        ("Art Vandelay (Import-Export)", 994),
        ("Herr Spektral-Specht", 913),
        ("Lady Lila-Laune", 863),
        ("Sir RGB von Schnelldruck", 754),]


class View(ttk.Frame):
    
    def __init__(self, parent_window):
        super().__init__(parent_window)
        self.window = parent_window
        self.grid(row = 0, column = 0, sticky = (tk.N, tk.E, tk.S, tk.W))
        self.controller = None
    
    def set_controller(self, controller):
        self.controller = controller

    def create_grid(self, rows, cols):
        for i in range(rows):
            self.rowconfigure(i, weight = 1)
        for i in range(cols):
            self.columnconfigure(i, weight = 1)


class Window():

    def configure_window(self, title, width, height):
        self.title(title)
        self.window_width = width
        self.window_height = height
        self.resizable(False, False)
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)

    def center_window_on_screen(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        center_x = int(screen_width / 2 - self.window_width / 2)
        center_y = int(screen_height / 2 - self.window_height / 2)
        self.geometry(
            f'{self.window_width}x{self.window_height}+{center_x}+{center_y}')


class MainModel():

    def __init__(self):
        self.hex_code = self.get_random_hex_string(6)
        self.rgb_code = self.get_rgb_from_hex_code(self.hex_code)
        self.css_name = self.get_name_of_hex_code(self.hex_code)
        self.colors_converted = list()

    @property
    def hex_code(self):
        return self._hex_code
    
    @hex_code.setter
    def hex_code(self, value):
        if self.is_hex_code(value, (3, 6)):
            self._hex_code = value
            self.rgb_code = self.get_rgb_from_hex_code(value)
            self.css_name = self.get_name_of_hex_code(value)
        else:
            raise ValueError()

    def is_hex_string(self, str_value):
        for i in str_value:
            if i.casefold() not in "0123456789abcdef":
                return False
        return True

    def is_hex_code(self, str_value, valid_lengths = (3, 4, 6, 8)):
        if self.is_hex_string(str_value):
            return True if len(str_value) in valid_lengths else False
        else:
            return False

    def get_decimal_from_hex_string(self, hex_str):
        decimal_value = 0
        for i in range(len(hex_str)):
            if hex_str[i].casefold() in "abcdef":
                summand = "abcdef".index(hex_str[i].casefold()) + 10
            else:
                summand = hex_str[i]
            decimal_value += int(summand) * 16 ** (len(hex_str) - 1 - i)
        return decimal_value

    def get_rgb_from_hex_code(self, hex_code):
        if len(hex_code) in (3, 4):
            hex_code = self.get_full_hex_code(hex_code)
        red = self.get_decimal_from_hex_string(hex_code[0:2])
        green = self.get_decimal_from_hex_string(hex_code[2:4])
        blue = self.get_decimal_from_hex_string(hex_code[4:6])
        if len(hex_code) == 8:
            alpha = 100 * self.get_decimal_from_hex_string(hex_code[6:8])//255
            return (red, green, blue, alpha)
        else:
            return (red, green, blue)

    def get_name_of_hex_code(self, search_hex):
        for css3_name, hex in COLOR_NAMES.items():  
            if hex.casefold() == search_hex.casefold():
                return css3_name
        return ""

    def get_random_hex_string(self, length):
        return ''.join(choices("0123456789abcdef", k = length))

    def get_full_hex_code(self, short_hex_code):
        return ''.join([i * 2 for i in short_hex_code])

    def unique_colors_converted(self):
        return len(set(self.colors_converted))


class MainView(View):

    def __init__(self, parent_window):
        super().__init__(parent_window)
        self.PADDING_X = 15
        self.PADDING_Y = 15
        self.controller = None
        self.create_grid(7, 1)
        for i in range(7):
            if i != 1: self.grid_rowconfigure(i, weight = 0)
        self.grid_rowconfigure(1, weight = 1)
        self.create_rgb_color_box()
        self.create_color_name_label()
        self.create_comment_label()
        self.create_combobox()
        self.create_convert_button()
        self.create_random_button()
        self.create_secret_button()
        self.create_checkbox()

    def create_rgb_color_box(self):
        self.label_rgb_code = tk.Label(
            self, text = '', font = ('Courier', 20, 'bold'), 
            height = 2, relief = 'groove')
        self.label_rgb_code.grid(
            row = 0, column = 0, sticky = (tk.N, tk.W, tk.E),
            ipadx = 50, ipady = 50, padx = self.PADDING_X, pady=self.PADDING_Y)
        
    def create_color_name_label(self):
        self.label_css_name = tk.Label(
            self, text = '', font = ('Arial', 8, 'bold'))
        self.label_css_name.grid(
            row = 0, column = 0, sticky = (tk.S, tk.W, tk.E), 
            padx = self.PADDING_X + 7, pady = (0, 60))
        self.label_css_name.grid_remove()

    def create_comment_label(self):
        self.comment_frame = ttk.LabelFrame(
            self, text='Die Stimmme der KI sagt:', labelanchor = tk.N)
        self.comment_frame.grid(
            row = 1, column=0, sticky = (tk.N, tk.W, tk.S, tk.E), 
            padx= self.PADDING_X)
        self.comment = tk.StringVar()
        self.comment_frame.grid_rowconfigure(0, weight = 1)
        self.comment_frame.grid_columnconfigure(0, weight = 1)
        self.label_comment = ttk.Label(
            self.comment_frame, textvariable = self.comment, wraplength = 330, 
            justify = tk.CENTER, anchor = tk.N, foreground = "#444444")
        self.label_comment.grid(
            row = 0, column = 0, sticky = (tk.W, tk.E))

    def create_combobox(self):
        self.user_input = tk.StringVar()
        self.cbox_color_select = ttk.Combobox(
            self, textvariable = self.user_input, font = ('Courier', 20),
            justify = tk.CENTER, state = 'normal', height = 20,
            value = tuple(COLOR_NAMES.keys()))
        self.cbox_color_select.grid(
            row = 2, column = 0, sticky = (tk.W, tk.E), ipadx = 30, ipady = 10, 
            pady = (self.PADDING_Y, self.PADDING_Y/2), padx = self.PADDING_X)
        self.cbox_color_select.bind(
            '<<ComboboxSelected>>', self.on_select_color_name)
        self.cbox_color_select.bind('<Return>', self.on_return_combobox)
        self.cbox_color_select.focus()
        self.cbox_color_select.select_range(0, 7)

    def create_convert_button(self):
        self.button_convert = ttk.Button(
            self, text = TEXT.LABEL_CONVERT_BTN, width = 20)
        self.button_convert.grid(
            row = 3, column = 0, sticky = (tk.W, tk.E),
            pady = (0, self.PADDING_Y/2), padx = self.PADDING_X)
        self.button_convert['command'] = self.on_click_convert_button

    def create_random_button(self):
        self.button_random = ttk.Button(self, text = TEXT.LABEL_RANDOM_BTN)
        self.button_random.grid(
            row = 4, column = 0, sticky = (tk.W, tk.E), 
            padx = self.PADDING_X, pady = (0, self.PADDING_Y/2))
        self.button_random['command'] = self.on_click_random_button

    def create_secret_button(self):
        self.secret_button = ttk.Button(self, text = TEXT.LABEL_SECRET_BTN)
        self.secret_button.grid(
            row = 5, column = 0, sticky = (tk.W, tk.E), 
            padx = self.PADDING_X, pady = (0, self.PADDING_Y/2))
        self.secret_button.grid_remove()
        self.secret_button['command'] = self.on_click_secret_button

    def create_checkbox(self):
        self.window_is_topmost = tk.BooleanVar()
        self.checkbox_topmost = ttk.Checkbutton(
            self, text = TEXT.LABEL_CHECKBOX, 
            variable = self.window_is_topmost)
        self.checkbox_topmost.grid(
            row = 6, column = 0, padx = self.PADDING_X, 
            pady = (self.PADDING_Y/2, self.PADDING_Y))
        self.checkbox_topmost['command'] = self.on_click_checkbox

    def on_click_secret_button(self):
        self.controller.open_game_window()

    def on_click_checkbox(self):
        self.controller.toggle_topmost(self.window_is_topmost.get())

    def on_return_combobox(self, event):
        self.controller.validate_input(self.user_input.get())

    def on_click_convert_button(self):
        self.controller.validate_input(self.user_input.get())

    def on_select_color_name(self, event):
        selected_color_name = self.user_input.get()
        self.user_input.set(f"#{COLOR_NAMES[selected_color_name].lower()}")
        self.cbox_color_select.select_range(0,7)
        self.controller.validate_input(self.user_input.get())

    def on_click_random_button(self):
        self.controller.set_input_to_random_hex_code()
        self.controller.validate_input(self.user_input.get())

    def set_user_input_to_value(self, value):
        self.user_input.set(value)

    def set_rgb_label_bg_color(self, hex_code):
        self.style = ttk.Style()
        self.style.configure('Color.TFrame',  background = f'#{hex_code}')
        self.label_rgb_code['background'] = f'#{hex_code}'
        self.label_css_name['background'] = f'#{hex_code}'

    def set_font_color(self, color):
        self.label_rgb_code['foreground'] = color
        self.label_css_name['foreground'] = color


class MainController:

    def __init__(self, app, model, view):
        self.app = app
        self.model = model
        self.view = view
        self.view.user_input.set(f'#{self.model.hex_code}')
        self.validate_input(self.model.hex_code)
        self.insert_comment(TEXT.DEFAULT_COMMENT)
        self.view.cbox_color_select.select_range(0,7)
        
    def set_input_to_random_hex_code(self):
        random_hex_code = self.model.get_random_hex_string(6)
        self.view.user_input.set(f'#{random_hex_code}')

    def validate_input(self, str_value):
        str_value = str_value.strip('# ')
        try:
            self.model.hex_code = str_value
            self.view.set_user_input_to_value(f'#{str_value}')
            self.model.colors_converted.append(str_value)
            self.display_rgb_code()
            self.comment_on_hex_code(str_value)
            if (self.model.unique_colors_converted() >= 42 and 
                self.app.secret_discovered is False): 
                self.reveal_secret_button()
                self.messagebox_secret_found()
        except ValueError:
            if self.model.is_hex_code(str(str_value), (4,)):
                self.view.user_input.set(f'#{str_value}')
                self.insert_comment(choice(TEXT.FOUR_DIGIT_CODES))
                self.display_message('TRANSPARENT')
            elif self.model.is_hex_code(str(str_value), (8,)):
                self.view.user_input.set(f'#{str_value}')
                self.insert_comment(choice(TEXT.EIGHT_DIGIT_CODES))
                self.display_message('TRANSPARENT')
            elif str_value.casefold() == TEXT.CHEAT_CODE:
                self.insert_comment(TEXT.CHEAT_USED)
                self.display_message('SECRET_FOUND')
                self.reveal_secret_button()
            elif str_value == "":
                self.insert_comment(choice(TEXT.NO_INPUT))
                self.display_message('EMPTY_INPUT')
            else:
                self.insert_comment(choice(TEXT.MISC_INVALID_INPUTS))
                self.display_message('INVALID_INPUT')
    
    def display_rgb_code(self):
        self.view.label_css_name.grid_remove()
        rgb = self.model.rgb_code
        self.view.label_rgb_code['text'] = f"({rgb[0]},{rgb[1]},{rgb[2]})"
        self.view.set_rgb_label_bg_color(self.model.hex_code)
        self.view.set_font_color(self.get_contrasting_color())
        if self.model.css_name:
            self.view.label_css_name['text'] = self.model.css_name
            self.view.label_css_name.grid()

    def display_message(self, type):
        self.view.label_css_name.grid_remove()
        self.view.set_rgb_label_bg_color("dddddd")
        self.view.set_font_color("#aaaaaa")
        match type:
            case 'INVALID_INPUT':
                self.view.label_rgb_code['text'] = TEXT.LABEL_INVALID_INPUT
            case 'EMPTY_INPUT':
                self.view.label_rgb_code['text'] = TEXT.LABEL_EMPTY_INPUT
            case 'TRANSPARENT':
                self.view.label_rgb_code['text'] = TEXT.LABEL_TRANSPARENT_COLOR
            case 'SECRET_FOUND':
                self.view.label_rgb_code['text'] = TEXT.LABEL_SECRET_UNLOCKED
                    
    def reveal_secret_button(self):
        self.app.secret_discovered = True
        self.app.geometry(
            f"{self.app.window_width}x{self.app.window_height + 40}")
        self.view.secret_button.grid()
    
    def messagebox_secret_found(self):
        msgbox.showinfo(title = TEXT.SECRET_TITLE, message = TEXT.SECRET_MSG,
                        detail = TEXT.SECRET_DETAIL)

    def comment_on_hex_code(self, hex_input):
        match len(hex_input):
            case 3:
                self.insert_comment(choice(TEXT.THREE_DIGIT_CODES))
            case 6:
                try:
                    self.insert_comment(
                        choice(TEXT.NAMED_CODES[hex_input.upper()]))
                except:
                    if random() < 0.75:
                        self.insert_comment(choice(TEXT.MISC_CODES))
                    else:
                        self.insert_comment(choice(TEXT.RANDOM))

    def insert_comment(self, comment):
        self.view.comment.set(comment)

    def get_contrasting_color(self):
        luminance =  (self.model.rgb_code[0] * 0.2126 + 
                      self.model.rgb_code[1] * 0.7152 + 
                      self.model.rgb_code[2] * 0.0722)
        return 'white' if luminance < 140 else 'black'

    def toggle_topmost(self, bool_value):
        self.app.call('wm', 'attributes', '.', '-topmost', bool_value)

    def open_game_window(self):
        new_window = GameWindow()
        new_window.grab_set()


class MainWindow(Window, tk.Tk):

    def __init__(self):
        super().__init__()
        self.configure_window(TEXT.APP_TITLE, 380, 600)
        self.center_window_on_screen()
        self.model = MainModel()
        self.view = MainView(self)
        self.controller = MainController(self, self.model, self.view)
        self.view.set_controller(self.controller)
        self.secret_discovered = False
        self.protocol('WM_DELETE_WINDOW', self.display_exit_confirmation)

    def display_exit_confirmation(self):
        if self.secret_discovered is False:
            close_window = msgbox.askyesno(
                title = TEXT.EXIT_CONF_TITLE, message = TEXT.EXIT_CONF_MSG, 
                detail=TEXT.EXIT_CONF_DETAIL)
            if close_window: self.destroy()
        else:
            self.destroy()


# # # # # # # # # #    Ab hier wird's komplett albern :)    # # # # # # # # # #


class GamePoints:

    def __init__(self, parent, current_x, current_y, points):
        self.parent = parent
        self.current_x = current_x
        self.current_y = current_y
        self.points = points
        self.time_passed = 0
        self.create_shape()

    def create_shape(self):
        self.shape = self.parent.canvas.create_text(
            (self.current_x, self.current_y), text = self.points,
            fill='#bbbbbb', justify='center', font = ('Arial', 14))
    
    def self_destroy(self):
        self.parent.canvas.delete(self.shape)
        self.parent.points.pop(self.parent.points.index(self))

    def move(self):
        self.parent.canvas.move(self.shape, 0, -1.5)
        self.time_passed += 1


class GameChicken:
    
    def __init__(self, parent, points, size, amplitude, 
                 velocity, flying_range, layer):
        self.parent = parent
        self.points = points
        self.width = self.height = size
        self.amplitude = amplitude
        self.velocity = randint(velocity - 10, velocity + 10) / 100
        self.flying_range = flying_range
        self.layer = layer
        self.alive = True
        self.special = False
        self.set_coordinates()
        self.set_delta_values()
        self.create_shape()

    def set_coordinates(self):
        self.initial_x = choice([0 - self.width, CANVAS_WIDTH])
        self.current_x = self.initial_x
        self.initial_y = randint(
            self.flying_range[0] + self.amplitude,
            self.flying_range[1] - self.height - self.amplitude)
        self.current_y = self.initial_y

    def set_delta_values(self):
        self.delta_x = self.velocity if self.initial_x < 0 else -self.velocity
        self.delta_y = 0.5

    def create_shape(self):
        self.shape = self.parent.canvas.create_rectangle(
            (0, 0), (self.width, self.height),
            fill = f"#{self.get_random_hex_color()}", outline="")
        self.parent.canvas.tag_lower(self.shape, self.layer)
        self.parent.canvas.moveto(self.shape, self.initial_x, self.initial_y)
        self.parent.canvas.tag_bind(
            self.shape, '<Button-1>', lambda event: self.kill())

    def is_on_canvas(self):
        if (self.current_x >= -self.width and 
            self.current_x <= CANVAS_WIDTH and 
            self.current_y <= CANVAS_HEIGHT):
            return True
        else:
            return False
        
    def make_special(self):
        self.special = True
        self.points *= 2

    def get_random_hex_color(self):
        return ''.join(choices("456789abcdef", k = 6))

    def change_color(self):
        self.parent.canvas.itemconfigure(
            self.shape, fill = f"#{self.get_random_hex_color()}")

    def self_destroy(self):
        self.parent.canvas.delete(self.shape)
        self.parent.chickens.pop(self.parent.chickens.index(self))

    def move(self):
        match self.alive:
            case True:
                self.parent.canvas.move(self.shape, self.delta_x, self.delta_y)
                if abs(self.current_y - self.initial_y) >= self.amplitude:
                    self.delta_y *= -1 
            case False:
                    self.parent.canvas.move(self.shape, self.delta_x/2, 2)
        self.current_x += self.delta_x
        self.current_y += self.delta_y

    def kill(self):
        if self.parent.ammo > 0:
            self.alive = False
            self.parent.count += self.points
            self.parent.canvas.tag_unbind(self.shape, '<Button-1>')
            new_points = GamePoints(
                self.parent, self.current_x, self.current_y, self.points)
            self.parent.points.append(new_points)
 

class GameChickenSmall(GameChicken):

    def __init__(self, parent, points = 25, size = 8, 
                 amplitude = 20, velocity = 100, layer = 1,
                 flying_range = (0, CANVAS_HEIGHT*3//5)):
        super().__init__(parent, points, size, amplitude, 
                         velocity, flying_range, layer)
        if random() < 0.05: self.make_special()
    

class GameChickenMedium(GameChicken):

    def __init__(self, parent, points = 10, size = 16, 
                 amplitude = 25, velocity = 125, layer = 2, 
                 flying_range = (CANVAS_HEIGHT*1//5, CANVAS_HEIGHT*4//5)):
        super().__init__(parent, points, size, amplitude, 
                         velocity, flying_range, layer)
        if random() < 0.05: self.make_special()


class GameChickenLarge(GameChicken):

    def __init__(self, parent, points = 5, size = 32, 
                 amplitude = 30, velocity = 150, layer = 3, 
                 flying_range = (CANVAS_HEIGHT*1//5, CANVAS_HEIGHT*3//4)):
        super().__init__(parent, points, size, amplitude, 
                         velocity, flying_range, layer)


class GameChickenHuge(GameChicken):

    def __init__(self, parent, points = 5, size = 64, 
                 amplitude = 25, velocity = 125, layer = 4, 
                 flying_range = (CANVAS_HEIGHT*3//5, CANVAS_HEIGHT*4//5)):
        super().__init__(parent, points, size, amplitude, 
                         velocity, flying_range, layer)


class GameHighscore():
    
    def __init__(self):
        self.user_name = None
        self.user_scores = list()
        self.new_high_score = False
        self.all_scores = TEXT.LIST_OF_PLAYERS
    
    def set_user_name(self, user_name):
        self.user_name = user_name

    def update(self, new_score):
        if new_score > self.all_scores[-1][1]:
            self.all_scores.pop()
            self.all_scores.append((self.user_name, new_score))
            self.all_scores.sort(key = lambda x: int(x[1]), reverse = True)
            self.new_high_score = True


class GameView(View):

    def __init__(self, parent_window):
        super().__init__(parent_window)
        self.window = parent_window
        self.grid(row = 0, column = 0, sticky = (tk.N, tk.E, tk.S, tk.W))
        self.controller = None


class GameViewStart(GameView):

    def __init__(self, parent_window):
        super().__init__(parent_window)
        self.create_grid(5, 1)
        self.rowconfigure(0, weight = 0)
        self.rowconfigure(1, weight = 0)
        self.rowconfigure(2, weight = 0)
        self.rowconfigure(3, weight = 0)
        self.rowconfigure(4, weight = 0)
        self.create_intro1_text()
        self.create_title()
        self.create_intro2_text()
        self.create_user_name_entry()
        self.create_start_button()
        self.configure(style="Game.TFrame")
        self.app = parent_window
        self.highscore = parent_window.highscore

    def create_intro1_text(self):
        self.label_text = ttk.Label(
            self, font = ("Arial", 12), justify = tk.CENTER, 
            style = 'Game.TLabel', anchor = tk.N, 
            text = f"\n\n{TEXT.GAME_INTRO1}", wraplength = 900)
        self.label_text.grid(
            row = 0, column = 0, sticky = (tk.E, tk.W))

    def create_title(self):
        self.label_title = ttk.Label(
            self, text = TEXT.GAME_TITLE, justify = tk.CENTER, 
            style = 'Game.TLabel', anchor = tk.S, 
            font = ("Arial", 18, 'bold'))
        self.label_title.grid(
            row = 1, column = 0, pady = 30, sticky = tk.S)

    def create_intro2_text(self):
        self.label_text = ttk.Label(
            self, font = ("Arial", 12), justify = tk.CENTER, 
            style = 'Game.TLabel', anchor = tk.N, 
            text = f"{TEXT.GAME_INTRO2}\n", wraplength = 900)
        self.label_text.grid(
            row = 2, column = 0, sticky = (tk.E, tk.W))

    def create_user_name_entry(self):
        self.user_name = tk.StringVar()
        self.user_name.set(TEXT.NAME_ENTRY)
        self.entry_name = ttk.Entry(
            self, text = self.user_name, justify = tk.CENTER, width = 25,
            font = ("TkDefaultFont", 12))
        self.entry_name.grid(
            row = 3, column = 0, sticky = tk.N, ipadx=5, ipady=8, pady=10)
        self.entry_name.bind(
            '<KeyRelease>', lambda event: self.on_keyrelease_entry_field())
        self.entry_name.bind(
            '<Return>', lambda event: self.on_return_entry_field(), add = '+')
        self.entry_name.focus()
        self.entry_name.select_range(0,100)
    
    def create_start_button(self):
        self.button_start = ttk.Button(
            self, text = TEXT.START_GAME, state = 'disabled',
            width = 34, command = self.on_click_start_button)
        self.button_start.grid(row = 4, column = 0, pady = 0, sticky = tk.N)
        
    def on_return_entry_field(self):
        if self.entry_name.get().strip() != "":
            self.on_click_start_button()

    def on_keyrelease_entry_field(self):
        if self.entry_name.get().strip() != "":
            self.button_start['state'] = 'enabled'
        else:
            self.button_start['state'] = 'disabled'

    def on_click_start_button(self):
        if self.controller:
            self.controller.prepare_new_game(self.entry_name.get())


class GameViewAction(GameView):

    def __init__(self, parent_window):
        super().__init__(parent_window)
        self.create_grid(1, 1)
        self.create_canvas()
        self.create_landscape()
        self.create_overlay()
        self.MAX_AMMO = 6
        self.DURATION_IN_SECONDS = 90
        self.DELTA_TIME_IN_MS = 10

    def create_canvas(self):
        self.canvas = tk.Canvas(
            self, width = CANVAS_WIDTH, height = CANVAS_HEIGHT,
            bg = '#333333', cursor = 'crosshair')
        self.canvas.grid(row = 0, column = 0)
        self.canvas.bind(
            '<Button-1>', lambda event: self.reduce_ammo())
        self.canvas.bind(
            '<Button-2>', lambda event: self.reload_ammo(), add='+')
        self.canvas.bind(
            '<Button-3>', lambda event: self.reload_ammo(), add='+')

    def create_landscape(self):
        landscape_layers = (
            (0.67, '#444444'), (0.76, '#555555'), (0.87, '#666666'))
        for i in landscape_layers:
            self.canvas.create_rectangle(
                (0, int(i[0] * CANVAS_HEIGHT)), (CANVAS_WIDTH, CANVAS_HEIGHT),
                fill = i[1], outline = '')

    def create_overlay(self):
        PADDING = 20
        self.overlay_time = self.canvas.create_text(
            (PADDING, PADDING), anchor = 'nw',
            fill = 'white', justify = 'left', font = ('Arial', 24))
        self.overlay_score = self.canvas.create_text(
            (CANVAS_WIDTH - PADDING, PADDING), anchor = 'ne',
            fill = 'white', justify = 'right', font = ('Arial', 24))
        self.overlay_ammo = self.canvas.create_text(
            (CANVAS_WIDTH-PADDING, CANVAS_HEIGHT-PADDING), anchor = 'se',
            fill = 'white', justify = 'right', font = ('Arial', 24, 'bold'))

    def start_new_game(self):
        self.set_focus_on_canvas()
        self.chickens = list()
        self.points = list()
        self.count = 0
        self.ammo = self.MAX_AMMO
        self.seconds_remaining = self.DURATION_IN_SECONDS
        self.seconds_passed = 0
        self.start_time = time.time()
        self.run_game()

    def set_focus_on_canvas(self):
        self.canvas.config(highlightthickness = 0)
        self.canvas.focus_set()
        self.canvas.focus()

    def end_game(self):
        for i in self.chickens: self.canvas.delete(i.shape)
        self.chickens.clear()
        for i in self.points: self.canvas.delete(i.shape)
        self.points.clear()
        if self.controller:
            self.controller.update_high_score(self.count)
            self.controller.show_high_score()

    def reduce_ammo(self):
        if self.ammo != 0: self.ammo -= 1

    def reload_ammo(self):
        if self.ammo == 0: self.ammo = self.MAX_AMMO

    def update_time(self):
        if time.time() - (self.start_time + self.seconds_passed) >= 1:
            self.seconds_passed += 1
            self.seconds_remaining -= 1

    def get_time_in_minutes(self):
        minutes = self.seconds_remaining // 60
        seconds = self.seconds_remaining % 60
        return f"{minutes}:{seconds:02d}"

    def spawn_chickens(self):
        if random() < 0.007: self.chickens.append(GameChickenSmall(self))
        if random() < 0.008: self.chickens.append(GameChickenMedium(self))
        if random() < 0.009: self.chickens.append(GameChickenLarge(self))
        if random() < 0.001: self.chickens.append(GameChickenHuge(self))

    def update_overlay(self):
        self.canvas.itemconfigure(self.overlay_score, text=f'{self.count}')
        self.canvas.itemconfigure(self.overlay_time,
                                  text = self.get_time_in_minutes())
        self.canvas.itemconfigure(self.overlay_ammo,
                                  text=f'{' I' * self.ammo}')

    def run_game(self):
        self.spawn_chickens()
        for i in self.chickens:
            i.move() if i.is_on_canvas() else i.self_destroy()
            if i.special is True: i.change_color()
        for i in self.points:
            i.move() if i.time_passed < 25 else i.self_destroy()
        self.update_overlay()
        self.update_time()
        if self.seconds_remaining >= 0:
            return self.canvas.after(self.DELTA_TIME_IN_MS, self.run_game)
        else:
            return self.end_game()


class GameViewScore(GameView):

    def __init__(self, parent_window):
        super().__init__(parent_window)
        self.create_grid(5, 3)
        self.rowconfigure(0, weight=3)
        self.rowconfigure(4, weight=3)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.create_title()
        self.create_list_frame()
        self.create_label_ranks()
        self.create_label_names()
        self.create_label_scores()
        self.create_label_points()
        self.create_label_message()
        self.create_button_again()

    def create_title(self):
        self.label_title = ttk.Label(
            self, text = TEXT.GAME_SCORE_TITLE, justify = tk.CENTER, 
            style = 'Game.TLabel', anchor = tk.S, 
            font = ("Arial", 18, 'bold'))
        self.label_title.grid(
            row = 0, column = 0, pady = 30, sticky = tk.S, columnspan=3)

    def create_list_frame(self):
        self.list_frame = ttk.Frame(self)
        self.list_frame.grid(row = 1, column=1, sticky=(tk.W, tk.E))
        self.list_frame.rowconfigure(0, weight=0)
        self.list_frame.columnconfigure(0, weight=1)
        self.list_frame.columnconfigure(1, weight=1)
        self.list_frame.columnconfigure(2, weight=1)

    def create_label_ranks(self):
        self.label_ranks = ttk.Label(
            self.list_frame, text = "", justify = tk.RIGHT, anchor=tk.E,
            font = ("Arial", 12), style = 'Game.TLabel')
        self.label_ranks.grid(row = 0, column = 0)

    def create_label_names(self):
        self.label_names = ttk.Label(
            self.list_frame, text = "", justify = tk.LEFT, anchor=tk.N,
            font = ("Arial", 12), style = 'Game.TLabel')
        self.label_names.grid(row = 0, column = 1)

    def create_label_scores(self):
        self.label_scores = ttk.Label(
            self.list_frame, text = "", justify = tk.RIGHT, anchor=tk.W,
            font = ("Arial", 12), style = 'Game.TLabel')
        self.label_scores.grid(row = 0, column = 2)

    def create_label_points(self):
        self.label_points = ttk.Label(self, text = "", style = 'Game.TLabel',  
                                      font = ("Arial", 12, 'bold'))
        self.label_points.grid(row = 2, column = 0, columnspan=3)

    def create_label_message(self):
        self.label_msg = ttk.Label(
            self, text = "", wraplength = 500, style = 'Game.TLabel', 
            font = ("Arial", 12), justify = tk.CENTER, anchor = tk.N)
        self.label_msg.grid(row = 3, column = 0, columnspan=3)

    def create_button_again(self):
        self.button_again = ttk.Button(
            self, text = TEXT.PLAY_AGAIN, width = 34,
            command = self.on_click_button_again)
        self.button_again.grid(row = 4, column = 0, columnspan=3)

    def on_click_button_again(self):
        self.controller.prepare_new_game()


class GameController():

    def __init__(self, highscore, views, switcher):
        self.highscore = highscore
        self.views = views
        self.switch_to_view = switcher

    def prepare_new_game(self, user_name = None):
        if user_name is not None: self.highscore.set_user_name(user_name)
        self.highscore.new_high_score = False
        self.switch_to_view('ACTION')
        self.views['ACTION'].start_new_game()

    def update_high_score(self, new_score):
        self.highscore.update(new_score)
        self.views['SCORE'].label_points['text'] = f"{new_score} Punkte"
        if self.highscore.new_high_score is True:
            message = choice(TEXT.NEW_HIGHSCORE)
        else:
            message = choice(TEXT.NO_HIGHSCORE)
        self.views['SCORE'].label_msg['text'] = message
        ranks = ""
        names = ""
        scores = ""
        for i in self.highscore.all_scores:
            ranks += f"{self.highscore.all_scores.index(i)+1}.\n"
            names += f"{i[0]}\n"
            scores += f"{i[1]}\n"
        self.views['SCORE'].label_ranks['text'] = ranks
        self.views['SCORE'].label_names['text'] = names
        self.views['SCORE'].label_scores['text'] = scores

    def show_high_score(self):
        self.switch_to_view('SCORE')


class GameWindow(Window, tk.Toplevel):

    def __init__(self):
        super().__init__()
        self.configure_window(
            TEXT.GAME_TITLE, CANVAS_WIDTH + 4, CANVAS_HEIGHT + 4)
        self.center_window_on_screen()
        self.highscore = GameHighscore()
        self.views = {
            'START' : GameViewStart(self),
            'ACTION' : GameViewAction(self),
            'SCORE' : GameViewScore(self)
        }
        self.set_controller()
        self.switch_to_view('START')

    def set_controller(self):
        self.controller = GameController(
            self.highscore, self.views, self.switch_to_view)
        for view in self.views.values():
            view.set_controller(self.controller)

    def switch_to_view(self, next_view):
        match next_view:
            case 'START': self.views['START'].tkraise()
            case 'ACTION': self.views['ACTION'].tkraise()
            case 'SCORE': self.views['SCORE'].tkraise()


app = MainWindow()
app.mainloop()