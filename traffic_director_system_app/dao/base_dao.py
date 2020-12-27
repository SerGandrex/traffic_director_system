class BaseDAO:
    MODEL_CLASS = None

    def save(self, obj):
        if not obj:
            return False
        obj.save()

        return True

    def delete(self, obj):
        if not obj:
            return False
        obj.delete()

        return True

    def get_all(self):
        return self.MODEL_CLASS.objects.all()

    def get(self, key):
        return self.MODEL_CLASS.objects.get(pk=key)

    def filter_by_kwargs(self, **kwargs):
        return self.MODEL_CLASS.objects.filter(**kwargs)


