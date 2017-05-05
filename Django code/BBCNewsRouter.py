class BBCRouter(object):
    """
    A router to control all database operations on models in the
    BBCNews application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read BBCNews models go to BBC.
        """
        if model._meta.app_label == 'BBCNews':
            return 'BBC'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write BBCNews models go to BBC.
        """
        if model._meta.app_label == 'BBCNews':
            return 'BBC'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the BBCNews app is involved.
        """
        if obj1._meta.app_label == 'BBCNews' or \
           obj2._meta.app_label == 'BBCNews':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the BBCNews app only appears in the 'BBC'
        database.
        """
        if app_label == 'BBCNews':
            return db == 'BBC'
        return None