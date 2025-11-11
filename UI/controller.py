import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    def popola_dropdown(self):
        musei = ["Nessun filtro"] + [m.nome for m in self._model.get_musei()]
        epoche = ["Nessun filtro"] + self._model.get_epoca()

        self._view.dd_museo.options.clear()
        self._view.dd_epoca.options.clear()

        self._view.dd_museo.options.extend([ft.dropdown.Options(m) for m in musei])
        self._view.dd_epoca.options.extend([ft.dropdown.Options(e) for e in epoche])

        self._view.dd_museo.value = "Nessun filtro"
        self._view.dd_epoca.value = "Nessun filtro"

        self._view.page.update()


    # CALLBACKS DROPDOWN
    def on_museo_change(self, e):
        self.museo_selezionato = e.control.value
        print(f"[DEBUG] Museo selezionato: {self.museo_selezionato}")

    def on_epoca_change(self, e):
        self.epoca_selezionata = e.control.value
        print(f"[DEBUG] Epoca selezionato: {self.epoca_selezionata}")
    # AZIONE: MOSTRA ARTEFATTI
    def mostra_artefatti(self, e=None):

        museo = self.museo_selezionato
        epoca = self.epoca_selezionata

        if epoca is None:
            epoca = self._view.dd_epoca.value
        if museo is None:
            museo = self._view.dd_museo.value

        artefatti = self._model.get_artefatti_filtrati(museo, epoca)

        if artefatti:
            self._view._mostra_lista_artefatti(artefatti)
        else:
            mostra_alert("Nessun artefatto trovato per i filtri selezionati")

