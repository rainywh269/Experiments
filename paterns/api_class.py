from collections import namedtuple

class FieldDesc(object):
    def gen_doc(self, intent=0):
        return self.__doc__

    def set(self, val):
        self.val = val
        return self

    def to_json(self):
        return self.val


class Str(FieldDesc):
    '''string value'''

class Int(FieldDesc):
    '''int value'''

class Array(FieldDesc):
    def __init__(self, ele_type):
        self.__ele_type = ele_type

    def gen_doc(self, indent=0):
        return "[%s]" % self.__ele_type.gen_doc(indent)

    def to_json(self):
        return [self.__ele_type.set(i).to_json() for i in self.val]

class CompoundFieldDesc(object):
    def fields(self):
        for k, v in self.__class__.__dict__.iteritems():
            if issubclass(v.__class__, FieldDesc):
                yield (k, v)

    def gen_doc(self, indent=0):
        out = []
        for k, f in self.fields():
            out.append("%s%s:%s," % ('\t'*(indent+1), k, f.gen_doc(indent+1)))
        return "{\n%s\n%s}" % ("\n".join(out), '\t'*(indent))

    def set(self, data):
        self.val = data
        return self

    def to_json(self):
        out = {}
        for k, f in self.fields():
            out[k] = f.set(getattr(self.val, k)).to_json()
        return out

class CelebrityDesc(CompoundFieldDesc):
    class RelatedWork(CompoundFieldDesc):
        title = Str()
        id = Int()

    name = Str()
    id = Int()
    other_cn_names = Array(Str())
    related_works = Array(RelatedWork())


Work = namedtuple('Work', ['title', 'id'])

class FakeCelebrity(object):
    def __init__(self):
        self.name = "wahahah"
        self.id = 1001
        self.related_works = [Work(i, 'title'+str(i)) for i in range(2)]
        self.other_cn_names = ["hello", "world"]

    def to_json(self):
        return CelebrityDesc().set(self).to_json()

if __name__ == '__main__':
    m = CelebrityDesc()
    print 'doc'
    print m.gen_doc()
    print 'data'
    print FakeCelebrity().to_json()
    # gen doc
    # 
#    print m.transform(Data())
