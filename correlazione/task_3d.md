**TASK3d: A partire da uno dei dataset che avete individuato per
la definizione delle domande (lezione 1), farne uno
studio di correlazione (su Python):**

**1- Individuare e applicare, motivando opportunamente, la
statistica di correlazione più opportuna**

**2- Calcolare il coeff r di correlazione**

**3- Calcolare r2 e significatività statistica (con 𝛼 = 0.05)**

**4- Fare valutazioni su causalità / non-causalità dell’eventuale
correlazione trovata**

Questo task analizza il dataset 'World Happiness Report 2019' scaricato da Kaggle per esplorare le correlazioni tra le diverse variabili numeriche presenti. Inizialmente, il dataset viene caricato, le righe contenenti valori mancanti vengono rimosse e viene calcolata e visualizzata la matrice di correlazione per tutte le colonne numeriche. Il coefficiente di correlazione di Pearson è stato scelto come statistica appropriata per misurare la relazione lineare tra le variabili continue del dataset. Per ogni coppia di variabili numeriche, vengono calcolati il coefficiente di correlazione di Pearson, il coefficiente di determinazione (r²) e il p-value per valutare la significatività statistica della correlazione, utilizzando una soglia alpha di 0.05. Infine, viene identificata e stampata la coppia di variabili che presenta la correlazione più elevata in valore assoluto.

1. Come statistica di correlazione si è scelto di impiegare il coefficiente di Pearson. Questa decisione si basa sulla natura delle variabili numeriche incluse nel dataset. Variabili come il punteggio di valutazione della vita, il Prodotto Interno Lordo pro capite, l'aspettativa di vita in salute, il livello percepito di supporto sociale, la libertà di compiere scelte di vita, la generosità e la percezione della corruzione, sono tutte espresse su scale continue o quantitative. Il coefficiente di Pearson è lo strumento statistico standard e più appropriato per indagare la relazione lineare tra variabili che presentano questa caratteristica.

2. Il coefficiente di correlazione r di Pearson più elevato calcolato nel codice è 0.8736 e misura la relazione tra 'Log of GDP per capita' e 'Healthy life expectancy'.

3. Questa relazione presenta un valore del coefficiente di determinazione (r²) pari a 0.7632. Il p-value associato è risultato essere molto basso e vicino allo zero, il che indica una buona significatività statistica della correlazione osservata.

4. Il 'Log of GDP per capita' rappresenta il prodotto interno lordo (PIL) pro capite di un Paese, trasformato con il logaritmo per ridurre l'effetto di enormi differenze tra Paesi molto ricchi e poveri.
Questo permette di fare comparazioni più eque tra economie di dimensioni diverse. D'altra parte, 'Healthy life expectancy' è il numero medio di anni che una persona può aspettarsi di vivere in buona salute, considerando anche disabilità o malattie che riducono la qualità della vita. Anche se è vero che un PIL più alto tende ad essere associato a migliori strutture sanitarie, educazione e benessere generale, non possiamo affermare con certezza che un aumento del PIL causi direttamente una vita più sana. Ad esempio, Paesi con un PIL elevato come la Svizzera o la Norvegia hanno accesso a migliori ospedali, sistemi sanitari più avanzati e programmi di prevenzione che possono migliorare l'aspettativa di vita sana ma alcune variabili come il sistema educativo, le politiche governative o la qualità dell'aria possono giocare un ruolo altrettanto importante. Inoltre, alcuni Paesi con un PIL basso, ma con buone politiche sanitarie, come Cuba, potrebbero avere una vita sana relativamente lunga nonostante una minore ricchezza economica.