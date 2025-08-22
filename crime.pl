% Types de crime
crime_type(assassinat).
crime_type(vol).
crime_type(escroquerie).

% Faits - Suspects
suspect(john).
suspect(mary).
suspect(alice).
suspect(bruno).
suspect(sophie).

% Motifs
has_motive(john, vol).
has_motive(mary, assassinat).
has_motive(alice, escroquerie).

% Présence sur la scène de crime
was_near_crime_scene(john, vol).
was_near_crime_scene(mary, assassinat).

% Empreintes sur l'arme
has_fingerprint_on_weapon(john, vol).
has_fingerprint_on_weapon(mary, assassinat).

% Transactions bancaires suspectes
has_bank_transaction(alice, escroquerie).

% Fausse identité
owns_fake_identity(sophie, escroquerie).

% Règles de culpabilité

% Règle pour le vol
is_guilty(Suspect, vol) :-
    has_motive(Suspect, vol),
    was_near_crime_scene(Suspect, vol),
    ( has_fingerprint_on_weapon(Suspect, vol)
    ; eyewitness_identification(Suspect, vol)
    ).

% Règle pour l'assassinat
is_guilty(Suspect, assassinat) :-
    has_motive(Suspect, assassinat),
    was_near_crime_scene(Suspect, assassinat),
    ( has_fingerprint_on_weapon(Suspect, assassinat)
    ; eyewitness_identification(Suspect, assassinat)
    ).

% Règle pour l'escroquerie (corrigée)
is_guilty(Suspect, escroquerie) :-
    has_motive(Suspect, escroquerie),
    ( has_bank_transaction(Suspect, escroquerie)
    ; owns_fake_identity(Suspect, escroquerie)
    ).

% Quelques témoins oculaires pour les tests
eyewitness_identification(john, vol).
eyewitness_identification(mary, assassinat).