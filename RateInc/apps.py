from django.apps import AppConfig

class RateincConfig(AppConfig):
    name = 'RateInc'

    def ready (self):
        print('signal is ready')
        import RateInc.signals
     

    
