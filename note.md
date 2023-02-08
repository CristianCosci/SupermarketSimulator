# Creazione dei dati
Per determinare i dati si potrebbe pensare ad un intervallo con un unico picco e non doppio (per non incorrere in distribuzioni troppo complesse, l'obiettivo è restare al massimo nella poissoniana)

Un ipotetico intervallo da seguire può essere quello dell'orario di apertura pomeridiano, dalle 16 alle 20 e generare il picco intorno alle 17:30/18:00.

Un buon numero di ingressi, osservando le distribuzioni degli altri progetti può essere intorno ai 70 totali con intervalli da 15 minuti e con un minimo di 7 persone ad intervallo.

- totale intervalli 16
- minimo intervalli 1
- massimo intervalli 21

I dati sono stati creati e rispettano una distribuzione di Poisson come previsto  e voluto.

<hr>

# Struttura del progetto
- Descrizione del problema
- Pianificazione della simulazione
- Studio teorico e analisi del modello con relativo grafico e disegno
- Spiegazione dei dati e relativa convalida
- Parametri del sistema reale
- Metodo delle prove ripetute
- Analisi del modello e dei relativi nodi
- Costruzione del simulatore
- Simulazione effettiva
- Proposte di miglioramento (da trovare almeno 2) e relativi parametri
- Conclusione


## Valori da calcolare per analisi del modello (per ogni nodo)
- Tempo medio di arrivi lamda
- Tempo meido di servizio Ts
- tempo medio di interarrivo mu
- intensità traffico del sistema rho
- numero medio di utenti presenti nel sistema N
-  numero medio di utenti in coda W
- tempo medio atteso in coda Tw
- Tempio medio di risposta R o Tr