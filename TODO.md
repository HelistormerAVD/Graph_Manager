


# Aktuelle Priorisierte Aufgaben:
### - view: "onLoadEditor()" muss noch funktionieren. (Kenneth)
### - view: "onDisconnectLink()" muss noch geschrieben werden. (Lorenz)
### - view: "onDeleteBlock()" muss gefixt werden, vermutlich mit update Blocks Lösch-Anomalie (Kenneth)
### - view/blocks: for schleife implementieren. (Kenneth)
### - view/blocks: if Bedingung implementieren. (Kenneth)
### - blocks: blöcke anpassen zu den Funktionen und Textfeldern (Victoria)

### --------------------------------------------------------------------------------------------------------
### - dataTypes: BDList muss erstellt werden (aktuell nur das gleiche wie BDString) (Lorenz)
### - block: graph (+ image) Blöcke erstellen. (Victoria)
    -   Funktionen dazu (Lorenz)
### - view: Das Laden von skripten erstellen. (Lorenz + Kenneth)
### - view: Das Speichern von skripten erstellen. (Lorenz + Kenneth)
### - view: Das Löschen von Blöcken + alle Dictionary-Einträge. (Kenneth)
### - view: Execution verbessert werden. (Kenneth)
### - view/block: Die Variablen müssen funktionieren. (Kenneth)
### - view/block: Der "Function"-, "Goto"-, "If_Else"-, Block muss noch funktionierend gemacht werden. (Kenneth)
### - view/block: Der Schleifen Block muss noch funktionierend gemacht werden. (Kenneth)



### --------------------------------------------------------------------------------------------------------
### - Blöcke hinzufügen (die initBlock_...) nach Muster (Victoria)
### - Block_selection fixen (was wenn Block gelöscht oder gleich bei dual Selection) (Kenneth)
### - Versuchen Fehler zu finden bei updateBlockPosition bzw. (Wenn Blöcke verlinkt werden sind sie nicht aligned) (Lorenz)
### - Selection fixen (ähnlich wie in der Kommentierten Tabelle). (Lorenz)
### - viewK: onDeleteBlock() darf keinen Start- und Endblock Löschen. (Kenneth)
### - viewK: onExecuteScript() simple Hilfsmethoden schreiben, um DataTypes der Blöcke zu bekommen. (Kenneth)
### - viewK: block Menu anpassen (vervollständigen). (Kenneth)
### - dataTypes: Datentypen Klassen umschreiben, sodass alle von "onExecuteScript()" aufgerufen werden können. (Kenneth)
### - viewK: ersten Compiler Schreiben für "onExecuteScript()". (Kenneth)

### --------------------------------------------------------------------------------------------------------

##    Priorisierte Aufgaben:
### - view: onCreateLink() schreiben (Lorenz)
### - view: onDeleteBlock() schreiben (Victoria)
### - view: onExecuteScript() schreiben (Kenneth)
### - scriptVariable: erstellen + funktionen (Kenneth)
### - view: updateBlockPosition() fixen (Kenneth)
### - block: moveBlock() fixen (Kenneth)
### - view: add_block() generischer machen (Kenneth)
### - block_components: componenten anpassen + generischer machen (Kenneth)

### --------------------------------------------------------------------------------------------------------
## TODO:
### - Block Klasse erstellen/verwendbar machen. (Kenneth)
    - generelle Blockfunktionen hinzufügen, wie (z.B. getPosition, getComponents, ...)
    - Einzelne Blockarten erstellen (initialisieren wie bei "__init__")
### - BlockComponents funktionsfähig machen. (Victoria)
    - generelle Funktionen hinzufügen, wie (getPosition, changePosition, ...)
### - Funktionen für DataTypes schreiben. (Lorenz)
    - 
### - view mit den Objekten (wie Block.py) verknüpfen, bzw. verwenden
    - Snapping von den Blöcken soll über die Tools funktionieren (click on Block = snapp)
    - verlinkung soll auch mit einem Tool gemacht werden ebenso 
### - Block Klasse erstellen/verwendbar machen.
    - Einzelne Blockarten erstellen (initialisieren wie bei "__init__")
### - BlockComponents verbessern (funktionen ergänzen wie überprüfung der Eingabe, z.B. ob nur Nummern erlaubt sind.)
### - FileIO an die Blöcke etc. Anpassen 
#### - Funktionen Abgabe Konform machen
#### - Funktionen richtig Kommentieren