class CduRouter(object):
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read auth models go to auth_db.
        """
        if model._meta.app_label == 'cdu':
            return 'gisdata'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth models go to auth_db.
        """
        if model._meta.app_label == 'cdu':
            return 'gisdata'
        return None

    def allow_syncdb(self, db, model):
        """
        Make sure the auth app only appears in the 'gisdata'
        database.
        """
        if db == 'gisdata':
            return model._meta.app_label == 'cdu'
        elif model._meta.app_label == 'cdu':
            return False
        return None