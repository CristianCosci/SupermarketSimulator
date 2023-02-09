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

<hr>

## **Studio Teorico e Analisi del modello**
È possibile rappresentare il sistema reale mediante un modello ad eventi discreti di tipo aperto, con spazio degli stati discreto. Nel nostro caso, abbiamo analizzato il Supermercato Conad località Mercatale. Nello specifico un cliente che intende andare a fare spesa può usufruire dei seguenti Reparti:
- Macelleria
- Gastronomia (non macelleria)
- Scaffali
Le casse disponibili ai clienti sono le seguenti:
- 1 Casse per chi acquista generi alimentari

### CONCLUSIONI DOPO LE OSSERVAZIONI SETTIMANALI
Per analizzare in maniera corretta i parametri caratteristici dell’attività commerciale presa in esame, abbiamo monitorato l’afflusso di persone tra le 16:00 e le 20:00, poiché in tale periodo si ha il maggior afflusso di clienti.

Possiamo osservare che l’andamento è il seguente:
- Dalle 16:00 alle 17:45 gli arrivi tendono a crescere
- Dalle 17:30 alle 17:45 abbiamo il picco massimo di arrivi (max arrivi in 15min è 21)
- Dalle 17:45 alle 20:00 gli arrivi tendono a scemare

Il numero medio persone al minuto che arrivano al sistema è circa 0,61 (uno ogni 1,6 min = uno ogni 97,29 secondi), infatti nelle 4 ore prese in esame, sono arrivati circa 148 clienti. Il tempo di servizio varia secondo l’operazione effettuata. Si ha quindi:
|    **Reparto**    |**Tempo di Servizio Medio**| **Servienti** |modello di coda|
| -                 | -                         | -             | - |
|  **Gastronomia**  | 3 minuti                  | 1             | $m/m/1$ |
| **Macelleria**    | 4 minuti                  | 1             | $m/m/1$ |
| **Scaffali**      | 10 minuti                 | $\infty$      | $m/m/\infty$
| **Cassa**         | 4 minuti                  | 1             | $m/m/1$ |

### Metodo delle prove ripetute
Per convalidare il simulatore abbiamo utilizzato il metodo delle prove ripetute. Prima di vedere effettivamente come è stato implementato in python facciamo dei cenni teorici relativi a tale metodo.