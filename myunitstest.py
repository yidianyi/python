class Dict(dict):
    def __init__(self,*args,**kw):
        super(Dict, self).__init__(*args,**kw)
    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError('no this attribute %s'%item)
    def __setattr__(self, key, value):
        self[key]=value


