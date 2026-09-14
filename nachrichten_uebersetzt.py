import feedparser
import anthropic
import json

client = anthropic.Anthropic()

url = "https://rss.orf.at/news.xml"
feed = feedparser.parse(url)

def uebersetze(text):
    antwort = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=500,
        system="Du bist ein professioneller Übersetzer für Nachrichtentexte ins Arabische. Übersetze natürlich und flüssig, so wie ein muttersprachlicher Journalist schreiben würde – nicht wörtlich. Gib NUR die Übersetzung zurück, ohne Einleitung oder Erklärung.",
        messages=[
            {"role": "user", "content": text}
        ]
    )
    return antwort.content[0].text

ergebnisse = []

for eintrag in feed.entries[:5]:
    titel_original = eintrag.title
    kategorie = eintrag.tags[0].term
    titel_arabisch = uebersetze(titel_original)
    
    nachricht = {
    "titel_original": titel_original,
    "titel_arabisch": titel_arabisch,
    "link": eintrag.link,
    "kategorie": kategorie
}
    ergebnisse.append(nachricht)
    print("Fertig:", titel_original)

datei = open("nachrichten.json", "w")

json.dump(ergebnisse, datei, ensure_ascii=False, indent=2)

datei.close()