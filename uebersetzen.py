import anthropic

client = anthropic.Anthropic()


text_original = "Wirtschaftskammer beginnt mit Stellenabbau"

antwort = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=500,
    system="Du bist ein professioneller Übersetzer für Nachrichtentexte ins Arabische. Übersetze natürlich und flüssig, so wie ein muttersprachlicher Journalist schreiben würde – nicht wörtlich. Gib NUR die Übersetzung zurück, ohne Einleitung oder Erklärung.",
    messages=[
        {"role": "user", "content": text_original}
    ]
)

print(antwort.content[0].text)