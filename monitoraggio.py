SOGLIA_ORE = 1000

aeromobili = [
    {"codice": "I-ABC", "modello": "A320", "ore_volo": 1240, "controlli_ok": True},
<<<<<<< HEAD
    {"codice": "I-DEF", "modello": "B737", "ore_volo": 850, "controlli_ok": False},
    {"codice": "I-GHI", "modello": "ATR72", "ore_volo": 1500, "controlli_ok": False},
    {"codice": "I-JKL", "modello": "A350", "ore_volo": 450, "controlli_ok": True}
]

def stampa_riepilogo(lista):
    print("=== RIEPILOGO FLOTTA ===")
    for aero in lista:
        stato = "OK" if aero["controlli_ok"] else "INSPECTION NEEDED"
        print(f"[{aero['codice']}] Modello: {aero['modello']} | Ore: {aero['ore_volo']} | Controlli: {stato}")
=======
    {"codice": "I-DEF", "modello": "B737", "ore_volo": 850, "controlli_ok": False}
]

def filtra_controlli_non_validi(lista):
    return [aero for aero in lista if not aero["controlli_ok"]]

def filtra_oltre_soglia(lista, soglia):
    return [aero for aero in lista if aero["ore_volo"] > soglia]
>>>>>>> origin/features/segnalazioni
