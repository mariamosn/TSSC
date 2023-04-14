Maria Moșneag
343C1
Tema 1 TSSC


1. cryptography
    Am analizat pașii urmați pentru generarea mesajului criptat și apoi am scris
    un script (task1.py) pe care să îl folosesc pentru decriptare.
    Scriptul:
        - are o valoare hardcodată pentru cheia privată
        - primește g și p ca input
        - calculează și afișează cheia publică
        - primește cheia publică a celuilalt
        - calculează cheia partajată
        - decodează mesajul din base64
        - decriptează codul obținut folosind cheia determinată anterior

2. linux access control (remote container)


3. binary exploit
    Am folosit Ghidra pentru a analiza binarul.
    Pentru a obține flag-ul am exploatat aceeași vulnerabilitate de două ori, și
    anume faptul că, în funcția loop, când numerele sunt citite în buffer, nu se
    verifică nicio limită, astfel încât este ușor faci buffer overflow și să su-
    prascrii datele de pe stivă, inclusiv adresa de return și primul parametru.
    Astfel, am modificat flow-ul programului în următorul fel:
        - Din main se apelează loop.
        - În loop se citesc numerele și, prin buffer overflow, se suprascrie a-
            dresa de return cu cea a funcției loop.
        - Este afișată valoarea lucky_number.
        - Când suntem întrebați dacă vrem să continuăm, alegem "n", pentru că
            astfel nu mai este generată o nouă valoare pentru lucky_number, păs-
            trându-se cea care a fost afișată anterior.
        - La ieșirea din funcție, se sare la adresa de return care, fiind supra-
            scrisă anterior este începutul funcției loop.
        - Se citesc iar numerele, iar de această dată suprascriem adresa de
            return cu cea a funcției win și primul parametru cu valoarea
            lucky_number afișată anterior.
        - Alegem și de această dată opțiunea "n" când suntem întrebați dacă do-
            rim să continuăm.
        - La ieșirea din funcție se sare la win.
        - În win se verifică dacă primul parametru este egal cu lucky_number și,
            fiind suprascris anterior (și cum lucky number nu a mai fost recal-
            culat), condiția este satisfăcută.
        - Este afișat flag-ul.

    Payload-uri:
        - "[orice]\n": când ni se cere numele
        - "[orice număr] " * 37
            + "[134514611 = valoarea în decimal egală cu 0x080487b3, adresa
                            funcției loop]"
            + "x\n"
        - "n\n": când suntem întrebați dacă continuăm
        - "[orice număr] " * 37
            + "[134514406 = valoarea în decimal egală cu 0x080486e6, adresa
                            funcției win]"
            + "[orice număr] "
            + "[valoarea lucky_number afișată anterior] "
            + "x\n"
        - "n\n": când suntem întrebați dacă continuăm

[
    Extra:
    A doua abordare presupune:
        - folosirea unui format string attack în main pentru a afla valoarea
            lucky_number (string-ul citit ca nume era apoi folosit ca format
            string într-un apel de printf, fiind astfel posibil să incluzi adre-
            sa de la care vrei să faci leak-ul în string, iar apoi un %s astfel
            încât să fie afișat string-ul de la acea adresă)
        - exploatarea aceleași vulnerabilități din loop pentru a suprascrie:
            adresa de return cu cea a funcției win și
            primul parametru cu valoarea lucky_number leak-uită anterior
]
