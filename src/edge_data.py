class edge_data:
    def __init__(self,src=0,dest=0,weight=0.0):
        self.src =src
        self.dest = dest
        self.weight=weight
        self.tag= -1
        self.info=""

    def get_src(self):
        return self.src

    def get_dest(self):
        return self.dest

    def get_weight(self):
        return self.weight

    def get_tag(self):
        return self.tag

    def set_tag(self,tag):
        self.tag=tag

    def set_info(self, info):
        self.info = info

    def get_info(self):
        return self.info

    def _repr_(self):
        return "(src: {}, dest: {}, weight: {})".format(self.src, self.dest, self.weight)