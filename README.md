Napisz program dla bankomatu który działa na poniższych założeniach:
•    Zakłada się, że bankomat jest automatem wolnostojącym, z dostępem do Internetu.
Bankomat jest powiązany w bankiem internetowym, w którym klient na konto. Klient może pobrać z bankomatu kwotę nie wyższą niż połowa stanu jego konta. Sekwencja operacji poboru gotówki z bankomatu – jest losowa.
Przed pobraniem gotówki z bankomatu, klient jest identyfikowany poprzez :
a) Numer PIN;
b) Kartę bankową
•    Konwersacja klienta z bankomatem odbywa się za pomocą ekranu. Identyfikacja klienta jest dokonywana raz na godzinę (tzn., że po nieprawidłowej identyfikacji, następuje blokada na 1 godzinę). W przypadku prawidłowej identyfikacji – klient podaje kwotę, która ma być wypłacona. W przypadku braku pokrycia tej kwoty, następuje blokada na 1 dzień.
•    W stanie początkowym, w kasetach bankomatu znajduje się :
a) 10 banknotów – o nominale 200PLN;
b) 10 banknotów – o nominale 100PLN;
c) 10 banknotów – o nominale 50PLN;
d) 10 banknotów – o nominale 20PLN;
e) 10 banknotów – o nominale 10PLN;
•    Bankomat może wydawać kwoty, które są wielokrotnością 10PLN (do 500PLN) – od banknotów o najwyższych nominałach do banknotów o najniższych nominałach.
•    Jeśli bankomat nie ma banknotów o jakichś nominałach lub nie może wydać żądanej kwoty to jest częściowo niesprawny. W takim przypadku bankomat powinien podać na ekranie „najbliższą” kwotę – niższą lub wyższą – którą może wydać. Jeśli bankomat nie potrafi wydać żądanej kwoty – to jest niesprawny."
•    Przy budowie programu utwórz 5 użytkowników z przypisanymi kwotami początkowymi na rachunku ( każda operacja zmienia stan konta )
